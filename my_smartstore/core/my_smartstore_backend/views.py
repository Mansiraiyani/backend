import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from my_smartstore_backend.models import User, Otp, Category, Slide
from my_smartstore_backend.serializers import UserSerializer, CategorySerializre, SlideSerializre
from my_smartstore_backend.utils import send_otp, token_response, IsAuthenticatedUser


# Create your views here.

@api_view(['POST'])
def request_otp(request):
    email = request.data.get('email')
    phone = request.data.get('phone')
    if phone and email:
        if User.objects.filter(email=email).exists():
            return Response('email already exists', status=400)
        if User.objects.filter(phone=phone).exists():
            return Response('phone already exists', status=400)
        return send_otp(phone)
    else:
        return Response('Data missing', status=400)


@api_view(['POST'])
def verify_otp(request):
    otp = request.data.get('otp')
    phone = request.data.get('phone')

    otp_obj = get_object_or_404(Otp, phone=phone, verified=False)
    if otp_obj.validity.replace(tzinfo=None) > datetime.datetime.utcnow():
        if otp_obj.otp == int(otp):
            otp_obj.verified = True
            otp_obj.save()
            return Response('otp verified successfully')
        else:
            return Response("incorrect otp", status=400)
    else:
        return Response("expired otp")


@api_view(['POST'])
def create_account(request):
    email = request.data.get('email')
    phone = request.data.get('phone')
    password = request.data.get('password')
    fullname = request.data.get('fullname')
    if phone and email and password and fullname:
        otp_obj = get_object_or_404(Otp, phone=phone, verified=True)
        otp_obj.delete()
        user = User()
        user.email = email
        user.phone = phone
        user.fullname = fullname
        user.password = make_password(password)
        user.save()
        return token_response(user)
        # User.objects.create(email=email, fullname=fullname, phone=phone, password=make_password(password))
        # return Response("Account created successfully!")
    else:
        return Response("Data missing", status=400)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    phone = request.data.get('phone')
    password = request.data.get('password')
    if email:
        user = get_object_or_404(User, email=email)
    elif phone:
        user = get_object_or_404(User, phone=phone)
    else:
        return Response("data missing", status=400)

    if check_password(password, user.password):
        return token_response(user)
    else:
        return Response('incorrect password!')

@api_view(['GET'])
@permission_classes([IsAuthenticatedUser])
def userdata(request):
    user = request.user
    data = UserSerializer(user,many=False).data
    return Response(data)
    return Response()

@api_view(['GET'])
def categories(request):
    list = Category.objects.all().order_by('position')
    data  = CategorySerializre(list,many=True).data
    return Response(data)

@api_view(['GET'])
def slides(request):
    list = Slide.objects.all().order_by('position')
    data  = SlideSerializre(list,many=True).data
    return Response(data)








