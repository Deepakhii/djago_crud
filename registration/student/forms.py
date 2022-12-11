from django import forms
from . import models
class StudentRegForms(forms.ModelForm):
    ENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name= forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':"form-control"}))
    email   = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
    mobile  = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control input-group"}))
    gender  = forms.CharField(max_length=6, label="Gender",
                                initial='M',
                                widget=forms.Select(choices=ENDER_CHOICES,attrs={'class':"form-control form-control"}),
                                required=True)
    dob     = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':"form-control"}))
    file    = forms.FileField(widget=forms.FileInput(attrs={'class':"form-control"}))
    password = forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'class':"form-control"}))
    class Meta:
        model = models.StudentReg
        fields =['name','email','mobile','gender','dob','file','password']
        labels = {'name':'Name','email':'Email'}
