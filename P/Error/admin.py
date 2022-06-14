from django.contrib import admin
from .models import ERRORModel
from .models import Comment

# Register your models here.
admin.site.register(ERRORModel)
admin.site.register(Comment)