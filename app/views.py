from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Post




def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html',{'title': 'About'})

def appliances(request):
    return render(request, 'app/appliances.html',{'title': 'Appliances'})

def productsNew(request):
    return render(request, 'app/productsNew.html',{'title': 'Products'})

def profile(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'app/profile.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'app/profile.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


#def item_list(request):
#    context = {
#        'items': Item.objects.all()
#    }
#    return render(request, "app/itemlist.html", context)
#def search(request):
#    return HttpResponse('it works')



