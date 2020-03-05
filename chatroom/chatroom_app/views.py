from django.shortcuts import render
from .forms import CHATFORM
from .models import CHAT_MESSAGE ,USER
def MAINPAGE(request):
    command = 0
    chatForm = CHATFORM(request.POST)
    chatMessages = CHAT_MESSAGE.objects.all()
    if chatForm.is_valid():
        message = chatForm.cleaned_data["message"]
        if message == "!help" or message == "!commands":
            command = 1
        else:
            command = 0
            CHAT_MESSAGE.objects.get_or_create(messageText=message )

    else:
        pass

    data = {
        "form" : chatForm,
        "msgs" : chatMessages,
        "command": command
    }

    return render(request,"index.html",data)
