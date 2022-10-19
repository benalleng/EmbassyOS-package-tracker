from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('packages/', views.package_index, name='packages_index'),
    path('packages/<int:package_id>', views.package_detail, name='packages_detail'),
    path('packages/create/', views.PackageCreate.as_view(), name='packages_create'),
    path('packages/update/', views.PackageUpdate.as_view(), name='packages_update'),
    path('accounts/signup/', views.signup, name='signup'),
]