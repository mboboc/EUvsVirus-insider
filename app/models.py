from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.validators import RegexValidator


# Create your models here.

class Volunteer(User):
    user = models.OneToOneField(AbstractBaseUser, on_delete=models.CASCADE, primary_key=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    age = models.IntegerField(null=False)
    address = models.CharField(max_length=80)

    REQUIRED_FIELDS = ['username', 'password', 'email', 'first-name', 'last-name']
    USERNAME_FIELD = 'user'
