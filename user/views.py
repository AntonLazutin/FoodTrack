from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserRegisterForm
# from django.contrib.auth.forms import UserCreationForm


class LoginPageView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('meal_log') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"
    

class LogoutPageView(View):

    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect((reverse_lazy('login')))


class ProfileView(View):
    template_name='profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name='profile.html')