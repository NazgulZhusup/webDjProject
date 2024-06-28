from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reviews_home'),
    path('add/', views.create_review, name='new_review'),
]
