from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# views : when user access some url, this method will work

def see_all_rooms(request):
    rooms = Room.objects.all()                                        # got the info about all rooms from DB
    return render(
        request,
        "all_rooms.html", 
        {
            "rooms": rooms,
            "title": "Hello! this title comes from django!"

        }, 
    )        # rendered HTML to user

def see_one_room(request, room_pk):
    try:
        room = Room.objects.get(pk= room_pk)
        return render(request, "room_detail.html", {"room": room, })
    except Room.DoesNotExist:
        return render(request, "room_detail.html", {'not_found': True})     # customized error

