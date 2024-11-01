import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Weather
from .serializers import weatherSerializer

# Create your views here.

# 1. OpenWeather API로부터 데이터 다운로드 후 출력
@api_view(['GET'])
def index(request):
    # 외부에 보여지면 안되기 때문에 환경 변수로 빼내줘야 한다.
    apiKey = "7b23a2684c45240e820e7a3d86256dba"
    cityName = 'Busan,kr'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={cityName}&appid={apiKey}'
    response = requests.get(url).json()
    return Response(response)
    
def savedata(request):
    # 1. API를 통해 데이터를 가져온다
    # 2. 원하는 필드만 꺼내서 DB에 없다면 저장한다.
    apiKey = "7b23a2684c45240e820e7a3d86256dba"
    cityName = 'Busan,kr'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={cityName}&appid={apiKey}'
    response = requests.get(url).json()

    for li in response.get('list'):
        dt_txt = li.get('dt_txt')
        temp = li.get('main').get('temp')
        feels_like = li.get('main').get('feels_like')

        if data in Weather.objects.all():
            continue

        if Weather.objects.filter(dt_txt = dt_txt, temp = temp, feels_like = feels_like).exists():
            continue


        saveData = {
            'dt_txt' : dt_txt,
            'temp' : temp,
            'feels_like' : feels_like
        }

        serializer = weatherSerializer(data=saveData)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
    return JsonResponse({'message' : '저장 성공!'})
    # 3. DB에 저장하기 위해 데이터들을 포장(유효성 검증, 저장 등의 과정을 편하게 다루기 위해)
