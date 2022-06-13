from django.contrib import admin
from .models import ERROR
from .models import Comment

# Register your models here.
admin.site.register(ERROR)
admin.site.register(Comment)