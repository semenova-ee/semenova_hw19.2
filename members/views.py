from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetView
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import DetailView

from .forms import RegisterUserForm
from .models import CustomUser
from .tokens import account_activation_token


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Welcome!")
            return redirect('catalog:index')
        else:
            messages.success(request, "There Was An Error Logging In, Try Again...")
            return redirect('members:login')

    else:
        return render(request, 'members/authenticate/login.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('catalog:index')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.success(request, ("Registration Successful!"))
            send_email(user, form)
            messages.success(request, ("Please confirm your email"))
            return redirect("members:login")
    else:
        form = RegisterUserForm()
    return render(request, 'members/authenticate/register_user.html', {
        'form': form,
    })

def send_email(user, form):
    mail_subject = 'Activation link has been sent to your email id'
    message = render_to_string('members/email/verify_email_message.html',
                               {'user': user,
                                'domain': "127.0.0.1:8000",
                                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                'token': account_activation_token.make_token(user),
                                })
    to_email = form.cleaned_data.get('email')
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()

def verify_email(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


class ProfileUser(DetailView):
    model = CustomUser
    template_name = 'members/profile_user.html'
    context_object_name = "custom_user"


class CustomPasswordResetView(PasswordResetView):
    base_class = PasswordResetView
    template_name = 'members/pass/password_reset_form.html'
    email_template_name = 'members/pass/password_reset_email.html'
    success_url = reverse_lazy('members:password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'members/pass/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'members/pass/password_reset_confirm.html'
    success_url = reverse_lazy('members:password_reset_complete')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your password has been reset successfully.')
        # Log the user in automatically after password reset
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['new_password1'])
        login(self.request, user)
        return response



class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'members/pass/password_reset_complete.html'
