from django.shortcuts import render, get_object_or_404
from .models import Post


def render_posts(request):
    posts= Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


#aca intente numerar los posts publicados, para buscarlos en serie del 1 en adelante , pero no funciona (?)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})
                  
                  



