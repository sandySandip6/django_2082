from django.contrib import admin
from .models import Question

# Register your models here. 

admin.site.register(Question)
admin.site.site_header = "MyPost Admin"