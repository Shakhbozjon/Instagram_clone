from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from accounts.models import Profile
from .forms import PostCreateForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Post, Likes


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'index.html'


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'index.html', {'profiles': profiles})



# class PostListView(View):
#     template_name = 'index.html'
#
#     def get(self, request, *arga, **kwargs):
#         all_posts = Post.objects.all()
#
#         context = {
#             'all_posts': all_posts
#         }
#
#         return render(request, self.template_name, context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'registration/post_detail.html'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'summary', 'body', 'photo',)
    template_name = 'registration/post_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'registration/post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'registration/post_new.html'
    fields = ('picture', 'caption', 'user')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser


@login_required
def index(request):
    user = request.user
    user = request.user
    all_users = User.objects.all()

    profile = Profile.objects.all()


    context = {
        'profile': profile,
        'all_users': all_users,
    }
    return render(request, 'index.html', context)


@login_required
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()
    # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    return HttpResponseRedirect(reverse('post-details', args=[post_id]))










