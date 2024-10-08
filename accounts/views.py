import os

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import get_random_string
# Create your views here.
from django.urls import reverse
from django.views import View
from .forms import UserLoginForm, UserRegisterForm, UserVerificationCodeForm, EditProfileForm
import ghasedakpack
from .forms import EditProfileUserForm
from django.contrib import messages
from random import randint
from uuid import uuid4
from .models import RegisterUserOtp, User

sms = ghasedakpack.Ghasedak("5a36e1045f08fd777bd67da30f8702863765d5f8ceb420324c7da377aafd5707")


class UserLoginView(View):
    def get(self, request):

        form = UserLoginForm()
        return render(request, "acounts/login.html", {"form": form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data["phone"], password=data["password"])
            if user is not None:
                login(request, user)
                messages.success(request,"login successfully")
                return redirect("/")
            else:
                form.add_error("phone", "کاربر با این شماره تماس و رمز عبو پیدا نشد.")

        return render(request, "acounts/login.html", {"form": form})


def user_logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logout successfully")
        return redirect("/")

    messages.error(request,"not logout ")
    return redirect("/")


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()

        return render(request, "acounts/register.html", {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            randomcode = randint(1000, 9999)
            print(data["phone"], randomcode)

            token = get_random_string(length=150)

            sms.verification({'receptor': data["phone"], 'type': '1', 'template': 'randjavad', 'param1': randomcode})
            RegisterUserOtp.objects.create(phone=data["phone"], code=randomcode, token=token)
            return redirect(f"/acounts/register/code/?phone={token}")

        return render(request, "acounts/register.html", {"form": form})


class UserVerificationcodeView(View):
    def get(self, request):
        form = UserVerificationCodeForm()

        return render(request, "acounts/code_register.html", {"form": form})

    def post(self, request):
        token = request.GET.get("phone")
        form = UserVerificationCodeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if RegisterUserOtp.objects.filter(code=data["code"], token=token).exists():
                otp = RegisterUserOtp.objects.get(token=token)
                user = User.objects.create_user(phone=otp.phone)

                phone = user.phone
                login(request, user)
                otp.delete()
                messages.success(request,"confirm code")

                return redirect(f"/acounts/editprofile/?phone={phone}")
            else:
                form.add_error("code", "کد تایید درست نیست")

        return render(request, "acounts/code_register.html", {"form": form})


class UserEditView(View):
    def get(self, request):
        form = EditProfileForm(instance=request.user)

        return render(request, "acounts/edit_profile_register.html", {"form": form})

    def post(self, request):
        phone = request.GET.get("phone")

        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            user = User.objects.get(phone=phone)
            request.user.set_password(request.POST.get("password"))
            request.user.save()
            messages.success(request,"user created")

            return redirect("/acounts/login")

        return render(request, "acounts/edit_profile_register.html", {"form": form})


class UserEditProfileView(View):

    def get(self, request):
        form = EditProfileUserForm(instance=request.user)

        return render(request, "acounts/edit_profile.html", {"form": form})

    def post(self, request):
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            request.user.discription = request.POST.get("discription")
            request.user.email = request.POST.get("email")

            if len(request.FILES) != 0:
                request.user.image = request.FILES["image"]
                request.user.set_password(request.POST.get("password2"))
                request.user.save()

            form.save()

            messages.success(request,"user edited")
            return redirect("/")
        return render(request, "acounts/edit_profile.html", {"form": form})


def delete_user_view(request):
    request.user.delete()
    messages.success(request,"user deleted")

    return redirect("/")
