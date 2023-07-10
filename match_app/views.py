from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Experience,Booking
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required



# Create your views here.



def match_app(request):
    return render(request,'match_app/match_app.html')

# def get_experience_id():
#     experience = Experience.objects.get(id=experience_id)
#     return experience


@login_required
def book_offer(request, experience_id):
    try:
        experience = Experience.objects.get(id=experience_id)
    except Experience.DoesNotExist:
        raise Http404("Experience does not exist")

    booking = Booking()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.product_id = experience.id # Assign the experience_id directly to the product_id field
            booking.user = request.user
            booking.save()

            booking.complete_payment()

            return redirect('match_app:booking_success')

    else:
        form = BookingForm()

    context = {
        'experience': experience,
        'form': form
    }

    return render(request, 'match_app/booking.html', context)


def booking_success(request):
    return HttpResponse("booking success! great job gimme that money!")


def available_experiences(request):
    experiences = Experience.objects.all()
    context = {
        'experiences': experiences
    }
    return render(request, 'match_app/experiences.html', context)

