from django.shortcuts import redirect, render


from .models import Pizza

from .forms import PizzaForm

# Create your views here.

def index(request): 
    return render(request, 'MainApp/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all().order_by('date_added')

    context = {'pizzas': pizzas}

    return render(request, 'MainApp/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    toppings = pizza.toppings_set.all()
    context = {'pizza':pizza, 'toppings': toppings}
    comments = pizza.comment_set.all()
    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments}

    return render(request, 'MainApp/pizza.html', context)

def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
     
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect ('pizzas:pizza', pizza_id = pizza_id)
    
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_comment.html', context)





