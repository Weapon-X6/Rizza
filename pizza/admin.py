from django.contrib import admin

from .models import Pizza, Pizzeria

admin.site.register(Pizzeria)
admin.site.register(Pizza)
