from django.urls import path
from jobseeker import views

urlpatterns = [
    path("reg/",views.Register.as_view(),name="reg"),
    path("signin/",views.Signin.as_view(),name="signin")
]