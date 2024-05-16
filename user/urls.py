from django.urls import path
from . import views


urlpatterns = [
    path('', views.LoginPageView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.LogoutPageView.as_view(), name='logout'),
    path('profile', views.ProfileView.as_view(), name='profile'),
]