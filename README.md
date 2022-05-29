## Eshop
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Overall setup](#overall-setup)
* [Paypall setup](#paypal-setup)
* [Celery setup](#celery-setup)

## General info
This project is a ecommerce shop which sells training programs. App have funcionalities as:
* Shop cart
* Password reset
* Paypall gateway implementation
* Automative sending emails with invoice

## Technologies
Project is created with:
 * Django
* Bootstrap
* Celery
* Django-paypal
* Pillow
* WeasyPrint
## Overall setup
To run this project, you need to install packages with `pip install requirements.txt`. 
Also you need to fill `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `PAYPAL_RECEIVER_EMAIL` in `settings.py` file.
Default superusser username and password is `root admin`
For launching project you need to run `python manage.py runserver` in project`s dictionary.
## Paypal setup
Paypal will only work if application isn`t on localhost so you need to launch it in the internet. You can use ngrok for it
## Celery setup
You need to run this : `celery -A eshop  worker --loglevel=info --concurrency 1 -P solo`in order to do tasks
You can also run this: `celery flower` to see tasks 
