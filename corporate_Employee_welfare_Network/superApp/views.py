from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"commom/homepage.html")


def loginform(request):
    return render(request,"commom/loginform.html")