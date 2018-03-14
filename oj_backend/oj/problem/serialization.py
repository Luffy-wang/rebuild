from rest_framework import serializers

from django import forms
class UploadForm(forms.Form):
    file=forms.FileField()