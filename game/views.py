from django.shortcuts import render
from game.forms import *
from django.core.mail import send_mail
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request,'home.html')



def registration(request):
    ERFO=RegistrationForm()
    d={'ERFO':ERFO}
    if request.method=='POST':
        NMRFO=RegistrationForm(request.POST)  #Non Modifiable Registration Form Object

        if NMRFO.is_valid():
            MRFO=NMRFO.save(commit=False)
            pwd=NMRFO.cleaned_data['password']
            MRFO.set_password(pwd)
            MRFO.save()
            


            message = f"""
            Hi {MRFO.username},

            Welcome to Guess Master!

            Your account has been successfully created.
            Now you can start playing and test your guessing skills.

            If you did not create this account, please ignore this email.

            Happy Guessing! 🎯
            """


            send_mail("Welcome to Guess Master 🎉",message,'krishnaegv@gmail.com',[MRFO.email],fail_silently=False)

            return HttpResponseRedirect(reverse('home'))
        else:
            print(NMRFO.errors)
            return HttpResponse('invalid ')









    return render(request,'registration.html',d)





def signin(request):
    return render(request,'signin.html')