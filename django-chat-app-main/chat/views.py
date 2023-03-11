import datetime
from django.shortcuts import render, redirect
from chat.models import Message
from django.http import HttpResponse, JsonResponse
from chat.chbot import cbot
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from chat.forms import CustomUser
from django.contrib import messages
# Create your views here.

def loginuser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('room')

        messages.warning(request,"Bad login credentials")
    
    u=User.objects.all()
    return render(request,'login.html',{'page':page , 'user':u})

def logoutuser(request):
    logout(request)
    return redirect('login')

def registeruser(request):
    page = 'register'
    form=CustomUser()
    context = {'form':form, 'page':page}
    if request.method=="POST":
        form = CustomUser(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request,username=user.username,password=request.POST['password1'])

            if user is not None:
                login(request,user)
                return redirect('room')
        
        else:
            context = {'form':form, 'page':page}
            return render(request, 'login.html',context)
    return render(request, 'login.html',context)

# @login_required(login_url='login')
# def home(request):
#     return render(request, 'home.html')

@login_required(login_url='login')
def room(request):
    username = request.user.username
    room_details = Message.objects.filter(user=request.user)
    return render(request, 'home.html', {
        'username': username,
        'room_details': room_details
    })

@login_required(login_url='login')
def send(request):
    print(1234567)
    message = request.POST['message']
    username = request.user
    x = datetime.datetime.now()
    d = x.strftime("%x")
    t = x.strftime("%X")

    new_message = Message.objects.create(value=message, user=username,user_message=True,date=d,time=t)
    new_message.save()
    text = cbot(message)
    new_message = Message.objects.create(value=text, user=username,bot_message=True,date=d,time=t)
    new_message.save()
    print(text)
    return HttpResponse('Message sent successfully')

@login_required(login_url='login')
def getMessages(request):
    username = request.user
    messages = Message.objects.filter(user = username)
    return JsonResponse({"messages":list(messages.values())})