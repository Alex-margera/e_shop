from django.urls import path
from blog import views as blog

urlpatterns = [
    path("", blog.blog_page, name="blog.html"),
    path("single/", blog.single_blog_page, name="single_blog.html"),
]