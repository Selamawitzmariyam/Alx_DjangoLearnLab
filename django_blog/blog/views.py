from django.shortcuts import render, get_object_or_404,redirect 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db import Post
from .models import  Comment
from .forms import CommentForm
from django.urls import reverse_lazy

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

def search_posts(request):
    query = request.GET.get('q', '')  # Get search query from URL
    results = Post.objects.filter(
        (title__icontains=query),
        (content__icontains=query) |
        (tags__name__icontains=query)
    ).distinct()  # Avoid duplicates

    return render(request, 'blog/search_results.html', {'query': query, 'results': results})
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Default: <app>/<model>_list.html
    context_object_name = 'posts'
    ordering = ['-published_date']  # Show newest first

# DetailView - Shows a single blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Default: <app>/<model>_detail.html

# CreateView - Allows users to add a new blog post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

# UpdateView - Allows authors to edit their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Allow only the author to edit

# DeleteView - Allows authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'  # Redirect to homepage after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    def add_comment(request, post_id):
        post = Post.objects.get(id=post_id)
    
        if request.method == 'POST':
         form = CommentForm(request.POST)
        if form.is_valid():
            # Create a new comment, linked to the post and user
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.id)  # Redirect to post detail page after submission
        else:
         form = CommentForm()

        return render(request, 'blog/add_comment.html', {'form': form, 'post': post})
class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return Comment.objects.filter(post=post)

# 📝 Add a new comment to a post (Only authenticated users)
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
            return redirect('post-detail', pk=post.id)  # Redirect to post detail page after submission
    else:
        form = CommentForm()

    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})

# ✏️ Edit a comment (Only the comment author can edit their comment)
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the comment is updated by the correct user
        return super().form_valid(form)

    def test_func(self):
        """Ensure only the comment author can edit."""
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})

# 🗑️ Delete a comment (Only the comment author can delete their comment)
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        """Ensure only the comment author can delete."""
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})
class PostListByTagView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags__in=[self.tag])