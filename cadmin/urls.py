from django.urls import path
from .views import dashboardBase , detail_view , personal_remark , address_remark , bank_remark 
app_name = "cadmin"
urlpatterns = [
    path("", dashboardBase, name="dbb"),
    path("<int:id>",detail_view,name="details"),
    path("personremark/<int:id>", personal_remark,name="personRemark"),
    path("addressremark/<int:id>",address_remark,name="addressRemark"),
    path("bankremark/<int:id>", bank_remark, name="bankRemark"),
    
    
]
