from django import forms
from movierater.models import Rating

class RatingForm(forms.Form):
    class Meta:
        model = Rating
        fields = ('rating')
