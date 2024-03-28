from . import views
from django.urls import path

urlpatterns=[
    path('show_products/', views.show_products),
    path('show_products/<int:pk>/', views.show_product),
    path('show_categories/', views.show_categories),
    path('show_categories/<int:pk>/', views.show_category),
    path('show_categories/<int:pk>/products/', views.show_list_of_products_by_category),
]