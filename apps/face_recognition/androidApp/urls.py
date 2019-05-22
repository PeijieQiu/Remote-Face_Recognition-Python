from django.urls import path
from androidApp import views

urlpatterns = [
    path('index/', views.index),
    path('image_upload_handler/', views.image_upload_handler)
]
