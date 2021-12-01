from django.shortcuts import render


from .models import Pizza


# Create your views here.

def index(request): 
    return render(request, 'MainApp/home.html')

def pizza(request):
    pizza = Pizza.objects.order_by('date_added')

    context = {'pizza': pizza}

    return render(request, 'MainApp/topics.html', context)
