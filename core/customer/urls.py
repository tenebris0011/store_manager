from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'customer'
urlpatterns = [
    path('preorders', views.PreOrders, name='preorders'),
    path('store_credit', views.StoreCredit, name='store_credit'),
]