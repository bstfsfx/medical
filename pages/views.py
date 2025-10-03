from django.shortcuts import render
from listings.models import Listing
from doctors.models import Doctor
def index(request):
    listings = Listing.objects.filter(is_publish=True)[:3]
    context = {"listings": listings}
    return render(request, 'pages/index.html' , context)

def about(request):
    doctors = Doctor.objects.order_by("-hire_date")[:3]
    mvp_doctors = Doctor.objects.all().filter(is_mvp=True)
    context = {
        "doctors":doctors,
        "mvp_doctors":mvp_doctors
    }
    return render(request,'pages/about.html', context)




#from django.http import HttpResponse

# Create your views here.

# functions

# views.index

#def index(request):
#    return HttpResponse("<h1>Hello world!</h1>")
#    print(request.path)
#   return render(request, 'pages/index.html')
#    return HttpResponse("<h1>Hello, world !</h1>")
# views.about

#def about(request):
#    print(request.path)
#    return render(request, 'pages/about.html')