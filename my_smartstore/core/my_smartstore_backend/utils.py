import datetime
import uuid
from random import randint

from rest_framework.permissions import BasePermission
from rest_framework.response import Response

from my_smartstore_backend.models import Otp, Token


def send_otp(phone):

    otp = randint(100000,999999)
    validity = datetime.datetime.now()+datetime.timedelta(minutes=10)
    Otp.objects.update_or_create(phone = phone,defaults={"otp":otp,"verified":False,"validity":validity})

    return Response ('otp sent successfully')


def new_token():
    token=uuid.uuid1().hex
    return token

def token_response(user):
    token = new_token()
    Token.objects.create(token=token,user=user)
    return Response('Token '+token)

# def send_password_reset_email(user):
#     token = new_token()
#     exp_time=datetime.datetime.now() + datetime.timedelta(minutes=10)
#     PasswordResetToken.objects.update_or_create(user=user,defaults={'user':user,'token':token,'validity':exp_time})


class IsAuthenticatedUser(BasePermission):
    message = "unauthenticated_user"

    def has_permission(self, request, view):
        return bool(request.user)

