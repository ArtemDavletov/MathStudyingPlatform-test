from django.contrib import admin

# Register your models here.
from jb_task2.socnet.models import User, Relationship

admin.site.register(User)
admin.site.register(Relationship)
