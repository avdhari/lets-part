from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.utils import timezone

def Home(request):
    events = Event.objects.all().order_by('-date_published')

    return render(request, 'main/home.html', {'events': events})


def NewPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'main/newpost.html', {'form': form})