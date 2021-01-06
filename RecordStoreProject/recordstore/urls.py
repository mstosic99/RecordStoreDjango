from django.urls import path
from . import views

app_name = 'recordstore'
urlpatterns = [
    path('', views.index, name='recordstore.index'),
    path('records/', views.records, name='records'),
    path('record/<int:id>', views.record, name='record'),
    path('record/edit/<int:id>', views.edit, name='record'),
    path('record/new', views.new, name='record'),
]
