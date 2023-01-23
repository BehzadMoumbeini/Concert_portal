from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Concertmodel, Locationmodel, Timemodel
import accounts, ticketsales
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SearchForm, ConcertForm


def concertListView(request):

    #make instance
    searchForm=SearchForm(request.GET)
    if searchForm.is_valid():
        SearchText = searchForm.cleaned_data["SearchText"]
        concerts = Concertmodel.objects.filter(Name__contains=SearchText)
    else:
        concerts = Concertmodel.objects.all()

    context = {
        "concertlist":concerts,
        "concertcount":concerts.count(),
        "SearchForm":searchForm
    }
    return render(request, "ticketsales/concertlist.html", context)

@login_required
def locationListView(request):
    locations = Locationmodel.objects.all()
    context = {
        "locationlist":locations,
    }
    return render(request, "ticketsales/locationlist.html", context)


def concertDetailsView(request, concert_id):
    concert = Concertmodel.objects.get(pk=concert_id)

    context = {
        "concertdetails":concert
    }

    return render(request, "ticketsales/concertdetails.html",context)

@login_required
def timeView(request):
    # if request.user.is_authenticated and request.user.is_active:

        times = Timemodel.objects.all()
        context = {
            "timelist":times,
        }
        return render(request, "ticketsales/timelist.html", context)

    # else:
    #     return HttpResponseRedirect(reverse(accounts.views.loginView))

def concertEditView(request, concert_id):
    concert = Concertmodel.objects.get(pk=concert_id)
    if request.method=="POST":
        concertForm = ConcertForm(request.POST, request.FILES, instance=concert)
        if concertForm.is_valid:
            concertForm.save()
            return HttpResponseRedirect(reverse(accounts.views.concertListView))

    else:
        concertForm = ConcertForm(instance=concert)

    context = {
        "concertForm":concertForm,
        "PosterImage": concert.Poster
    }

    return render(request, "ticketsales/concertEdit.html",context)
