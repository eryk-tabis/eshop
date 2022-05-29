from .forms import MyUserCreationForm, UserPasswordResetForm, MyUserLoginForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .tasks import user_created, password_change_requested
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import views as auth_views
from .forms import PasswordChangeForm
# Create your views here.


@csrf_protect
def logout_user(request):
    """
    View responsible for logout user
    """
    logout(request)
    return redirect('main_view')


@csrf_protect
def login_page(request):
    """
    View responsible for render /login page and login users
    """
    if request.user.is_authenticated:
        return redirect('main_view')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return to same site if redirected
            if request.POST.get('next'):
                return redirect(request.POST.get('next'))
            else:
                return redirect('main_view')
        else:
            messages.error(request, 'Username and password does not match')
    form = MyUserLoginForm
    return render(request, 'user/login.html', {'form': form})


@csrf_protect
def register_page(request):
    """
    View responsible for rendering /register page and registering users
    """
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if request.POST.get('receive_newsletter', ''):
                user.receive_newsletter = True
            user.save()
            login(request, user)
            user_created.delay(user.id)
            return redirect('main_view')
    return render(request, 'user/register.html', {'form': form})


@csrf_protect
def password_reset(request):
    """
    View responsible for rendering /password-reset page and sending emails
    """
    if request.method == 'POST':
        form = UserPasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            user = User.objects.get(email=data)
            if user:
                # sends email to user
                password_change_requested.delay(user.email)
                return redirect('password_reset_done')
    form = UserPasswordResetForm()
    return render(request, 'user/password_reset.html', {'form': form})


class PasswordResetDoneView(auth_views.PasswordResetCompleteView):
    """
    View responsible for rendering password-reset/done/ page
    """
    template_name = 'user/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    View responsible for rendering /reset page and changing passwords
    """
    template_name = 'user/password_reset_confirm.html'
    form_class = PasswordChangeForm


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    """
    View responsible for rendering reset/done/ page
    """
    template_name = 'user/password_reset_complete.html'
