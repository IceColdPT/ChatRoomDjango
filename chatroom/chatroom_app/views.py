from django.shortcuts import render
from .forms import CHATFORM

def MAINPAGE(request):

    chatForm = CHATFORM(request.POST)

    if chatForm.is_valid:
        print(chatForm)

    data = {
        "form" : chatForm
    }

    return render(request,"index.html",data)
