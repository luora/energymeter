from django.contrib import admin
from energydata.models import MeterInfo, EnergyData

# Register your models here.
admin.site.register(MeterInfo)
admin.site.register(EnergyData)


