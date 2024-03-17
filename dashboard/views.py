from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PersonalDetailForm, AddressDetailForm, BankDetailForm, LoanApplicationForm
from app.models import PersonalDetails, AddressDetails, BankDetails, LoanApplication
from django.contrib import messages

# Create your views here.

@login_required(login_url="login")
def dashboard(request):
    user = request.user
    personal_details = PersonalDetails.objects.filter(user=user.id).first()
    address_details = AddressDetails.objects.filter(user=user.id).first()
    bank_details = BankDetails.objects.filter(user=user.id).first()

    personal_form = PersonalDetailForm(instance=personal_details)
    address_form = AddressDetailForm(instance=address_details)
    bank_form = BankDetailForm(instance=bank_details)

    return render(request, "dashboard/home.html", {'personal_form':personal_form,
                                                    'address_form':address_form,
                                                    'bank_form':bank_form,
                                                    'personal_details':personal_details,
                                                    'address_details':address_details,
                                                    'bank_details':bank_details})

@login_required(login_url="login")
def update_personal_details(request):
    if request.method == "POST":
        user = request.user
        personal_details = PersonalDetails.objects.filter(user=user.id).first()
        personal_form = PersonalDetailForm(request.POST, instance=personal_details)
        if personal_form.is_valid():
            personal_details = personal_form.save(commit=False)
            personal_details.user = user
            personal_form.save()
            messages.success(request, "Personal Details Updated Successfully")
        else:
            messages.error(request, "Error Updating Personal Details")
        return redirect('dashboard-home')

@login_required(login_url="login")
def update_address_details(request):
    if request.method == "POST":
        user = request.user
        address_details = AddressDetails.objects.filter(user=user.id).first()
        address_form = AddressDetailForm(request.POST, request.FILES, instance=address_details)
        if address_form.is_valid():
            address_details = address_form.save(commit=False)
            address_details.user = user
            address_form.save()
            messages.success(request, "Address Details Updated Successfully")
        else:
            print(address_form.errors)
            messages.error(request, "Error Updating Address Details")
        return redirect('dashboard-home')

@login_required(login_url="login")
def update_bank_details(request):
    if request.method == "POST":
        user = request.user
        bank_details = BankDetails.objects.filter(user=user.id).first()
        bank_form = BankDetailForm(request.POST, request.FILES, instance=bank_details)
        if bank_form.is_valid():
            bank_details = bank_form.save(commit=False)
            bank_details.user = user
            bank_form.save()
            messages.success(request, "Bank Details Updated Successfully")
        else:
            messages.error(request, "Error Updating Bank Details")
        return redirect('dashboard-home')

@login_required(login_url="login")

def application(request):
    loan_applications = LoanApplication.objects.filter(user=request.user.id).order_by('-created_at')

    application_form = LoanApplicationForm()
    if request.method == "POST":
        user = request.user
        application_form = LoanApplicationForm(request.POST)
        if application_form.is_valid():
            application = application_form.save(commit=False)
            application.user = user
            application_form.save()
            messages.success(request, "Application Submitted Successfully")
            return redirect('dashboard-application')
        else:
            messages.error(request, "Error Submitting Application")
    return render(request, "dashboard/application.html", {'application_form':application_form, 'loan_applications':loan_applications})

@login_required(login_url="login")
def delete_application(request, id):
    loan_application = LoanApplication.objects.get(id=id)
    loan_application.delete()
    messages.success(request, "Application Deleted Successfully")
    return redirect('dashboard-application')

@login_required(login_url="login")
def offers(request):
    offers = LoanApplication.objects.filter(status='approved').order_by('-created_at')
    context = {
        'offers': offers
    }
    return render(request, "dashboard/offers.html", context)