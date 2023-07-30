from django.contrib import admin

# Register your models here.
from .models import Cliente, Ciudad

admin.site.register(Cliente)
admin.site.register(Ciudad)