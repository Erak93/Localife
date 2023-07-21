from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
#from django_google_maps import fields as map_fields


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="user_profile",
                                on_delete=models.CASCADE,null=True)
    # username = models.CharField(max_length=250, unique=True)
    # first_name = models.CharField(max_length=250)
    # last_name = models.CharField(max_length=250)
    # email = models.EmailField(("email address"), blank=False, unique=True)
    # password = models.CharField(max_length=200)
    # The user inherit from abstractUser which already has username, first name, last name, email and password
   
    location=models.CharField(max_length=200, blank=True)
    #address = map_fields.AddressField(max_length=200)
    #geolocation = map_fields.GeoLocationField(max_length=100)
    user_profile_image= models.ImageField(upload_to='user_app/profile_pics',blank=True, null=True)
    user_bio=models.TextField(default="Insert bio")
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='userprofile_set'  # Provide a unique related_name
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='userprofile_set'  # Provide a unique related_name
    )

    # additional customizations if needed

   
    def __str__(self):
        return f'{self.user.username}'


class TravelerProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    



    def __str__(self):
        return self.user_profile.user.username


class ExperienceTag(models.Model):
    tag_name=models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name

class Region(models.Model):
    region_name=models.CharField(max_length=255)
    region_desc=models.TextField(max_length=1000)

class Experience(models.Model):
    host = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,blank=False)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)    
    price = models.DecimalField(max_digits=12, decimal_places=2)
    experience_tags = models.ManyToManyField(ExperienceTag, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,default=1)  # Provide a default value hereRegion, on_delete=models.CASCADE)
    experience_image = models.ImageField(upload_to='experience_pics',blank=True, null=True)


    def __str__(self):
        return f'{self.title,self.id}'


class Booking(models.Model):
    traveler = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    

    def __str__(self):
        return f"{self.traveler.user_profile.user.username} - {self.listing.title}"


class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Experience, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f"{self.author} - {self.listing.title}"
    