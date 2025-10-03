from django.shortcuts import render

from listings.models import Listing
def index(request):
    listings = Listing.objects.filter(is_publish=True)[:3]
    context = {"listings":listings}
    return render(request,'pages/index.html' , context)

def about(request):
    return render(request,'pages/about.html')




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