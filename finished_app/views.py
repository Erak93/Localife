from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from user_app.models import Review, Experience
from search_app.models import Booking
# Create your views here.

@login_required
def create_review(request, experience_id):
    experience = get_object_or_404(Experience, id=experience_id)
        # Check if the user has a valid booking for the given experience
    try:
        booking = Booking.objects.get(experience_name=experience.title, traveler=request.user.username)
    except Booking.DoesNotExist:
        # If the user doesn't have a booking, render the 'review_not_allowed.html' template
        return render(request, 'finished_app/review_not_allowed.html')
    # Check if the current date is after the enddate of the experience
    
    if timezone.now().date() < experience.end_date:
        return render(request, 'finished_app/review_untimely.html')
    
    # Check if a review already exists for this experience and user
    existing_review = Review.objects.filter(author=request.user.user_profile, listing=experience).first()
    if request.method == 'POST':
        rating = int(request.POST['rating'])
        comment = request.POST['comment']

        # If a review already exists, update it; otherwise, create a new one
        if existing_review:
            existing_review.rating = rating
            existing_review.comment = comment
            existing_review.save()
        else:
            review = Review.objects.create(author=request.user.user_profile, listing=experience, rating=rating, comment=comment)

        # Optionally, you can perform additional actions here, such as updating the experience's overall rating or sending notifications.

        # Redirect the user to a thank you page or the experience detail page
        user_reviews = Review.objects.filter(author=request.user.user_profile)
        return render(request, 'finished_app/thank_you.html', { 'user_reviews': user_reviews})
    user_reviews = Review.objects.filter(author=request.user.user_profile)
    # Render the review creation form
    return render(request, 'finished_app/create_review.html', {'experience': experience, 'user_reviews': user_reviews})


def finished_app(request):
    return render(request, 'finished_app/finished_app.html')