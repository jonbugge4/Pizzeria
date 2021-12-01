from django.contrib import admin

# Register your models here.
from .models import Pizza
admin.site.register(Pizza)

from .models import Toppings
admin.site.register(Toppings)

from .models import Comment
admin.site.register(Comment)

