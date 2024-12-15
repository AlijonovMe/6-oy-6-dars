from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('brands/<int:brands_id>/', brandDetail, name='brands_detail'),
    path('cars/<int:cars_id>/', carDetail, name='cars_detail')
]