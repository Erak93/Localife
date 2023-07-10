from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Experience(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    picture = models.ImageField(upload_to='media')                    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='bookings')
    payment_status = models.BooleanField(default=False)


    def total_price(self):
        return self.Experience.price

    def complete_payment(self):
        # could also be done by making payment_status default true
        self.payment_status = True
        self.save()
