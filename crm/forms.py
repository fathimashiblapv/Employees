from django import forms
from crm.models import Employees
from django.contrib.auth.models import User

class EmployeesForm(forms.Form):
    Name=forms.CharField()
    Department=forms.CharField()
    Salary=forms.IntegerField()
    Email=forms.EmailField()
    Contact=forms.CharField()
    Age=forms.IntegerField()
    DOB=forms.DateField()


class EmployeesModelForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields="__all__"

        widgets={
            "Name":forms.TextInput(attrs={"class":"form-control"}),
            "Department":forms.TextInput(attrs={"class":"form-control"}),
            "Salary":forms.NumberInput(attrs={"class":"form-control"}),
            "Email":forms.EmailInput(attrs={"class":"form-control"}),
            "Contact":forms.Textarea(attrs={"class":"form-control"}),
            "Age":forms.NumberInput(attrs={"class":"form-control","rows":5}),
            "DOB":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }




class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    






    
    
