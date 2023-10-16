from rest_framework import serializers


class serializerAirport(serializers.Serializer):
    code = serializers.CharField(max_length=3) 
    city = serializers.CharField(max_length=64)



