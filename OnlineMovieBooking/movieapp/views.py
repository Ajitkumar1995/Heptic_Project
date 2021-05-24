from django.shortcuts import render,redirect
from .models import *
from .import forms
from .forms import SeatForm,BookingForm,SelectedSeatForm
from django.core.mail import send_mail
import datetime
def index(request):
    send_mail("Hello gmail",
              'Hello there, This is an automated message',
              'kajit4416@gmail.com',
              ['ajit11000@gmail.com'],fail_silently=False,auth_user=None,auth_password=None,connection=None)
    return render(request,'booking/index.html')

def reserve_seat(request,pk=1):
    try:
        show_info = Show.pk
    except:
        raise Exception("Page Does Not Exist.")
    form  = SeatForm()
    form2 = SelectedSeatForm()
    context = {'show_info':show_info,'form':form,'form2':form2}
    return render(request,'booking/reserve_seat.html',context)


def movie_list(request):
    movies = Movie.objects.all().order_by('language')
    movie_list = []
    movie_by_lang = []
    lang = movies[0].language
    for i in range(0, len(movies)):
        if lang != movies[i].language:
            lang = movies[i].language
            movie_list.append(movie_by_lang)
            movie_by_lang = []
        movie_by_lang.append(movies[i])
        movie_list.append(movie_by_lang)
    return render(request, 'movie/movie_list.html', {'movies': movie_list})

def movie_details(request, movie_id):
    movie_info = Movie.objects.get(pk=movie_id)
    shows = Show.objects.filter(movie=movie_id,
	date=datetime.date.today()).order_by('theatre')
    show_list = []
    show_by_theatre = []
    theatre = shows[0].theatre
    for i in range(0, len(shows)):
        if theatre != shows[i].theatre:
            theatre = shows[i].theatre
            show_list.append(show_by_theatre)
            show_by_theatre = []
            show_by_theatre.append(shows[i])
        show_list.append(show_by_theatre)
    return render(request, 'movie/movie_details.html',{'movie_info': movie_info, 'show_list': show_list})


def theatre_list(request):
    theatres = Theatre.objects.all().order_by('city')
    theatre_list = []
    theatre_by_city = []
    city = theatres[0].city
    for i in range(0, len(theatres)):
        if city != theatres[i].city:
            city = theatres[i].city
            theatre_list.append(theatre_by_city)
            theatre_by_city = []
        theatre_by_city.append(theatres[i])
    theatre_list.append(theatre_by_city)
    return render(request, 'theatre/theatre_list.html', {'theatres': theatre_list})


def theatre_details(request, theatre_id):
    theatre_info = Theatre.objects.get(pk=theatre_id)
    shows = Show.objects.filter(theatre=theatre_id,
	date=datetime.date.today()).order_by('movie')
    show_list = []
    show_by_movie = []
    movie = shows[0].movie
    for i in range(0, len(shows)):
        if movie != shows[i].movie:
            movie = shows[i].movie
            show_list.append(show_by_movie)
            show_by_movie = []
            show_by_movie.append(shows[i])
        show_list.append(show_by_movie)
    print(show_list)
    return render(request, 'theatre/theatre_details.html',{'theatre_info': theatre_info, 'show_list': show_list})

#payment confirmation and booking method
