"""
URL configuration for booking_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api.views import GetAllBookings,GetAllUpcomingClasses,BookClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/upcoming-classes/",GetAllUpcomingClasses.as_view()),
    path("api/get-booking-list/",GetAllBookings.as_view()),
    path("api/get-booking/<str:pk>/",GetAllBookings.as_view()),
    path("api/book-class/",BookClass.as_view()),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
