from django.shortcuts import render
from django.views.generic import*
from django.http import HttpResponseRedirect
from .models import*
from .forms import*

# Create your views here.
class BlogView(ListView):
    model = Post
    template_name = 'Blog.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'

class PostListView(ListView):
    model = Post
    template_name = 'PostListView.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'

class PostView(DetailView):
    model = Post
    template_name = 'Post.html'

def Register(request):
    form = RegistrationForm()
    Form = {'form':form}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'Register.html', Form)