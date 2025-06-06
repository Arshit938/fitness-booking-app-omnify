from django.contrib import admin
from .models import Client, Instructor, FitnessClass, Booking

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email')
    search_fields = ('client_name', 'client_email')
    ordering = ('client_name',)

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_number', 'address')
    search_fields = ('name', 'email')
    ordering = ('name',)

@admin.register(FitnessClass)
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_type', 'scheduled_start_time', 'instructor',"remaining_slots")
    list_filter = ('class_type', 'scheduled_start_time')
    search_fields = ('instructor__name',)
    ordering = ('-scheduled_start_time',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'fitness_class', 'timestamp', 'is_confirmed')
    list_filter = ('is_confirmed', 'timestamp')
    search_fields = ('client__client_name', 'fitness_class__class_type')
    ordering = ('-timestamp',)

