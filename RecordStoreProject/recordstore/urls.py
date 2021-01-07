from django.urls import path
from . import views

app_name = 'recordstore'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('records/', views.records, name='records'),
    path('records/<int:id>/', views.record, name='record'),
    path('record/edit/<int:id>/', views.edit, name='edit'),
    path('record/new/', views.new, name='new'),
    path('record/wishlist/', views.wishlist, name='wishlist'),
    path('record/add_wish/<int:id>', views.add_wish, name='add_wish'),
    path('record/delete/<int:id>', views.delete, name='delete')
]
