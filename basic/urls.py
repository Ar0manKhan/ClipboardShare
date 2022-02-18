from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "basic"
urlpatterns = [
    path("", TemplateView.as_view(template_name="basic/index.html")),
    path("create", views.create, name="create"),
    path("getroom/<slug:room_id>", views.GetRoom.as_view(), name="getroom")
]
