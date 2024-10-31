from django import forms
from .models import Interested

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interested
        fields = ['name', 'email', 'phone', 'age', 'starting_date', 'address', 'session']
        widgets = {
            'session': forms.HiddenInput(),  # This will be hidden and automatically set by the view
            'starting_date': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker for calendar
            'address': forms.TextInput(attrs={'placeholder': 'Optional'}),  # Optional address field with placeholder
        }


from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'review_text']
