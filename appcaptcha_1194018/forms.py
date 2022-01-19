from django import forms
from appcaptcha_1194018.models import Captcha_Clicksor
from captcha.fields import CaptchaField
from django.core import validators

TIME_ZONE = [('(GMT) Cassablanca, Monrovia', '(GMT) Cassablanca, Monrovia'), ('(GMT+7) Jakarta', '(GMT+7) Jakarta'), ('(GMT+8) Australia', '(GMT+8) Australia'), ('(GMT+9) Russia', '(GMT+9) Russia')]
COUNTRY = [('Indonesia', 'indonesia'), ('Kontrakan', 'kontrakan'), ('Sarijadi', 'sarijadi'), ('Brazil', 'brazil'), ]

class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    country = forms.CharField(widget=forms.Select(attrs={'class':'form-select'},choices=COUNTRY))
    time_zone = forms.CharField(widget=forms.Select(attrs={'class':'form-select'},choices=TIME_ZONE))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    confirm_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    website = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    zip_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    
    captcha = CaptchaField()
    class Meta: 
        model = Captcha_Clicksor
        fields = '__all__'

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        confirm_email = all_clean_data['confirm_email']
        name = all_clean_data['name']
        website = all_clean_data['website']
        address = all_clean_data['address']
        company = all_clean_data['company']
        password = all_clean_data['password']
        confirm_password = all_clean_data['confirm_password']
        
        # Validator email harus sama
        if email != confirm_email:
            raise forms.ValidationError("MAKE SURE YOUR EMAILS MATCH")
        
        # Validator password harus sama
        if password != confirm_password:
            raise forms.ValidationError("MAKE SURE YOUR PASSWORD MATCH")
        
        # Validator nama
        if name[0].lower() != 'a':
            raise forms.ValidationError("NAMA HARUS DIAWALI HURUF A")
        
        # Validator Website
        if website[0].lower() != 'h':
            raise forms.ValidationError("ALAMAT WEBSITE HARUS DIAWALI DARI HURUF H")
        
        # Validator Address
        if address[0].lower() != 'j':
            raise forms.ValidationError("ALAMAT HARUS DIMULAI DARI HURUF J")
        
        # Validator Company
        if company[0].lower() != 'p':
            raise forms.ValidationError("PERUSAHAAN HARUS DIMULAI DARI HURUF P")
    