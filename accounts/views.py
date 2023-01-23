from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import accounts.views
import ticketsales
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Profilemodel
from  .forms import ProfileRegisterForm

def loginView(request):
    #post
    if request.method=='POST':
        username=request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))

            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {
                "username": username,
                "errormessage": "WE DID NOT FIND THE USER"

            }
            return render(request, "accounts/login.html", context)
    #get
    else:
        return render(request, "accounts/login.html", {})


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(ticketsales.views.concertListView))

@login_required
def profileView(request):
    profile = request.user.profile

    context = {
        "profile":profile
    }

    return render(request,"accounts/profile.html", context)


def profileRegisterView(request):

    if request.method=="POST":
        profileRegisterForm = profileRegisterForm(request.POST,request.FILE)
        if profileRegisterForm.is_valid():

            user = User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],
                                            email=profileRegisterForm.cleaned_data["email"],
                                            password=profileRegisterForm.cleaned_data["password"],
                                            first_name=profileRegisterForm.cleaned_data["first_name"],
                                            last_name=profileRegisterForm.cleaned_data["last_name"])

            user.save()
            profileModel = Profilemodel(user=user, Profile_image=profileRegisterForm.cleaned_data['Profile_image'],
                                        Gender = profileRegisterForm.cleaned_data['Gender'],
                                        Credit = profileRegisterForm.cleaned_data['Credit'])

            profileModel.save()

            return HttpResponseRedirect(reverse(ticketsales.views.concertListView))
        else:
            profileRegisterForm = profileRegisterForm()

        context = {
            "formData": profileRegisterForm

        }


    return render(request, "accounts/profileRegister.html", context)


def ProfileEditView(request):

    if request.method=="POST":
        profileEditForm = ProfileEditForm(request.POST, request.FILES, instance = request.user.profile)
        if profileEditForm.is_valid:
            profileEditForm.save()
            return HttpResponseRedirect(reverse(accounts.views.profileView))
    else:
        profileEditForm = ProfileEditForm(instance=request.user.profile)

    context = {
        "profileEditForm":profileEditForm,
        "ProfileImage": request.user.profile.ProfileImage

    }

    return render(request, "accounts/profileEdit.html", context)
