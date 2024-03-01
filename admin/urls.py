from django.urls import path
from .views import dashboardBase , other
urlpatterns = [
    path("", dashboardBase, name="dbb"),
    path("other" ,other, name="other"),
    
    
]
