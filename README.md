## 📽️ Loom Demo

🎥 [Click here to watch the demo](https://www.loom.com/share/cd36cc8124ae4627bb2a024c43d22b07?sid=8d20371d-90da-482b-9997-09166fd4fa99)

---

# 🏋️‍♀️ Fitness Studio Booking API

This is a simple Django RESTful API built for managing fitness classes, instructors, clients, and class bookings. It allows users to view upcoming classes, book a class, and view their bookings.

---

## 📌 Features

- View upcoming fitness classes (Yoga, Zumba, HIIT)
- Book a class by providing client and class details
- Prevents overbooking by checking available slots
- Fetch all bookings by client email or booking ID
- Timezone aware (supports IST)
- Clean and modular Django code structure

---

## 🚀 Technologies Used

- Python 3
- Django & Django REST Framework
- SQLite (for simplicity)
- Timezone Support via `django.utils.timezone`

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arsit938/fitness-booking-app-omnify.git
   cd booking_app
   ```

2. **Create virtual environment & activate**
   ```bash
   python -m venv env
   source env/bin/activate  
   ```
   *On Windows:* 
   ```bash
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
  ```bash
  python manage.py makemigrations
  ```
   ```bash
   python manage.py migrate
   ``` 

5. **Run the server**
   ```bash
   python manage.py runserver
   ```

---

## 📂 API Endpoints

### ✅ Get All Upcoming Classes
```
GET http://127.0.0.1:8000/api/upcoming-classes/
```
Returns all fitness classes scheduled **after the current time**.

**Sample Response:**
```json
{
  "data": [
      {
          "id": "1b4236cb-e97d-4514-92cf-80e1a3e41f51",
          "scheduled_start_time": "2025-06-06T11:44:53Z",
          "class_type": "Yoga",
          "instructor": {
              "id": "b3e658c8-d62e-47bc-bd59-5159f7433df5",
              "name": "ABC",
              "address": "xyz123",
              "contact_number": "1234567890",
              "email": "abc@123.com"
          },
          "remaining_slots": 100,
          "end_time": "2025-06-06T12:46:00Z"
      }
  ]
}
```

---

### ✅ Book a Class
```
POST http://127.0.0.1:8000/api/book-class/
```

**Sample Request Body:**
```json
{
  "client_name": "Jane Doe",
  "client_email": "jane@example.com",
  "fitness_class_id": ""
}
```

**Sample Response:**
```json
{
  "booking_details": {
      "id": "fb8edc30-579e-46ae-8c8f-81b463106f6b",
      "client": {
          "client_id": "9f26f99b-2da0-471d-a5f5-6d4a7568c200",
          "client_name": "Jane Doe",
          "client_email": "jane@example.com"
      },
      "fitness_class": {
          "id": "1b4236cb-e97d-4514-92cf-80e1a3e41f51",
          "scheduled_start_time": "2025-06-06T11:44:53Z",
          "class_type": "Yoga",
          "instructor": {
              "id": "b3e658c8-d62e-47bc-bd59-5159f7433df5",
              "name": "ABC",
              "address": "xyz123",
              "contact_number": "1234567890",
              "email": "abc@123.com"
          },
          "remaining_slots": 99,
          "end_time": "2025-06-06T12:46:00Z"
      },
      "timestamp": "2025-06-06T10:02:46.690934Z",
      "is_confirmed": true
  }
}
```

---

### ✅ Get All Bookings
```
GET api/get-booking-list/?client_email=jane@example.com
```

**Sample Response:**
```json
{
  "data": [
      {
          "id": "fb8edc30-579e-46ae-8c8f-81b463106f6b",
          "client": {
              "client_id": "9f26f99b-2da0-471d-a5f5-6d4a7568c200",
              "client_name": "Jane Doe",
              "client_email": "jane@example.com"
          },
          "fitness_class": {
              "id": "1b4236cb-e97d-4514-92cf-80e1a3e41f51",
              "scheduled_start_time": "2025-06-06T11:44:53Z",
              "class_type": "Yoga",
              "instructor": {
                  "id": "b3e658c8-d62e-47bc-bd59-5159f7433df5",
                  "name": "ABC",
                  "address": "xyz123",
                  "contact_number": "1234567890",
                  "email": "abc@123.com"
              },
              "remaining_slots": 99,
              "end_time": "2025-06-06T12:46:00Z"
          },
          "timestamp": "2025-06-06T10:02:46.690934Z",
          "is_confirmed": true
      }
  ]
}
```

or  
if user wants to look into a specific booking provide booking id inside url just like below
```
GET http://127.0.0.1:8000/api/get-booking/<str:pk>/
```
**Sample URL Request**
```
GET http://127.0.0.1:8000/api/get-booking/fb8edc30-579e-46ae-8c8f-81b463106f6b/
``` 

**Sample Response**

```json
{
  "data": {
      "id": "fb8edc30-579e-46ae-8c8f-81b463106f6b",
      "client": {
          "client_id": "9f26f99b-2da0-471d-a5f5-6d4a7568c200",
          "client_name": "Jane Doe",
          "client_email": "jane@example.com"
      },
      "fitness_class": {
          "id": "1b4236cb-e97d-4514-92cf-80e1a3e41f51",
          "scheduled_start_time": "2025-06-06T11:44:53Z",
          "class_type": "Yoga",
          "instructor": {
              "id": "b3e658c8-d62e-47bc-bd59-5159f7433df5",
              "name": "ABC",
              "address": "xyz123",
              "contact_number": "1234567890",
              "email": "abc@123.com"
          },
          "remaining_slots": 99,
          "end_time": "2025-06-06T12:46:00Z"
      },
      "timestamp": "2025-06-06T10:02:46.690934Z",
      "is_confirmed": true
  }
}
```

---

## 🙌 Author

**Arshit**  
Python | Django | LLM Integration  
[GitHub](https://github.com/Arshit938)
