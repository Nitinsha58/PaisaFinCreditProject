from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import UserForm, PersonalDetailForm , AddressDetailForm , BankDetailForm , PersonalDetailComForm
from users.models import User 
from .models import PersonalDetails , BankDetails , AddressDetails
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'app/index.html')

def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        personal_detail_form = PersonalDetailForm(request.POST)

        if user_form.is_valid() and personal_detail_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            my_user = User.objects.get(phone=user.phone)

            if my_user is None:
                    messages.error(request, "Error Creating Account, please try again later.")
                    return redirect('register')

            personal_detail = personal_detail_form.save(commit=False)
            personal_detail.user = my_user
            personal_detail.save()
            messages.success(request, "Account created successfully")
            return redirect('login')
    else:
        user_form = UserForm()
        personal_detail_form = PersonalDetailForm()
    return render(request, 'app/registration/register.html', {'user_form': user_form, 'personal_detail_form': personal_detail_form})

@login_required(login_url='login')
def register_com(request):
    user = request.user
    user_detail = PersonalDetails.objects.filter(user=user.id).first() 
    personal_details_form = PersonalDetailComForm(request.POST or None, instance=user_detail)
    
    if request.method == 'POST':
        if personal_details_form.is_valid():
            personal_detail = personal_details_form.save(commit=False)
            personal_detail.user = user
            
            personal_detail.save()
            messages.success(request, "Personal details saved successfully")
            return redirect('address')

    context = {'personal_details_form': personal_details_form}
    return render(request, 'app/registration/registerCom.html', context)

def login_user(request):
    error = None
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if phone and password:
            user = authenticate(phone=phone, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            error = "Incorrect phone number or password "
        else:
            error = "Phone or password cannot be empty"

    return render(request, 'app/registration/login.html', {'error': error})

def forgot_password(request):
    
    return render(request, 'app/registration/forgotPassword.html')

def generate_otp(request, phone):
    otp = ''.join([str(random.randrange(0,10)) for i in range(6)])
    if 15 >= phone.isdigit() and len(phone) >= 10:
        user = User.objects.filter(phone=phone).first()

        if user:
            user.otp = otp
            user.save()
            return JsonResponse({'message': 'OTP sent to your phone number'})
    return JsonResponse({'error': 'Invalid phone number'})

@login_required(login_url='login')
def logout_user(request):
    messages.info(request, "Logged out successfully")
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def changePassword(request):
    return render(request, 'app/registration/changePassword.html')

@login_required(login_url='login')
def address(request):
    user = request.user
    address_details = AddressDetails.objects.filter(user=user.id).first()
    address_form = AddressDetailForm(request.POST or None, instance=address_details)

    if request.method == "POST":
        address_form = AddressDetailForm(request.POST, request.FILES, instance=address_details)
        if address_form.is_valid(): 
            address_instance = address_form.save(commit=False)
            address_instance.user = user
            address_instance.save()

            messages.success(request, "Address details added successfully")
            return redirect('bank')  

    context = {"address_form": address_form, 'address_details': address_details}
    return render(request, 'app/registration/address.html', context)  

@login_required(login_url='login')
def bankDetail(request):
    user = request.user
    bank_details = BankDetails.objects.filter(user=user.id).first()
    bank_form = BankDetailForm(request.POST or None, instance=bank_details)
    if request.method == "POST":
        bank_form = BankDetailForm(request.POST, request.FILES, instance=bank_details)
        if bank_form.is_valid():
            bank_instance = bank_form.save(commit=False)
            bank_instance.user = user
            bank_instance.save()

            messages.success(request, "Bank details added successfully")
            return redirect('dashboard-home')

    context = { "bank_form": bank_form, 'bank_details': bank_details}
    return render(request, 'app/registration/bank.html', context)
