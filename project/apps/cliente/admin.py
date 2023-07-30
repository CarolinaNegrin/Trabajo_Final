from django.contrib import admin

# Register your models here.
from .models import Cliente, Ciudad

admin.register(Cliente)
admin.register(Ciudad)