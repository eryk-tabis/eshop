from eshop.celery import app
from django.core.mail import send_mail
from .models import User
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.conf import settings


@app.task
def user_created(user_id):
    """
    Task to send an e-mail notification when a user is succesfully created.
    """
    user = User.objects.get(id=user_id)
    subject = f'Thank you for creating account'
    message = f'Dear {user.username}, \n\n'\
              f'Thank you for creating account in simontabis.com'\

    mail_sent = send_mail(subject, message, 'simontabistest@gmail.com', [user.email])
    return mail_sent


@app.task
def password_change_requested(email):
    """
    Task to send e-mail with link to changing password page
    """
    user = User.objects.get(email=email)
    subject = 'Password Reset Requested'
    email_template_name = 'user/password_reset_email.txt'
    c = {
        "email": user.email,
        'domain': settings.SITE_URL,
        'site_name': 'Website',
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "user": user,
        'token': default_token_generator.make_token(user),
        'protocol': 'http'}
    email = render_to_string(email_template_name, c)
    mail_sent = send_mail(subject, email, 'simontabistest@gmail.com', [user.email])
    return mail_sent
