from django.urls import path
from . import views       
    
    
app_name = "main"   
urlpatterns = [
        path("", views.login_request, name ="login"),  #add this
        path("logout", views.logout_request, name= "logout"),
    ]