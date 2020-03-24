from django.shortcuts import render


def blog_page(request):
    context = {
    }
    return render(request, "blog.html", context)

def single_blog_page(request):
    context = {
    }
    return render(request, "single_blog.html", context)


# Create your views here.
