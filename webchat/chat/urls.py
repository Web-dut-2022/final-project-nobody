from django.urls import path

from . import views

urlpatterns = [
    path("<room_name>/<user_name>/", views.room, name='room'),

]
