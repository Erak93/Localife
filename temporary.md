# CHOICES FOR USER
from .models_choices import (
    GENDER_CHOICES,
    COLOR_CHOICES,
    FABRIC_CHOICES,
    FABRIC_THICKNESS_CHOICES,
    BRAND_CHOICES,
    TYPE_CHOICES,
    SIZE_CHOICES,
    CONDITION_CHOICES,
    ENVIRONMENT_CHOICES,
)


class User(AbstractUser):
    # fields we inherit from AbstractUser:
    # username, password, password_conf, email, first_name, last_name,
    # joining_date, last_login, is_staff, is_active, is_superuser
    email = models.EmailField(_("email address"), blank=True, unique=True)
    info_about = models.TextField(blank=True)
    info_birthday = models.DateField(default=timezone.now, blank=False)
    info_gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=False)
    # info_gender_interest = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=False)
    location_city = models.CharField(max_length=255, blank=False)
    location_latitude = models.FloatField(blank=True, null=True)
    location_longitude = models.FloatField(blank=True, null=True)
    notification = models.BooleanField(default=True)
    social_instagram = models.URLField(
        max_length=255,
        blank=True,
        null=True,
    )
    social_facebook = models.URLField(
        max_length=255,
        blank=True,
        null=True,
    )
    social_twitter = models.URLField(
        max_length=255,
        blank=True,
        null=True,
    )
    social_spotify = models.URLField(
        max_length=255,
        blank=True,
        null=True,
    )