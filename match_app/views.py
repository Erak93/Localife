from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Experience,Booking
from django.http import HttpResponse, Http404



# Create your views here.



def match_app(request):
    return render(request,'match_app/match_app.html')

# def get_experience_id():
#     experience = Experience.objects.get(id=experience_id)
#     return experience

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Experience, Booking

def book_offer(request, experience_id):
    try:
        experience = Experience.objects.get(id=experience_id)
    except Experience.DoesNotExist:
        raise Http404("Experience does not exist")

    booking_success = Booking()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.product = experience  
            booking.user = request.user
            booking.save()

            booking_success.complete_payment()

            return redirect('match_app:booking_success')

    else:
        form = BookingForm()

    context = {
        'experience': experience,  
        'form': form
    }

    return render(request, 'booking.html', context)

def booking_success(request):
    return HttpResponse("booking success! great job gimme that money!")
