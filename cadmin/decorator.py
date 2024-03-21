from django.shortcuts import redirect
from functools import wraps
def check_admin(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            print("user is admin ")
            return func(request, *args, **kwargs)
        else:
           
            return redirect("login")
    return wrapper