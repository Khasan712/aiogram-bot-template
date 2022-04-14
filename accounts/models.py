from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from django_countries.fields import CountryField

# Create your models here.

class UserRelegion(models.Model):
    relegion = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Accounts(AbstractBaseUser, PermissionsMixin):
    phone_regex_validator = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+998991234567'. "
        "Up to 15 digits allowed.",
    )
    
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(validators=[phone_regex_validator], max_length=15, unique=True)
    relegion = models.ForeignKey(UserRelegion, on_delete=models.PROTECT, blank=True, null=True)
    # location = 
    country = CountryField(blank=True, null=True)
    bio = models.CharField(max_length=150, blank=True, null=True)
    # socila_links = 
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        verbose_name="date_joined", auto_now_add=True, null=True, blank=True
    )  # can't be blank
    last_login = models.DateTimeField(
        verbose_name="last_login", auto_now=True, null=True, blank=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


