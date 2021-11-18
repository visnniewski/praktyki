from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Title

def index(request):
    latest_blog_post_list = Title.objects.order_by('-pub_date')[:10]
    context = {
        'latest_blog_post_list': latest_blog_post_list
    }
    return render(request, 'blog/index.html', context)

def blogpost(request, post_id):
    post = get_object_or_404(Title, pk=post_id)
    return render(request, 'blog/post.html', {'post': post})

def postedit(request, post_id):
    post = get_object_or_404(Title, pk=post_id)
    return render(request, 'blog/edit.html', {'post': post})

def changepost(request, post_id):
    post = get_object_or_404(Title, pk=post_id)
    new_description = post.description_set.get(pk=post_id)
    new_description.description_text = request.POST['post-description']
    post.pub_date = timezone.now()
    post.save()
    new_description.save()
    return HttpResponseRedirect(reverse('blogpost', args=(post.id,)))

def deletepost(request, post_id):
    post = get_object_or_404(Title, pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))

def add(request):
    return render(request, 'blog/add.html', {})

def addpost(request):
    # new_post = Title.objects.create(pk=len(Title.objects.all()) + 1)
    # post = get_object_or_404(Title, pk=new_post.id)
    # new_post.pub_date = timezone.now()
    # new_post.title_text = request.POST['new_title']
    # new_post.save()
    # description = post.description_set.get(pk=new_post.id)
    # description.description_text = request.POST['post-description']
    # description.save()
    return HttpResponseRedirect(reverse('index'))