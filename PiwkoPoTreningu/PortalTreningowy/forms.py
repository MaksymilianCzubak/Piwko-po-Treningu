from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, validate_email
from django.forms import CheckboxSelectMultiple

from PortalTreningowy.models import Plan, TrainingSession, User, TrainingSessionNotes


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)

class NoteAddForm(forms.ModelForm):
    class Meta:
        widgets = {'user': forms.HiddenInput, 'training_session': forms.HiddenInput}
        fields = ('training_notes', 'user_weight', 'user_vo2max', 'hr_max', 'training_session', 'user')
        model = TrainingSessionNotes

        # training_session = forms.IntegerField(widget=forms.HiddenInput())
        # user = forms.IntegerField(widget=forms.HiddenInput())
        training_notes = forms.CharField(widget=forms.Textarea)
        user_weight = forms.FloatField(label="Waga Zawodnika", min_value=0.1)
        user_vo2max = forms.FloatField(label="V02max Zawodnika", min_value=0.1)
        hr_max = forms.IntegerField(label='Wprowadź tętno maksymalne', min_value=0)