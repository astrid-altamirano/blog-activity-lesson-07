from django.contrib import admin
from blog.models import Post, Category,Comment  # <-- import Category
# Put today

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)

# Register your models here.
# blog/admin.py

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

