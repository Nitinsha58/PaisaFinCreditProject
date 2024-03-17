from django.urls import path
from .views import (
    dashboard, 
    update_personal_details, 
    update_address_details, 
    update_bank_details,
    application,
    delete_application,
    offers,
    resendOtp,
    verify_phone
    )


urlpatterns = [
    path("", dashboard, name="dashboard-home"),
    path("update-personal-details/", update_personal_details, name="update-personal-details"),
    path("update-address-details/", update_address_details, name="update-address-details"),
    path("update-bank-details/", update_bank_details, name="update-bank-details"),
    path("application/", application, name="dashboard-application"),
    path("delete-application/<int:id>", delete_application, name="delete-application"),
    path("offers/", offers, name="dashboard-offer"),
    path("verify-phone/", verify_phone, name="verify-phone"),
    path("resend-otp/", resendOtp, name="resend-otp"),
]