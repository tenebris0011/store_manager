from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'inventory'
urlpatterns = [
    path('new', views.NewInventory, name='new'),
    path('singles', views.SinglesInventory, name='singles'),
]