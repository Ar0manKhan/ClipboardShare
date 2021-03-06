from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Room, Clipboard
from django.views import generic
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


def join_room(request):
    return redirect(reverse("basic:getroom", args=[request.GET.get("room_code")]))


class GetRoom(generic.DetailView):
    model = Room
    template_name = "basic/room.html"
    context_object_name = "room_list"

    def post(self, request, pk):
        data = request.POST.get('text')
        room = get_object_or_404(Room, pk=pk)
        try:
            room.clipboard_set.create(text=data)
        except:
            return Http404()
        return redirect(request.path)
