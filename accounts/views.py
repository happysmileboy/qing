from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from allauth.account.views import SignupView, LoginView, PasswordResetView

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from django.core.mail import send_mail

from .models import EmailConfirm, User

from .utils import generate_random_string

from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required
from .decorators import mentee_required
from django.utils.decorators import method_decorator

from .forms import SignUpForm,MenteeSignUpForm, MentorSignUpForm

# Create your views here.


class MySignupView(SignupView):
    template_name = 'signup.html'


class MyLoginView(LoginView):
    template_name = 'login.html'



def signup_mentee(request, commit=True):
    signup_form = SignUpForm(request.POST or None)
    mentee_form = MenteeSignUpForm(request.POST or None, prefix='mentee')
    if request.method == 'POST':
        if signup_form.is_valid() and mentee_form.is_valid():
            User.is_mentee=True
            user = signup_form.save()
            mentee = mentee_form.save(commit=False)
            mentee.user = user
            mentee.save()
            return login_and_redirect_next(request, user)
    ctx = {
        'signup_form': signup_form,
        'mentee_form': mentee_form,
    }
    return render(request, 'signup_mentee.html', ctx)

def signup_mentor(request):
    signup_form = SignUpForm(request.POST or None)
    mentor_form = MentorSignUpForm(request.POST or None, prefix='mentor')
    if request.method == 'POST':
        if signup_form.is_valid() and mentor_form.is_valid():
            User.is_mentor_univ = True
            user = signup_form.save()
            mentee = mentor_form.save(commit=False)
            mentee.user = user
            mentee.save()
            return login_and_redirect_next(request, user)
    ctx = {
        'signup_form': signup_form,
        'mentor_form': mentor_form,
    }
    return render(request, 'signup_mentor.html', ctx)

class MentorSignUpView(CreateView):
    model = User
    form_class = MentorSignUpForm
    template_name = 'signup_mentor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'mentor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(reverse(settings.SIGNUP_REDIRECT_URL))


def Logout(request):
    auth_logout(request)
    return redirect(reverse(settings.LOGOUT_REDIRECT_URL))


class MyPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'


def send_confirm_mail(user):
    try:
        email_confirm = EmailConfirm.objects.get(user=user)
    except EmailConfirm.DoesNotExist:
        email_confirm = EmailConfirm.objects.create(
            user=user,
            key=generate_random_string(length=60),
        )

    url = '{0}{1}?key={2}'.format(
        'http://localhost:8000',
        reverse('accounts:confirm_email'),
        email_confirm.key,
    )
    html = '<p>계속하시려면 아래 링크를 눌러주세요.</p><a href="{0}">인증하기</a>'.format(url)
    send_mail(
        '인증 메일입니다.',
        '',
        settings.EMAIL_HOST_USER,
        [user.email],
        html_message=html,
    )


def login_and_redirect_next(request, user):
    if EmailConfirm.objects.filter(user=user, is_confirmed=True).exists():
        auth_login(request, user)
        next_url = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
        return redirect(next_url)
    else:
        send_confirm_mail(user)
        return redirect(reverse('accounts:email_confirm_sent'))

def email_confirm_sent(request):
    return render(request, 'email/email_confirm_sent.html')


def confirm_email(request):
    key = request.GET.get('key')
    email_confirm = get_object_or_404(EmailConfirm, key=key, is_confirmed=False)
    email_confirm.is_confirmed = True
    email_confirm.save()
    return login_and_redirect_next(request, email_confirm.user)


def profile_detail(request):
    return render(request, 'profile_detail.html')