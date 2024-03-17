from django.urls import path
from .views import dashboardBase , detail_view , personal_remark , address_remark , bank_remark , pendingApplications, rejectedApplication, approvedApplication , loanApplicationNego
urlpatterns = [
    path("", dashboardBase, name="dbb"),
    path("pending", pendingApplications,name="pendingApplcation"),
    path("rejected", rejectedApplication, name="rejectedApplication"),
    path("approved", approvedApplication, name="approvedApplication" ),
    path("nego/<int:id>",loanApplicationNego,name="loanApplicationNego" ),
    path("<int:id>",detail_view,name="details"),
    path("personremark/<int:id>/<int:lid>", personal_remark,name="personRemark"),
    path("addressremark/<int:id>/<int:lid>",address_remark,name="addressRemark"),
    path("bankremark/<int:id>/<int:lid>", bank_remark, name="bankRemark"),
    
    
]
