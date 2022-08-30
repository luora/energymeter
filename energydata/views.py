from http.client import responses
from django.shortcuts import render
from rest_framework.response import Response
from energydata.services import computeKwh, computeKwhProfile
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

from rest_framework import viewsets
from energydata.models import EnergyData, MeterInfo
from energydata.serializers import EnergyDataSerializer, MeterInfoSerializer
from rest_framework.decorators import api_view,permission_classes
import datetime



# Create your views here.
class EnergyDataViewset(generics.ListCreateAPIView):
    #queryset = EnergyData.objects.all()
    serializer_class = EnergyDataSerializer
    http_method_names = ['get', 'post', 'head', 'options']

    def get_object(self):
        return get_object_or_404(EnergyData,meter_info = self.request.query_params.get("meter_number") )

    # def get(self, request,):
    #     meter_number = self.request.query_params.get("meter_number", None)

    #     if meter_number is None:
    #         return Response(data={
    #             "info": "meter_number is blank"
    #         },h
    #             status = status.HTTP_400_BAD_REQUEST
    #        )

    
    def get_queryset(self):
        # qs = get_object_or_404(EnergyData,meter_info = self.request.query_params.get("meter_number") )
        # if qs is None:
        #     re
        meter_number = self.request.query_params.get("meter_number", None)
        start_date = self.request.query_params.get('start_date', None)
        last_date = self.request.query_params.get('end_date', None)

        # if meter_number is None:
        #     return Response(data={
        #         "info": "meter_number is blank"
        #     },
        #     status = status.HTTP_400_BAD_REQUEST
        #     )

        return EnergyData.objects.filter(meter_info = meter_number, timestamp__range=[start_date,last_date])


class MeterInfoViewset(generics.ListCreateAPIView):
    queryset = MeterInfo.objects.all()
    serializer_class = MeterInfoSerializer
    http_method_names = ['get', 'post', 'head', 'options']


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@action(detail=False)
def EnergyProfileView(request):
    print("get data")
    meter_number = request.query_params.get('meter_number', None)
    start_date = request.query_params.get('start_date', None)
    last_date = request.query_params.get('end_date', None)

    print("start date {} ".format(start_date))
    print("last date {} ".format(last_date))

    # queryset = EnergyData.objects.filter(date__range=[])

    if meter_number is None:
        return Response(
            data = {
                "info":"meter number has not been provided"
            }
        )

    if start_date is None and last_date is None:
        return Response(data={
            "info": "enter start and end dates"
        })

    #raw_data = EnergyData.objects.filter(timestamp__gte=start_date, timestamp__lte=last_date)
        return self.meter_info.meter_number
    raw_data = EnergyData.objects.filter(timestamp__range=[start_date,last_date],meter_info__meter_number=meter_number)

    if(len(raw_data)==0 ):
        return Response(
            data={"info":"no data available for that date range"}
        )

    print("####")
    # print(raw_data)

    print(raw_data[0].voltage)

    print(len(raw_data))

    total_kwh = computeKwh(raw_data)

    return Response(data={
        "start_date": start_date,
        "end_date": last_date, 
        "total_kwh": total_kwh,
        "unit": "kWh"
        })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@action(detail=False)
def EnergyProfileViewRange(request):
    print("get data")
    meter_number = request.query_params.get('meter_number', None)
    start_date = request.query_params.get('start_date', None)
    last_date = request.query_params.get('end_date', None)

    # print("start date {} ".format(start_date))
    # print("last date {} ".format(last_date))

    # queryset = EnergyData.objects.filter(date__range=[])

    if start_date is None and last_date is None:
        return Response(data={
            "info": "enter start and end dates"
        })

    #raw_data = EnergyData.objects.filter(timestamp__gte=start_date, timestamp__lte=last_date)
    raw_data = EnergyData.objects.filter(timestamp__range=[start_date,last_date], meter_info__meter_number=meter_number)

    if(len(raw_data)==0 ):
        return Response(
            data={"info":"no data available for that date range"}
        )

    print("####")
    # print(raw_data)

    print(raw_data[0].voltage)

    print(len(raw_data))

    profile = computeKwhProfile(raw_data)

    return Response(data=profile)



    




# class EnergyProfileViewset(viewsets.GenericViewSet):

#     http_method_names = ['get', 'options', 'head']
#     permission_classes = () 

#     def retrieve():
#          pass



   