from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Stas',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'November 18'
    },
{
        'author': 'Oleg',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'November 18'
    }
]

def home (request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about (request):
    return render(request, 'blog/about.html')

