from django.db import models

# Create your models here.
class MeterInfo(models.Model):
    meter_number = models.CharField(max_length=100, unique=True,primary_key=True)
    location = models.CharField(max_length=100)
    install_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.meter_number


class EnergyData(models.Model):
    meter_info = models.ForeignKey(MeterInfo, on_delete=models.DO_NOTHING)
    voltage = models.FloatField(max_length=10,null=False)
    current = models.FloatField(max_length=10,null=False)
    inst_power = models.FloatField(max_length=10,null=False)
    power_factor = models.FloatField(max_length=10,null=False)
    frequency = models.FloatField(max_length=10,null=False)
    timestamp = models.DateTimeField()
    

    def __str__(self) -> str:
        return self.meter_info.meter_number