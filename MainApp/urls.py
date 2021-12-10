from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizzas, name='pizzas'),
    path('pizza',views.pizza, name='pizza'),
    path('new_comment',views.new_comment, name='new_comment')

]