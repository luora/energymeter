from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import EnergyData, MeterInfo


class MeterInfoSerializer(ModelSerializer):

    timestamp = serializers.DateTimeField()

    class Meta:
        model = MeterInfo
        fields =["meter_info","voltage","current", "inst_power", "power_factor","frequency","timestamp"]


class EnergyDataSerializer(ModelSerializer):

    class Meta:
        model = EnergyData
        fields = "__all__" 