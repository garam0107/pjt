from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    path('index/', views.index, name = "index"),
    path('check/<int:game_session_id>/', views.check, name = "check"),
]
