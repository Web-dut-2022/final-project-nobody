from django.urls import path, include
from django.contrib import admin

from user import views as uv

urlpatterns = [
    path("chat/", include('chat.urls')),
    path("", uv.login),
    path("logout/", uv.logout),
    path("register/", uv.register),
    path("userprofile/<username>", uv.userprofile, name='userprofile'),
    path("<username>/friendprofile/<friendname>", uv.friendprofile, name='friendprofile'),
    path("<username>/", uv.back2chat, name='back2chat'),
    path("admin/", admin.site.urls),
]
