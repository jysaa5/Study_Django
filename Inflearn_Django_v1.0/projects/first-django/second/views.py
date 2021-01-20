from django.shortcuts import render
from second.models import Post
from .forms import PostForm

# Create your views here.
def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    form = PostForm()
    return render(request, 'second/create.html', {'form': form})
