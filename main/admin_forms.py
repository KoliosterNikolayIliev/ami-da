from django import forms

from .models import Image


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"

    def validate_unique(self):
        pass


class PlayModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"

    def validate_unique(self):
        pass


class VideoModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"

    def validate_unique(self):
        pass
