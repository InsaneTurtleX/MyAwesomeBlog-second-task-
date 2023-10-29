from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='about'),
    path('<slug:category_slug>', views.home, name='products_by_category'),
    ]