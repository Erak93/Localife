from django.db import models
from django.contrib.auth.models import User
#from django_google_maps import fields as map_fields


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The user inherit from abstractUser which already has username, first name, last name, email and password
    # Add additional fields for user profile information
    # For example: location, bio, profile picture, etc.
    location=models.CharField(max_length=50)
    #address = map_fields.AddressField(max_length=200)
    #geolocation = map_fields.GeoLocationField(max_length=100)
    user_profile_image= models.ImageField(upload_to='profile_pics')
   
    def __str__(self):
        return self.user.username


class TravelerProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # Add additional fields specific to travelers
    # For example: interests, preferred destinations, etc.



    def __str__(self):
        return self.user_profile.user.username


class ExperienceTag(models.Model):
    tag_name=models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name



class Experience(models.Model):
    host = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,blank=False)
    # Add additional fields for listing details
    # For example: location, price, availability, etc.
    price = models.DecimalField(max_digits=12, decimal_places=2)
    experience_tags = models.ManyToManyField(ExperienceTag)    
    experience_image = models.ImageField(upload_to='experience_pics',blank=False)


    def __str__(self):
        return self.title


class Booking(models.Model):
    traveler = models.ForeignKey(TravelerProfile, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    # Add additional fields for booking details
    # For example: total price, status, etc.

    def __str__(self):
        return f"{self.traveler.user_profile.user.username} - {self.listing.title}"


class Review(models.Model):
    author = models.ForeignKey(TravelerProfile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Experience, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f"{self.author.user_profile.user.username} - {self.listing.title}"
    