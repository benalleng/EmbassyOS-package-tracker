from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('packages/', views.package_index, name='package_index'),
    path('accounts/signup/', views.signup, name='signup'),
]