from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    path('new_comment/<int:pizza_id>/',views.new_comment, name='new_comment')

]

