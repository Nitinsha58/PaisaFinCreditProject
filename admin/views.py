from django.shortcuts import render

# Create your views here.
def dashboardBase(request):
    return render(request,"admin/dashboard.html",{} )


def other(request):
    return render(request,"admin/offers.html",{} )
