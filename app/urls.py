from django.urls import path
from .views import (register_user, 
                    login_user, 
                    password_reset, 
                    address, 
                    register_com,
                    bankDetail, 
                    forgot_password, 
                    logout_user,
                    index,
                    generate_otp)

urlpatterns = [
    path("", index, name="home"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("forgotpassword/", forgot_password, name="forgotpassword"),
    path("changepassword/<str:tk>/<str:p>/",password_reset, name="changepassword"),
    path("address/",address, name="address"),
    path("bank/",bankDetail, name="bank"),
    path("generateotp/", generate_otp, name="generateotp"),
    path("registercom/", register_com, name="registerCom"),
]