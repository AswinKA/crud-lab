from django.urls import path
from .views import dashboard, add_item, edit_item, delete_item

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add/', add_item, name='add_item'),
    path('edit/<int:id>/', edit_item, name='edit_item'),
    path('delete/<int:id>/', delete_item, name='delete_item'),
]
