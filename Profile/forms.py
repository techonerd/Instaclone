from django import forms
from .models import User, Post, Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'