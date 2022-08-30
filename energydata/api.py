from django.db import router
from rest_framework import routers
from energydata import views

router = routers.DefaultRouter()

router.register(r'energydata',views.EnergyDataViewset)
router.register(r'meterinfo', views.MeterInfoViewset)

# router.register(r'energyprofile', views.EnergyProfileView)