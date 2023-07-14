from django.contrib import admin
from .models import UserProfile,TravelerProfile,Experience,ExperienceTag,Booking,Review,Region

# Register your models here.

#from django_google_maps import widgets as map_widgets
#from django_google_maps import fields as map_fields

#class UserProfileAdmin(admin.ModelAdmin):
  #  formfield_overrides = {
   #     map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
   # }

admin.site.register(UserProfile)
admin.site.register(TravelerProfile)
admin.site.register(ExperienceTag)
admin.site.register(Experience)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Region)


