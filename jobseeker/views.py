from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView
from jobseeker.forms import Registration,Studentprofile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from myapp.models import student
# Create your views here.

class Register(CreateView):
    template_name="jobseeker/register.html"
    form_class=Registration
    model=User
    success_url = reverse_lazy("signin")

# class Signin(View):
#     def get(self,request,*args,**kwargs):
#         form=Loginform()
#         return render(request,"jobseeker/login.html",{"form":form})
    
#     def post(self,request,*args,**kwargs):
#         form=Loginform(request.POST)
#         if form.is_valid():
#             u_name=form.cleaned_data.get("username")
#             pwd=form.cleaned_data.get("password")
#             user_obj=authenticate(request,username=u_name,password=pwd)
#             if user_obj:
#                 login(request,user_obj)
#                 return redirect
#             else:
#                 print("false dredentials")
#         return redirect("reg")

class Student_home(TemplateView):
    template_name="jobseeker/index.html"

class Jobseeker_profile(CreateView):
    template_name="jobseeker/profile.html"
    form_class=Studentprofile
    model=student
