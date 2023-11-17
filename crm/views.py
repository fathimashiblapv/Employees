from django.shortcuts import render,redirect
from django.views.generic import View
from crm.forms import EmployeesForm,EmployeesModelForm,RegistrationForm,LoginForm
from crm.models import Employees
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator



def signin_required(fn):

    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"Invalid Session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

@method_decorator(signin_required,name="dispatch")
class EmployeesCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeesModelForm()
        return render(request,"emp-add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=EmployeesModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully Added")
            # Employees.objects.create(**form.cleaned_data)
            print("created")
            return render(request,"emp-add.html",{"form":form})
        else:
            messages.error(request,"Failed To Add Employee")
            return render(request,"emp-add.html",{"form":form})
            

@method_decorator(signin_required,name="dispatch")
class EmployeesListView(View):
    def get(self,request,*args,**kwargs):
       qs=Employees.objects.all()
       Departments=Employees.objects.all().values_list("Department",flat=True).distinct()
       print(Departments)

       if "Department" in request.GET:
           dept=request.GET.get("Department")
           qs=qs.filter(Department__iexact=dept)

       return render(request,"emp-list.html",{"data":qs,"Departments":Departments})
        
        
    def post(self,request,*args,**kwargs):
        name=request.POST.get("Box")
        qs=Employees.objects.filter(Name__icontains=name)
        return render(request,"emp-list.html",{"data":qs})
    
@method_decorator(signin_required,name="dispatch")
class EmployeesDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        return render(request,"emp-detail.html",{"data":qs})
    
@method_decorator(signin_required,name="dispatch")
class EmployeesDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")  
        Employees.objects.get(id=id).delete()
        messages.success(request,"Deleted")
        return redirect("emp-all")
    
@method_decorator(signin_required,name="dispatch")
class EmplyeesUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Employees.objects.get(id=id)
        form=EmployeesModelForm(instance=obj)
        return render(request,"emp-edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Employees.objects.get(id=id)
        form=EmployeesModelForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated")
            return redirect("emp-detail",pk=id)
        else:
            messages.error(request,"Failed To update")
            return redirect(request,"emp-edit.html",{"form":form})
        

class SignUpView(View):
    def get (self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"created")
            return render(request,"register.html",{"form":form})
        else:
            messages.error(request,"failed")
            return render(request,"register.html",{"form":form})
        

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            print(request.user,"before")
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            User_obj=authenticate(request,username=u_name,password=pwd)
            if User_obj:
                print("valid")
                login(request,User_obj)
                print(request.user,"after")
                return redirect("emp-all")
        messages.error(request,"invalid credential")
        return render(request,"login.html",{"form":form})
        
@method_decorator(signin_required,name="dispatch")           
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
        
