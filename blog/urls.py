# blog/urls.py
from django.urls import path,include
from . import views
from blog.views import stub_view

urlpatterns = [
    
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    
]
