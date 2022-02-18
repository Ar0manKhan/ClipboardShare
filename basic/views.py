from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Room, Clipboard
from django.views import View
from django.db.utils import IntegrityError

# Create your views here.


def create(request):
    room_code = None
    # Run the loop untill the unqiue room_code is found.
    # Also having loop limit of 10 runs.
    for _ in range(10):
        try:
            room = Room()
            room.save()
            room_code = room.room_code
            break
        except IntegrityError:
            pass
    return redirect(reverse("basic:getroom", args=[room_code, ]))


class GetRoom(View):
    def get(self, request, room_id):
        return HttpResponse(f"Your room id is {room_id}")

    def post(self, request):
        pass
