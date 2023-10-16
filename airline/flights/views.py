from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from . serializers import serializerAirport
from rest_framework.renderers import JSONRenderer

from . models import Flight, Airport, Passenger
# Create your views here.
context = {"flights":Flight.objects.all()}

flight1 = Airport.objects.all()

# print(flight1)


# def api(request):
#     airport1 = Airport.objects.get(id=1)
#     airport1_ser = serializerAirport(airport1)
#     json_airport1 = JSONRenderer().render(airport1_ser.data)
#     return HttpResponse(json_airport1,content_type='application/json')
    


def index(request):
    return render(request,"flights/index.html",context)



def flight(request,flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request,"flights/flight.html",{"flight":flight,
      "passengers":flight.passengers.all(),
      "non_passengers":Passenger.objects.exclude(flights=flight).all()
      })

def book(request,flight_id):
    if request.method=="POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
    
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

