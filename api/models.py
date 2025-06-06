from django.db import models
from uuid import uuid4

class Client(models.Model):
    client_id = models.UUIDField(default = uuid4, primary_key = True, editable = False)
    client_name = models.CharField(max_length = 225)
    client_email = models.CharField(max_length = 350, unique = True)

    def __str__(self) -> str:
        return self.client_name

class Instructor(models.Model):
    id = models.UUIDField(default = uuid4, primary_key = True, editable = False)
    name = models.CharField(max_length = 225)
    address = models.CharField(max_length = 500)
    contact_number = models.CharField(max_length=13)
    email =  models.CharField(max_length = 350, unique = True)

    def __str__(self) -> str:
        return self.name

class FitnessClass(models.Model):
    id = models.UUIDField(default = uuid4, primary_key = True, editable = False)
    scheduled_start_time = models.DateTimeField()
    instructor = models.ForeignKey(Instructor, on_delete = models.CASCADE, related_name = "fitness_classes")
    class_type = models.CharField(
        choices = [
            ("Yoga","Yoga"),
            ("HIIT","HIIT"),
            ("Zumba","Zumba")
        ],
        default="Yoga"
    )
    remaining_slots = models.BigIntegerField()
    end_time = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.class_type}->{self.scheduled_start_time}"

class Booking(models.Model):
    id = models.UUIDField(default = uuid4, primary_key = True, editable = False)
    client = models.ForeignKey(Client,  on_delete = models.CASCADE, related_name ="bookings")
    fitness_class = models.ForeignKey(FitnessClass,  on_delete = models.CASCADE, related_name ="cls")
    timestamp = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default = True)

    def __str__(self) -> str:
        return f"{self.client.client_name} {self.fitness_class.class_type} {self.timestamp}"


    

