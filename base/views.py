from django.http import HttpResponse
from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Let\'s learn Python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend Developers'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    context = {}
    for room in rooms:
        if room['id'] == int(pk):
            context['room'] = room
            break
    return render(request, 'base/room.html', context)