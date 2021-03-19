from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    lorem_ipsum= "lorem ipsum dolor sit amet, etc"
    return HttpResponse(lorem_ipsum)

def contact(request):
    return render(request, 'contact.html')

# def index(request):
#     return render(request, 'index.html')


    # 1. make a view function
    # 2. make the html page
    # 3. add the view to the urls.py inside of main_app.urls

    # when i go to localhost:8000/contact

    # django => urls => /contact => views.contact (runs function)