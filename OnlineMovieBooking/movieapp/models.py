from django.db import models
from django.conf import settings
import datetime
# Create your models here.
class Theatre(models.Model):
    city=(('BLR','Bangalore'),
          ('DEL','Delhi'),
          ('MUM','Mumbai'),
          ('PUN','Pune'),
          ('CHN','Chennai'),)
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=3,choices=city)
    address=models.CharField(max_length=50)
    admin_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)+"-"+str(self.address)+"-"+str(self.city)
class Movie(models.Model):
    lang_choice=(
        ('Eng','English'),
        ('HIN','Hindi'),
        ('TAM','Tamil'),
        ('TEL','Telugu'),)
    rating=(
        ('U', 'U'),
        ('UA', 'U/A'),
        ('A', 'A'),
        ('R', 'R'),)
    name=models.CharField(max_length=30)
    cast=models.CharField(max_length=100)
    director=models.CharField(max_length=50)
    language=models.CharField(max_length=3,choices=lang_choice)
    certificate=models.CharField(max_length=2,choices=rating)
    popularity_index=models.IntegerField(unique=True)
    def __str__(self):
        return self.name

class Show(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    theatre=models.ForeignKey(Theatre,on_delete=models.CASCADE)
    screen=models.IntegerField(default=1)
    date=models.DateField()
    time=models.TimeField()
    def __str__(self):
        return str(self.movie)+"-"+str(self.theatre)+"-"+str(self.date)+"-"+str(self.time)

class Booking(models.Model):
    payment_choice=(
        ('cd','Credit Card'),
        ('db','Debit Card'),
    )
    id=models.CharField(primary_key=True,max_length=200)
    payment_type=models.CharField(max_length=2,choices=payment_choice,default="Credit Card")
    paid_amount=models.DecimalField(max_digits=8,decimal_places=2)
    paid_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.id)

class Seat(models.Model):
    seat_choice=(
        ('','Select'),
        ('Silver','Silver'),
        ('Gold','Gold'),
        ('Platinum','Platinum'),
    )
    no=models.CharField(max_length=3,null=True)
    seat_type=models.CharField(max_length=8,choices=seat_choice,blank=False)
    show=models.ForeignKey(Show,on_delete=models.CASCADE)
    class Meta:
        unique_together=('no','show')
    def __str__(self):
        return self.no+str(self.show)
class BookedSeat(models.Model):
    seat=models.ForeignKey(Seat,on_delete=models.CASCADE)
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    class Meta:
        unique_together=('seat','booking')
    def __str__(self):
        return str(self.seat)+'-'+str(self.booking)
