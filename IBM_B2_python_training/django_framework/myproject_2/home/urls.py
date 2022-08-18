from django.urls import path
from . import views
urlpatterns = [
    path('', views.myindexpage),
    path('about/', views.myaboutpage),
]
