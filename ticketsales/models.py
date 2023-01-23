from django.db import models
from jalali_date import date2jalali, datetime2jalali
from accounts.models import Profilemodel

class Concertmodel(models.Model):
    Name = models.CharField(max_length=100, verbose_name='concert name')
    SingerName = models.CharField(max_length=100, verbose_name='singer name')
    Length = models.IntegerField(verbose_name='concert name')
    #pic should not be in the DB but has address
    Poster = models.ImageField(upload_to="concert_image/", null=True, verbose_name='poster')

    def __str__(self):
        return self.SingerName

    class Meta:
        verbose_name='CONCERT'
        verbose_name_plural='CONCERT'


class Locationmodel(models.Model):
    idNumber = models.IntegerField(primary_key=True, verbose_name='location code')
    Name = models.CharField(max_length=100, verbose_name='location name')
    Address = models.CharField(max_length=500, default="Amsterdam, ...", verbose_name='address')
    Phone = models.CharField(max_length=11, null=True, verbose_name='phone')
    Capacity = models.IntegerField(verbose_name='capacity')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name='LOCATION'
        verbose_name_plural='LOCATION'

#for sessions (the "time" that a concert is happening in a "location") ==> FK
class Timemodel(models.Model):
    Concertmodel = models.ForeignKey(to=Concertmodel, on_delete=models.PROTECT, verbose_name='concert name')
    Locationmodel = models.ForeignKey(to=Locationmodel, on_delete=models.PROTECT, verbose_name='location')
    StartDateTime = models.DateTimeField(verbose_name='concert date')
    Seats = models.IntegerField(verbose_name='no of seats')
    Start=1
    End=2
    Cancel=3
    Sale=4
    status_choices = ((Start, 'ticket sale is started for this session'),
                      (End, 'ticket sale is over'),
                      (Cancel, 'this session is canceled'),
                      (Sale, 'ticket is still being sold'))
    Status = models.IntegerField(choices=status_choices, verbose_name='status')

    def __str__(self):
        return "Time: {} ConcertName: {} Location: {}".format(self.StartDateTime, self.Concertmodel.Name, self.Locationmodel.Name)

    class Meta:
        verbose_name='TIME'
        verbose_name_plural='TIME'

    def get_jalali_date(self):
        return datetime2jalali(self.StartDateTime)







#the ticket is for a person for a session in a location
class Ticketmodel(models.Model):
    Profilemodel = models.ForeignKey(Profilemodel, on_delete=models.PROTECT, verbose_name='user')
    Timemodel = models.ForeignKey('Timemodel', on_delete=models.PROTECT, verbose_name='session')
    Name = models.CharField(max_length=100, verbose_name='title')
    Price = models.IntegerField(verbose_name='price')
    Ticket_image = models.ImageField(upload_to="ticket_images/", verbose_name='picture')

    def __str__(self):
        return "TicketInfo: Profile: {} ConcertInfo: {}".format(Timemodel.__str__())


    class Meta:
        verbose_name='TICKET'
        verbose_name_plural='TICKET'





