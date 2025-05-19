from django import forms
from .models import CV

class EducationForm(forms.Form):
    school = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Okul/Üniversite Adı'}))
    degree = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bölüm/Derece'}))
    year = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Yıl'}))

class ExperienceForm(forms.Form):
    company = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Şirket Adı'}))
    position = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pozisyon'}))
    duration = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Çalışma Süresi'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'İş Tanımı', 'rows': 3}))

class SkillForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Beceri Adı'}))
    level = forms.ChoiceField(choices=[
        ('Başlangıç', 'Başlangıç'),
        ('Orta', 'Orta'),
        ('İyi', 'İyi'),
        ('Uzman', 'Uzman')
    ], widget=forms.Select(attrs={'class': 'form-control'}))

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['name', 'email', 'phone', 'photo', 'template']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız Soyadınız'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta Adresiniz'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon Numaranız'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'template': forms.HiddenInput(),
        }
