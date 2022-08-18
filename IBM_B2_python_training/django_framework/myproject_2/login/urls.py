from django.urls import path
from . import views
urlpatterns = [
    path('', views.myloginpage),
    path('registeruser/', views.myregisteruserpage),
    path('addnewuser/', views.myaddnewuserpage),
path('validate/', views.myvalidatepage),
]
