from django.shortcuts import render
from myApp2 import  models
# Create your views here.
def kk(request):
    a=models.bookdetails.objects.all()
    return render(request, "index.html", {"li":a})