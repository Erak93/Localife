from django import forms
from user_app.models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields='__all__'