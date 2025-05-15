from django import forms
from .models import UserProfile, WorkExperience, Education, Hobby

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'photo', 'selected_template']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        exclude = ['user_profile']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['user_profile']

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        exclude = ['user_profile']
