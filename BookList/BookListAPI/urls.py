from django.urls import path
from .views import MenuItemsView, MenuItemDetailView

urlpatterns = [
    path('menu-items/', MenuItemsView.as_view(), name='menu-items-list'),
    path('menu-items/<int:pk>/', MenuItemDetailView.as_view(), name='menu-item-detail'),
]
