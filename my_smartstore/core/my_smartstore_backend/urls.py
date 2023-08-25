from django.urls import path

from my_smartstore_backend.views import request_otp, verify_otp, create_account, login, userdata, categories, slides

urlpatterns = [
    path('request_otp/', request_otp),
    path('verify_otp/', verify_otp),
    path('create_account/', create_account),
    path('login/', login),
    path('userdata/', userdata,),
    path('categories/', categories,),
    path('slides/', slides,),
]
