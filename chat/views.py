from django.shortcuts import render

def index(request):
    # Here you might list chat rooms or something similar
    return render(request, 'chat/index.html')

def room(request, room_name):
    # Render the chat room page with the room name
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
