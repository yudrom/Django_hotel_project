from django.db import models
# from django.contrib.auth.models import User


class Country(models.Model):
    country_name = models.CharField(max_length=150, verbose_name='Страна')
    country_description = models.TextField(verbose_name='Описание страны', blank=True)
    country_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото страны', blank=True, null=True)
    city_name = models.CharField(max_length=150, verbose_name='Город', default='Russia')

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Hotel(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название отеля')
    description = models.TextField(verbose_name='Описание отеля', blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, verbose_name='Страна')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    contacts = models.TextField(verbose_name='Контакты', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Рейтинг')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True, null=True)
    allow_check_in_time = models.TimeField(verbose_name='Доступное время заезда', blank=True, null=True)
    allow_check_out_time = models.TimeField(verbose_name='Доступное время выезда', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
        ordering = ['-rating']


class Room(models.Model):

    ROOM_TYPE_CHOICES = (
        ('single', 'Одиночный'),
        ('double', 'Двухместный'),
        ('triple', 'Трёхместный'),
        ('quadruple', 'Четырёхместный')
    )

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, verbose_name='Отель')
    room_number = models.CharField(max_length=10, verbose_name='Номер комнаты')
    room_type = models.CharField(max_length=100, choices=ROOM_TYPE_CHOICES, verbose_name='Тип комнаты')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за ночь')
    availability = models.BooleanField(default=True, verbose_name='Доступность')

    def __str__(self):
        return f'{self.hotel} - {self.room_number}'

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'
        ordering = ['hotel', 'room_number']


# class Reservation(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Комната')
#     check_in_date = models.DateField(verbose_name='Дата заезда')
#     check_out_date = models.DateField(verbose_name='Дата выезда')
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая стоимость')
#
#     def __str__(self):
#         return f'{self.user.username} - {self.room.room_number} ({self.check_in_date} to {self.check_out_date})'
#
#     class Meta:
#         verbose_name = 'Бронирование'
#         verbose_name_plural = 'Бронирования'
