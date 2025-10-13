from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method =="POST":
        print("submit")
        messages.error(request, 'Account creeated successfully')
        #debug message content
        #storage = messages.get_messages(request)
        #for message in storage:
        #    print(message.level_tag, message.message)
        #debug end    
        return redirect('accounts:register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return redirect("pages:index")

def dashboard(request):
    return render(request,'accounts/dashboard.html')