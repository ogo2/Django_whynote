from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormView
from .forms import RegisterUserForm
from . forms import RegisterUserForm
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from .forms import *
# def index(request):
#     name = Users.name
#     country = Users.objects.get(id=1)
#     about_me = Users.about_me
#     return render(request, 'profile_user/index.html', {'name': name, 'country': country, 'about_me': about_me})



def profile2(request, username):
    # current_user = request.user
    # print(user_id)

    user = User.objects.all()
    user_info = User.objects.get(username=username)
    # profile = Profile.objects.get(user=request.user)
    f = user_info.profile
    print(f.photo)
    # print(user.index(username))

    # profile_info = Profile.objects.all().filter(user=username)
    # name_user = user[username]


    # print(name_user)
    return render(request, 'profile_user/profile.html', {'users': user, 'name_user': username,
                                                         'info_user': user_info.profile})



class profile(DetailView):
    model = User
    context_object_name = 'Profile'
    template_name = 'profile_user/profile.html'
    # name = Users.objects.get(id=1)
    # country = Users.country
    # about_me = Users.about_me
    # return render(request, 'profile_user/profile.html')


def login_user(request):
    return render(request, 'profile_user/login.html')


class RegisterUser(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'profile_user/registr.html'
    success_url = reverse_lazy('login')
    success_msg = 'Пользователь успешно создан'

    # def form_valid(self, form):
    #     print('lol good1')
    #     form_valid = super().form_valid(form)
    #     username = form.cleaned_data["username"]
    #     password = form.cleaned_data["password"]
    #     aut_user = authenticate(username=username, password=password)
    #     login(self.request, aut_user)
    #     return form_valid

    def get_context_data(self, **kwargs):
        print('lol good2')

        context = super().get_context_data()
        return context



    def form_invalid(self, form):
        return super(RegisterUser, self).form_invalid(form)
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title='Регистрация')
    #     return dict(list(context.items()) + list(c_def.items()))

class LoginUser(LoginView):
    form_class = LodinUserForm
    template_name = 'profile_user/login.html'

    def get_success_url(self, **kwargs):

        return reverse_lazy('index')

def logout_user(request):
    logout(request)
    return redirect('login')