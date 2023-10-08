from django.contrib import admin
from moviebase.models import Actor,Director,Gender,Movie

# Register your models here.
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Gender)
admin.site.register(Movie)