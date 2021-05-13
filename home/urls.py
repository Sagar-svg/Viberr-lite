
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('play/<int:song_id>/', views.play, name="play"),
    path('pause/<int:song_id>/', views.pause, name="pause"),

]
