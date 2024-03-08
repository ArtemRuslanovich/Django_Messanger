from django.shortcuts import render

from .models import Message

def home(request):
    messages = Message.objects.all()
    return render(request, '/Users/artemruslanovic/Django_Messanger/chat/templates/home.html', {'messages': messages})