from django import forms
from user_app.models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'description', 'price', 'experience_image']
    def save(self, commit=True, **kwargs):
        experience = super().save(commit=False)
        host = kwargs.get('host')  # Get the host from the keyword arguments
        if host:
            experience.host = host
        if commit:
            experience.save()
        return experience