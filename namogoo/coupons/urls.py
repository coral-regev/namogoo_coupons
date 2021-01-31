from django.urls import path
from . import views

urlpatterns = [
    path('GetCoupon/', views.get_coupon, name='get_coupon'),
    path('ReturnCoupon/', views.return_coupon, name='return_coupon'),
]