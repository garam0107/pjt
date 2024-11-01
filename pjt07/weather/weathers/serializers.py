from .models import Weather
from rest_framework import serializers


'''
DB에 지정된 필드들만 포장에 관여할거면 ModelSerializer
- 여러 테이블의 데이터를 한 번에 포장: Nested Serializer,
DB 필드 외의 데이터들도 포장에 관여할거면 Serializer
'''
class weatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
