from django.urls import path
from . import views

urlpatterns=[
    path('',views.getData), # This setting some end points
    path('add/',views.addItem)

]