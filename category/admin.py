from django.contrib import admin

# Register your models here.
from category.models import *

admin.site.register(Category)
admin.site.register(Post)