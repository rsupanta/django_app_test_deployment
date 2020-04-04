from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.


class userDB(models.Model):
    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    username = models.CharField(unique=True, max_length=50)

    email = models.EmailField(unique=True)

    photo = models.ImageField(
        upload_to='gallery',
        default='gallery/img.jpeg',
        blank=True
    )

    def __str__(self):
        return "Name: " + self.first_name + " " + self.last_name + " ||| User Name: " + self.username + "    |||   Email: " + self.email


class UserProfileInfo(models.Model):

    # built-it

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    # additional

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(
        upload_to='profile_pics',
        blank=True
    )

    def __str__(self):
        return self.user.username
