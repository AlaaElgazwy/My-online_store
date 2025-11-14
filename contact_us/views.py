from django.shortcuts import render
from .models import Contact_us
# Create your views here.

def contact_view(request):

    if request.method=='POST':
        Contact_us.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
       # return render(request,'contact_us/success.html')
    return render(request,'contact_us.html')    