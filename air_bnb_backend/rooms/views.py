from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


def see_all_rooms(request):
    rooms = Room.objects.all()  # DB에 모든 정보를 받아왔고
    return render(
        request,
        "all_rooms.html",
        {
            "rooms": rooms,
            "title": "Hello! this title comes from djanog!",
        },
    )  # HTML을 렌더링 "" <- key, rooms <- value


def see_one_rooms(request, room_id):
    return HttpResponse(f"see room with id: {room_id}")
