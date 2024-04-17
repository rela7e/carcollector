from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_accolade/', views.add_accolade, name='add_accolade'),
    path('cars/<int:car_id>/assoc_driver/<int:driver_id>/', views.assoc_driver, name='assoc_driver'),
    path('cars/<int:car_id>/unassoc_driver/<int:driver_id>/', views.unassoc_driver, name='unassoc_driver'),
    path('drivers/', views.DriverList.as_view(), name='drivers_index'),
    path('drivers/<int:pk>/', views.DriverDetail.as_view(), name='drivers_detail'),
    path('drivers/create/', views.DriverCreate.as_view(), name='drivers_create'),
    path('drivers/<int:pk>/update/', views.DriverUpdate.as_view(), name='drivers_update'),
    path('drivers/<int:pk>/delete/', views.DriverDelete.as_view(), name='drivers_delete'),
]
