from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Person)
admin.site.register(BloodBank)
admin.site.register(Event)
admin.site.register(Donate)
admin.site.register(Request)