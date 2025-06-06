from rest_framework import serializers
from .models import Client, Instructor, FitnessClass, Booking

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'client_name', 'client_email']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'address', 'contact_number', 'email']

class FitnessClassSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)
    instructor_id = serializers.PrimaryKeyRelatedField(
        queryset=Instructor.objects.all(), source='instructor', write_only=True
    )

    class Meta:
        model = FitnessClass
        fields = ['id', 'scheduled_start_time', 'class_type', 'instructor', 'instructor_id',"remaining_slots","end_time"]

class BookingSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), source='client', write_only=True
    )
    fitness_class = FitnessClassSerializer(read_only=True)
    fitness_class_id = serializers.PrimaryKeyRelatedField(
        queryset=FitnessClass.objects.all(), source='fitness_class', write_only=True
    )

    class Meta:
        model = Booking
        fields = ['id', 'client', 'client_id', 'fitness_class', 'fitness_class_id', 'timestamp', 'is_confirmed']
