
from . import views
from django.urls import path, include

urlpatterns = [
    path('dashboard', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('product/', views.product, name='dashboard-product'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('order/', views.order, name='dashboard-order'),
    path('warehouse/stock/', views.warehouse_stock_view, name='warehouse-stock'),
    path('warehouse/stock/update/', views.used_stock, name='update-stock'),
    path('inventory/', include('inventory.urls')),
]


