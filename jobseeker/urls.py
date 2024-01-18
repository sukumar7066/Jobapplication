from django.urls import path
from jobseeker import views

urlpatterns = [
    path("reg/",views.Register.as_view(),name="reg"),
    # path("signin/",views.Signin.as_view(),name="signin")
    path("seeker/",views.Student_home.as_view(),name="seekerindex"),
    path("create_profile/",views.Jobseeker_profile.as_view(),name="profile")
]