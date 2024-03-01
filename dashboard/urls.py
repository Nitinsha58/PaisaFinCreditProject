from django.urls import path
from .views import dashboard, update_personal_details, update_address_details, update_bank_details

urlpatterns = [
    path("", dashboard, name="dashboard-home"),
    path("update-personal-details/", update_personal_details, name="update-personal-details"),
    path("update-address-details/", update_address_details, name="update-address-details"),
    path("update-bank-details/", update_bank_details, name="update-bank-details"),
]