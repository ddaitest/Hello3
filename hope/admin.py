from django.contrib import admin

# Register your models here.
from .models import Driver, Task

admin.site.register(Driver)
admin.site.register(Task)