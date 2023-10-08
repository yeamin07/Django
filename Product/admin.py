from django.contrib import admin
from .models import *


# Register your models here.

#username = Yeaminshop(for admin & user)
#email = xyz@gmail.com
#pass = 123456

#username= hello(for user)
#password = helloworld


admin.site.register(Category)
admin.site.register(Product)


