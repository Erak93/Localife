from django import forms
from user_app.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model=User # This needs to be called model and refers to the model the form refers to
        fields='__all__'    # This also needs to be called fields. In this case we want to use all the fields