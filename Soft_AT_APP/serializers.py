from rest_framework import serializers
from .models import *

class ser_Soft_At_upload_status(serializers.ModelSerializer):
    class Meta:
        model = Soft_At_upload_status
        fields = '__all__'

