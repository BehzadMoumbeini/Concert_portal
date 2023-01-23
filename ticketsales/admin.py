from django.contrib import admin

from .models import Concertmodel, Timemodel, Ticketmodel, Locationmodel

admin.site.register(Concertmodel)
admin.site.register(Ticketmodel)
admin.site.register(Locationmodel)
admin.site.register(Timemodel)
