from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from api.models import FitnessClass,Booking, Client
from django.utils import timezone
from api.serialiser import FitnessClassSerializer,BookingSerializer

class GetAllUpcomingClasses(APIView):
    def get(self,request):
        try:
            objs = FitnessClass.objects.all().order_by("-scheduled_start_time")
            lst = []
            lst = [i for i in objs if i.scheduled_start_time >= timezone.now()]
            ser = FitnessClassSerializer(lst,many=True)
            return Response(
                {
                    "data": ser.data
                },status=status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            return Response(
                {
                    "error":"no fitness classes found!"
                },status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "error":f"{e}"
                },status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class BookClass(APIView):
    def post(self,request):
        try:
            data = request.data
            client_name = data.get("client_name")
            client_email = data.get("client_email")
            fitness_class_id = data.get("fitness_class_id")
            
            #check availability
            cls = FitnessClass.objects.get(id=fitness_class_id)
            if cls.remaining_slots==0:
                return Response(
                    {
                        "error":"No available slots in this fitness class"
                    }
                )

            

            #continue booking
            client, is_created = Client.objects.get_or_create(
                client_email = client_email,
                defaults={
                    'client_name': client_name
                }
            )
            booking = Booking.objects.create(
                client=client,
                fitness_class = cls
            )
            cls.remaining_slots-=1
            cls.save()
            ser = BookingSerializer(booking)
            return Response(
                {
                    "booking_details":ser.data
                },status=status.HTTP_201_CREATED
            )
        except ObjectDoesNotExist:
            return Response(
                {
                    "error":"no fitness classes found!"
                },status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            if FitnessClass.objects.filter(id=fitness_class_id).exists():
                booking = Booking.objects.create(
                    client=client,
                    fitness_class = cls,
                    is_confirmed = False
                )
            return Response(
                {
                    "error":f"{e}"
                },status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )   
        
class GetAllBookings(APIView):
    def get(self,request,pk=None):
        try:
            if pk:
                booking = Booking.objects.get(id=pk)
                ser = BookingSerializer(booking)
                return Response(
                    {
                        "data": ser.data
                    },status=status.HTTP_200_OK
                )
            else:
                client_email = request.GET.get("client_email")
                client = Client.objects.get(client_email=client_email)
                bookings = Booking.objects.filter(client=client).order_by("-timestamp")
                ser = BookingSerializer(bookings,many=True)
                return Response(
                    {
                        "data": ser.data
                    },status=status.HTTP_200_OK
                )
        except ObjectDoesNotExist:
            return Response(
                {
                    "error":"invalid id"
                },status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {
                    "error":f"{e}"
                },status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )       
