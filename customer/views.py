from django.shortcuts import render, redirect
from room.models import Room
from .models import Customer
from .forms import bookingForm
import datetime

# Create your views here.
def home_view(request):
    room = Room.objects.all()[:3]

    context = {
        'room' : room,
    }  
    return render(request, "index.html", context)

def allrooms(request):
    room = Room.objects.all()

    context = {
        'room' : room,
    }  
    return render(request, "allrooms.html", context)

def room_view(request, id):
    room = Room.objects.get(id = id)
    form = bookingForm()

    
    todaydate = datetime.date.today()
    

    if room.is_booked: 
        currentcus = Customer.objects.get(room = room)
       
        if currentcus == None:
            room.is_booked = False
            room.save()
        if currentcus.room_end < todaydate: 
            currentcus.room = None
            currentcus.save()           
            room.is_booked = False
            room.save() 

    context ={
        'room' : room,
        'form' : form,
    }

    if request.method == 'POST':
        form = bookingForm(request.POST)
        if form.is_valid():
            auser = form.save(commit=False)
            

            auser.save()
            
            customer = Customer.objects.get(id = auser.id)
            customer.room = room
            customer.save()

            room.is_booked = True
            room.save()

            return render(request, "rooms.html", context)

    return render(request, "rooms.html", context)

def cancelroom(request, id):
    room = Room.objects.get(id=id)

    if room.is_booked == False:
        return redirect('home')

    if request.method == 'POST':
        room.is_booked = False
        room.save()
        return redirect('home')

    context = {
        'room' : room,
    }
    return render(request, "cancel.html", context)