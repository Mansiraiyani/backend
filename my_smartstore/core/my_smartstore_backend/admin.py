from django.contrib import admin
from django.contrib.admin import register

from my_smartstore_backend.models import User, Otp, Token


# Register your models here.
@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','fullname','phone','created_at']
    readonly_fields = ['password']
@register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ['phone','otp','validity','verified']

@register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['token','user','created_at']


# @register(PasswordResetToken)
# class PasswordResetTokenAdmin(admin.ModelAdmin):
#     list_display = ['token','user','validity','created_at']
#
