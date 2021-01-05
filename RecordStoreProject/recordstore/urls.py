from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='recordstore.index'),
    path('hello/', views.hello, name='recordstore.hello')
]
