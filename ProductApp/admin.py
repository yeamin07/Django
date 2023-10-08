from django.contrib import admin
from .models import *

# Register your models here.

#username = Yeamin(for admin)
#email = yeamin@gmail.com
#pass = 123456


admin.site.register(Product)
admin.site.register(Category)