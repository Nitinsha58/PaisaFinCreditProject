from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse_lazy ,reverse
from .forms import PersonalDetailForm, AddressDetailForm, BankDetailForm
from app.models import PersonalDetails, AddressDetails, BankDetails
from django.contrib import messages
from users.models import User 
# Create your views here.
def dashboardBase(request):
    
    users = User.objects.all()
    return render(request,"adminDashboard/dashboard.html",{"users":users})



def detail_view(request, id):
    
    personal_details = PersonalDetails.objects.filter(user=id).first()
    address_details = AddressDetails.objects.filter(user=id).first()
    bank_details = BankDetails.objects.filter(user=id).first()

    personal_form = PersonalDetailForm(instance=personal_details)
    address_form = AddressDetailForm(instance=address_details)
    bank_form = BankDetailForm(instance=bank_details)
    

    user = User.objects.get(id=id)
   
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
                                                    'user':user})



def personal_remark(request,id):
    if request.method == "POST":
        user = User.objects.get(id=id)
        personal_form = PersonalDetailForm(request.POST)
        
        if personal_form.is_valid():
            personal_details = PersonalDetails.objects.get(user=user)
            personal_details.remark = personal_form.cleaned_data['remark']
            personal_details.save()
            
            messages.success(request,"Personal Remark Added")

        else: 
            
            messages.error(request,"Error ")

    return redirect('cadmin:dbb')
    
# def address_remark(request,id):
#     print("Working")
#     if request.method == "POST":
        
#         user = User.objects.get(id=id)
#         address_form = AddressDetailForm(request.POST)
#         print(address_form.is_valid())
#         if address_form.is_valid():
#             address_details  = AddressDetails.objects.get(user=user)
#             address_details.remark = address_form.cleaned_data['remark']
#             print(address_details.remark)
#             address_details.save()
#             messages.success(request,"address  Remark Added")
#         else:
#             messages.error(request,"Error ")

#     return redirect('cadmin:dbb')

def address_remark(request,id):
    if request.method == "POST":
        user = User.objects.get(id=id)
        address_form = AddressDetailForm(request.POST)
        print(address_form.is_valid())
        if address_form.is_valid():
            address_details  = AddressDetails.objects.get(user=user)
            address_details.remark = address_form.cleaned_data['remark']
            print(address_details.remark)
            address_details.save()
            messages.success(request,"address  Remark Added")
        else:
            messages.error(request,"Error ")
    return redirect('cadmin:dbb')

    


def bank_remark(request, id):
    if request.method =="POST":
        user = User.objects.get(id=id)
        bank_form = BankDetailForm(request.POST)

        if bank_form.is_valid():
            bank_details= BankDetails.objects.get(user=user)
            bank_details.remark = bank_form.cleaned_data['remark']
            bank_details.save()
            messages.success(request,"bank  Remark Added")
        else:
            messages.error(request,"Error ")
    return redirect('cadmin:dbb')
    
            
            
    





