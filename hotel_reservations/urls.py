from django.urls import path
from hotel_reservations import views


urlpatterns = [
    path('', views.index, name='main'),
    path('country-choice/<str:country>/', views.get_country, name='country'),
    path('rooms/<int:hotel_id>/', views.get_room, name='rooms'),
    path('success_payment/', views.calculate_total_price, name='calculate_total_price')
]