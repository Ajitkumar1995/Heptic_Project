from django.contrib import admin
from .models import Theatre,Movie,Show,Booking,Seat,BookedSeat
# Register your models here.
class TheatreAdmin(admin.ModelAdmin):
    class Meta:
        model=Theatre
admin.site.register(Theatre,TheatreAdmin)

class MovieAdmin(admin.ModelAdmin):
    class Meta:
        model=Movie
admin.site.register(Movie,MovieAdmin)

class ShowAdmin(admin.ModelAdmin):
    class Meta:
        model=Show
admin.site.register(Show,ShowAdmin)

class BookingAdmin(admin.ModelAdmin):
    class Meta:
        model=Booking
admin.site.register(Booking,BookingAdmin)


class SeatAdmin(admin.ModelAdmin):
    class Meta:
        model=Seat
admin.site.register(Seat,SeatAdmin)

class BoookedSeatAdmin(admin.ModelAdmin):
    class Meta:
        model=BookedSeat
admin.site.register(BookedSeat,BoookedSeatAdmin)