from django.shortcuts import render, redirect, get_object_or_404
from .models import Post,PostComent

# Create your views here.
def posthome(request):
    return render(request, 'posthome.html', {'posts': Post.objects.all()})

def postnew(request):
    return render(request, 'postnew.html')

def postcreate(request):
    if (request.method == 'POST'):
        new_post = Post()
        new_post.title = request.POST['title']
        new_post.content = request.POST['content']
        if 'image' in request.FILES.keys():
            new_post.image = request.FILES['image']
        new_post.save()
    return redirect('/post')

def postshow(request, post_id):
    one_post = get_object_or_404(Post, pk=post_id)
    coments = one_post.postcoment_set.all()
    return render(request, 'postshow.html', {'post': one_post, 'coments':coments})

def postedit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'postedit.html', {'post': post})

def postupdate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return redirect('/post/show/'+str(post_id))

def postdelete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('/post')

def postcomentcreate(request, post_id):
    if (request.method == 'POST'):
        post = get_object_or_404(Post, id=post_id)
        post.postcoment_set.create(title=request.POST['coment_content'])
    return redirect('/post/show/'+str(post_id))

def postcomentdelete(request, post_id,c_id):
    postcoment = get_object_or_404(PostComent, pk=c_id)
    postcoment.delete()
    return redirect('/post/show/'+str(post_id))