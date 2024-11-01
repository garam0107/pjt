
from django.urls import path
from . import views

app_name= 'weathers'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('save-data/', views.savedata, name = 'savedata'),

]
