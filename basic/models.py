from django.db import models
from django.utils.timezone import now   # For setting time by default
from random import choices  # For creating random room code


def generate_string() -> str:
    """Creating random string of length 4 character"""
    return ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=4))

# Create your models here.


class Room(models.Model):
    room_code = models.CharField(
        max_length=4,
        unique=True,
        default=generate_string
    )
    created = models.DateTimeField(default=now, editable=False)

    def __str__(self) -> str:
        return f"Room({self.room_code})"


class Clipboard(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Clipboard({self.room}, {self.text})"
