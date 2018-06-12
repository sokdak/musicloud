from django import forms
from django.contrib.auth.models import User
from mc.models import Album, Track


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fileds = ['artist', 'publisher', 'release_date']

class TrackForm(forms.ModelForm):

    class Meta:
        model = Track
        fileds = ['name', 'sex', 'is_group']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fileds = ['username', 'email', 'password']