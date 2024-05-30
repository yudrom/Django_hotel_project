from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Country, Hotel, Room, Reservation
from .decorators import login_required_with_message


def index(request):
    countries = Country.objects.all()
    context = {
        'countries': countries,
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


@login_required_with_message
def calculate_total_price(request):
    if request.method == 'POST':
        selected_rooms = request.POST.getlist('rooms')
        days = int(request.POST.get('days', 0))
        total_price = 0

        reservations = []

        for room_id in selected_rooms:
            if room_id:
                room = get_object_or_404(Room, pk=room_id)
                room_price = room.price_per_night * days
                total_price += room_price

                reservation = Reservation.objects.create(
                    user=request.user,
                    hotel=room.hotel,
                    room=room,
                    duration=days,
                    total_price=room_price
                )

                reservations.append(reservation)

        context = {
            'total_price': total_price,
            'reservation': reservations
        }

        return render(request, template_name='hotel_reservations/success_payment.html', context=context)

    return HttpResponseRedirect('/')
