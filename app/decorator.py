from django.shortcuts import redirect
from .models import PersonalDetails , AddressDetails, BankDetails

def first_time_register(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        personal_detail = PersonalDetails.objects.filter(user=user.id).first()
        address_detail = AddressDetails.objects.filter(user=user.id).first()
        bank_detail = BankDetails.objects.filter(user=user.id).first()

        if not personal_detail.first_time and address_detail and bank_detail:
            if view_func.__name__ == 'dashboard':
                return view_func(request, *args, **kwargs)
            return redirect('registerCom')
        elif not personal_detail.first_time:
            if view_func.__name__ == "register_com":
                return view_func(request, *args, **kwargs)
            return redirect('registerCom')
        elif not address_detail:
            if view_func.__name__ == "address":
                return view_func(request, *args, **kwargs)
            return redirect('address')
        elif not bank_detail:
            if view_func.__name__ == "bankDetail":
                return view_func(request, *args, **kwargs)
            return redirect('bank')

        return view_func(request, *args, **kwargs)
    return wrapper_func

