


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from user_app.models import Booking, Review

# Create your views here.

@login_required
def create_review(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, traveler__user_profile=request.user.userprofile)

    if request.method == 'POST':
        rating = int(request.POST['rating'])
        comment = request.POST['comment']

        # Create the review
        review = Review.objects.create(author=request.user.travelerprofile, listing=booking, rating=rating, comment=comment)

        # Optionally, you can perform additional actions here, such as updating the experience's overall rating or sending notifications.

        # Redirect the user to a thank you page or the experience detail page
        return render(request, 'reviews/thank_you.html')

    # Render the review creation form
    return render(request, 'reviews/create_review.html', {'booking': booking})


def finished_app(request):
    return render(request,'finished_app/finished_app.html')