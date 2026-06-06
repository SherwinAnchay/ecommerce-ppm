from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_list, name='order_list'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/product/new/', views.product_create, name='product_create'),
    path('manager/product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('manager/product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    ]