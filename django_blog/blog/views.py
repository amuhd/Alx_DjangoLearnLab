from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


# Registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Profile view
@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')


from .forms import CustomUserCreationForm, CommentForm  # Import the custom form

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'  # Specify the template
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'form': form, 'post': post})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        post_id = comment.post.id
        comment.delete()
        return redirect('post-detail', pk=post_id)
    return render(request, 'blog/delete_comment.html', {'comment': comment})

from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/comment_form.html'  # Create this template

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the comment author to the logged-in user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()  # Redirect to the related post after creation

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/comment_form.html'  # Use the same template for editing

    def get_queryset(self):
        # Ensure that users can only edit their own comments
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return self.object.post.get_absolute_url()  # Redirect to the related post after editing

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'  # Create this template

    def get_queryset(self):
        # Ensure that users can only delete their own comments
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return self.object.post.get_absolute_url()  # Redirect to the related post after deletion

from django.db.models import Q
from django.shortcuts import render
from .models import Post

def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'search_results.html', {'results': results})

from django.shortcuts import render, get_object_or_404
from .models import Tag, Post

def TagView(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = tag.posts.all()  # Retrieve all posts associated with this tag
    return render(request, 'blog/tag_detail.html', {'tag': tag, 'posts': posts})
