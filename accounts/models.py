from django.db import models
from django.contrib.auth.models import User


class Profilemodel(models.Model):
    #one user can only has one profile.
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user', related_name="profile")
    # Name = models.CharField(max_length=100, verbose_name='Name')
    # Family = models.CharField(max_length=100, verbose_name='Family')

    Man=1
    Woman=2
    status_choices=((Man, 'Man'),
                    (Woman, 'Woman'))
    Gender = models.IntegerField(choices=status_choices, verbose_name='Gender')
    Profile_image = models.ImageField(upload_to="profile_images/", verbose_name='picture')
    Credit = models.IntegerField(verbose_name='credit', default=0)

    class Meta:
        verbose_name='PROFILE'
        verbose_name_plural='PROFILE'

