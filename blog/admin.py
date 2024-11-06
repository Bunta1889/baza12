from django.contrib import admin
from .models import Blog, BlogComment, User

admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(User)

# Register your models here.
