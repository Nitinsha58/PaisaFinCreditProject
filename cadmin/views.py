from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse_lazy ,reverse
from .forms import PersonalDetailForm, AddressDetailForm, BankDetailForm , LoanApplicationForm
from app.models import PersonalDetails, AddressDetails, BankDetails , LoanApplication
from django.contrib import messages
from users.models import User 
# Create your views here.
def dashboardBase(request):
    
    users = User.objects.all()
    loanApplications = LoanApplication.objects.all()

    
    return render(request,"adminDashboard/dashboard.html",{"users":users, "loanApplications":loanApplications})

def pendingApplications(request):
    loanApplications = LoanApplication.objects.filter(status="pending")
    return render(request,"adminDashboard/pending.html",{"loanApplications":loanApplications})

def rejectedApplication(request):
    loanApplications = LoanApplication.objects.filter(status="rejected")
    return render(request,"adminDashboard/rejected.html",{"loanApplications":loanApplications})

def approvedApplication(request):
    loanApplications = LoanApplication.objects.filter(status="approved")
    return render(request,"adminDashboard/approved.html",{"loanApplications":loanApplications})

def detail_view(request, id):
    loanApplication = LoanApplication.objects.get(id=id)
    
    userid = loanApplication.user
    user = User.objects.get(id=userid.id)
    loadForm_id = id 

    personal_details = PersonalDetails.objects.filter(user=userid).first()
    address_details = AddressDetails.objects.filter(user=userid).first()
    bank_details = BankDetails.objects.filter(user=userid).first()
    load_application_details = LoanApplication.objects.filter(user=userid).first()
    
    personal_form = PersonalDetailForm(instance=personal_details)
    address_form = AddressDetailForm(instance=address_details)
    bank_form = BankDetailForm(instance=bank_details)
    load_application_form = LoanApplicationForm(instance=load_application_details)

    
   
    if request.method == 'POST':
        
        personal_form = PersonalDetailForm(request.POST)
        address_form = AddressDetailForm(request.POST)
        bank_form = BankDetailForm(request.POST)

        if personal_form.is_valid() and  address_form.is_valid() and bank_form.is_valid():
            
            personal_form.save()
            address_form.save()
            bank_form.save()
        

    
    return render(request, "adminDashboard/detail_views.html", {'personal_form':personal_form,
                                                    'address_form':address_form,
                                                    'bank_form':bank_form,
                                                    'personal_details':personal_details,
                                                    'address_details':address_details,
                                                    'bank_details':bank_details,
                                                    'user':user,
                                                    'loanApplication':loanApplication ,
                                                    'loanApplicationForm':load_application_form,
                                                    'loadForm_id':loadForm_id})

def loanApplicationNego(request, id):
    if request.method == "POST":
        loanApplication = LoanApplication.objects.get(id = id)
        loanApplication_form = LoanApplicationForm(request.POST)
        if loanApplication_form.is_valid():
            approved_amount = loanApplication_form.cleaned_data['approved_amt']
            loanApplication.approved_amt = approved_amount
            loanApplication.save()
            messages.success(request,"Successfully Added")

        else: 
            
            messages.error(request,"Error ")
    return redirect('cadmin:dbb')



def personal_remark(request,id,lid):
    if request.method == "POST":
        user = User.objects.get(id=id)
        personal_form = PersonalDetailForm(request.POST)
        
        if personal_form.is_valid():
            personal_details = PersonalDetails.objects.get(user=user)
            personal_details.remark = personal_form.cleaned_data['remark']
            personal_details.save()
            
            messages.success(request,"Personal Remark Added")
            return redirect(reverse('cadmin:details', kwargs={'id': lid}))

        else: 
            
            messages.error(request,"Error ")

    return redirect('cadmin:dbb')
    


def address_remark(request,id,lid):
    
    if request.method == "POST":
        user = User.objects.get(id=id)
        address_form = AddressDetailForm(request.POST)
        
        
        if address_form.is_valid():
            address_details  = AddressDetails.objects.get(user=user)
            address_details.remark = address_form.cleaned_data['remark']
            
            address_details.save()
            messages.success(request,"address  Remark Added")
            return redirect(reverse('cadmin:details', kwargs={'id': lid}))
        else:
            messages.error(request,"Error ")
            
           
    return redirect('cadmin:dbb')

    


def bank_remark(request, id,lid):
    
    if request.method =="POST":
        print("method is post ")
        user = User.objects.get(id=id)
        bank_form = BankDetailForm(request.POST)

        if bank_form.is_valid():
            bank_details= BankDetails.objects.get(user=user)
            bank_details.remark = bank_form.cleaned_data['remark']
            bank_details.save()
            messages.success(request,"bank  Remark Added")
            return redirect(reverse('cadmin:details', kwargs={'id': lid}))
        
    
    return redirect('cadmin:dbb')
    
            


    





