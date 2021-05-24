"""OnlineMovieBooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from movieapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('sendmail/',include('movieapp.urls')),
    #path('reserve/', views.reserve_seat),
    #path('movielist/',views.movie_list),
    #path('moviedetails/',views.movie_details),
    #path('theatrelist/',views.theatre_list),
    #path('theatredetails/',views.theatre_details),

]
