from django.urls import path
from . import views

urlpatterns = [
    # Example URL pattern
    path('used-stock/', views.used_stock, name='used-stock'),
]
