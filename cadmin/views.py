from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse_lazy ,reverse
from .forms import PersonalDetailForm, AddressDetailForm, BankDetailForm , LoanApplicationForm
from app.models import PersonalDetails, AddressDetails, BankDetails , LoanApplication
from django.contrib import messages
from users.models import User 
from .decorator import check_admin


# Create your views here.
@check_admin
def dashboardBase(request):
    
    users = User.objects.all()
    loan_applications = LoanApplication.objects.all()
    return render(request,"adminDashboard/dashboard.html",{"users":users, "loan_applications":loan_applications})

@check_admin
def pendingApplications(request):
    loanApplications = LoanApplication.objects.filter(status="pending")
    return render(request,"adminDashboard/pending.html",{"loanApplications":loanApplications})

    
@check_admin
def rejectedApplication(request):
    loanApplications = LoanApplication.objects.filter(status="rejected")
    return render(request,"adminDashboard/rejected.html",{"loanApplications":loanApplications})

@check_admin
def approvedApplication(request):
    loanApplications = LoanApplication.objects.filter(status="approved")
    return render(request,"adminDashboard/approved.html",{"loanApplications":loanApplications})

@check_admin
def detail_view(request, id):
    user = LoanApplication.objects.get(id=id).user
    personal_details = PersonalDetails.objects.filter(user=user).first()
    address_details = AddressDetails.objects.filter(user=user).first()
    bank_details = BankDetails.objects.filter(user=user).first()
    loan_application = LoanApplication.objects.get(id=id)

    if request.method == 'POST':
        personal_form = PersonalDetailForm(request.POST, instance=personal_details)
        address_form = AddressDetailForm(request.POST, instance=address_details)
        bank_form = BankDetailForm(request.POST, instance=bank_details)

        if personal_form.is_valid():
            personal_form.save()
            messages.success(request, "Successfully Added Remark for Personal Details")
        if address_form.is_valid():
            address_form.save()
            messages.success(request, "Successfully Added Remark for Address Details")
        if bank_form.is_valid():
            bank_form.save()
            messages.success(request, "Successfully Added Remark for Bank Details")
        
        
        if request.POST.get('approved_amt'):
            loan_application.approved_amt = int(request.POST['approved_amt'])
            loan_application.status = "approved"
            loan_application.save()
            messages.success(request, "Approved Loan Application")

    personal_form = PersonalDetailForm(instance=personal_details)
    address_form = AddressDetailForm(instance=address_details)
    bank_form = BankDetailForm(instance=bank_details)

    loan_applications = LoanApplication.objects.filter(user=user).order_by('-created_at')

    return render(request, "adminDashboard/detail_views.html", {
                            'loan_applications':loan_applications,
                            'personal_form':personal_form,
                            'address_form':address_form,
                            'bank_form':bank_form,
                        })

@check_admin
def reject_application(request, id):
    loan_application = LoanApplication.objects.get(id=id)
    loan_application.status = "rejected"
    loan_application.save()
    messages.success(request, "Application Rejected Successfully")
    return redirect('dbb')