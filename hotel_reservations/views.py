from django.shortcuts import render, get_object_or_404
# from . import models
from .models import Country, Hotel, Room


def index(request):
    countries = Country.objects.all()
    hotels = Hotel.objects.all()
    rooms = Hotel.objects.all()
    context = {
        'countries': countries,
        'hotels': hotels,
        'rooms': rooms
    }
    return render(request, template_name='hotel_reservations/index.html', context=context)


def get_country(request, country):
    selected_country = get_object_or_404(Country, country_name=country)
    hotels = Hotel.objects.filter(country=selected_country)
    context = {
        'hotels': hotels,
        'country': selected_country
    }
    return render(request, template_name='hotel_reservations/hotel_list.html', context=context)


def get_room(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    rooms = Room.objects.filter(hotel=hotel)

    room_type_translation = {
        'single': 'Одиночные',
        'double': 'Двухместные',
        'triple': 'Трёхместные',
        'quadruple': 'Четырёхместные'
    }

    room_types = {
        'Одиночные': [],
        'Двухместные': [],
        'Трёхместные': [],
        'Четырёхместные': []
    }

    for room in rooms:
        translated_type = room_type_translation.get(room.room_type, 'Unknown')
        if translated_type not in room_types:
            room_types[translated_type] = []
        room_types[translated_type].append(room)

    context = {
        'hotel': hotel,
        'room_types': room_types
    }
    return render(request, template_name='hotel_reservations/room_list.html', context=context)
