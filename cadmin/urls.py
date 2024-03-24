from django.urls import path
from .views import dashboardBase , detail_view, pendingApplications, rejectedApplication, approvedApplication, reject_application

urlpatterns = [
    path("", dashboardBase, name="dbb"),
    path("pending", pendingApplications,name="pendingApplcation"),
    path("rejected", rejectedApplication, name="rejectedApplication"),
    path("approved", approvedApplication, name="approvedApplication" ),
    path("<int:id>",detail_view,name="details"),
    path("reject/<int:id>",reject_application,name="reject-loan"),
]
