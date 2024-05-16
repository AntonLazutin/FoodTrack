from django.urls import path
from . import views


urlpatterns = [
    path('', views.LoginPageView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.LogoutPageView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('<int:pk>/update', views.UserUpdateView.as_view(), name='user_update'), 
    path('chart/', views.line_chart, name='line_chart'),
    path('chartJSON/', views.line_chart_json, name='line_chart_json'),
]