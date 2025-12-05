from rest_framework import serializers
from 


class StudentSerializer(serializers.ModelSerializer) :
    class Meta:
        model=Student