from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
# Create your views here.


def get_sign_zodiac(request, sign_zodiac):
    if sign_zodiac == 'leo':
        return HttpResponse("Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)")
    elif sign_zodiac == 'scorpio':
        return HttpResponse("Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)")
    elif sign_zodiac == 'aries':
        return HttpResponse("Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)")
    elif sign_zodiac == 'taurus':
        return HttpResponse("Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)")
    elif sign_zodiac == 'virgo':
        return HttpResponse("Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)")
    else:
        return HttpResponseForbidden(f"Не известный знак зодиака: {sign_zodiac}")


