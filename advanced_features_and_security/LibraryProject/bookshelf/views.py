from .forms import ExampleForm
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import journal,Post
from .forms import SearchForm 
from .models import Book
def book_search(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.none()  # start with an empty QuerySet

    if form.is_valid():
        query = form.cleaned_data.get('query')
        # Use Django's ORM which parameterizes queries and mitigates SQL injection risks
        books = Book.objects.filter(title__icontains=query)

    return render(request, 'bookshelf/book_list.html', {
        'form': form,
        'books': books,

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
@permission_required('yourapp.can_view', raise_exception=True)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

@permission_required('yourapp.can_create', raise_exception=True)
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'posts/create.html')

@permission_required('yourapp.can_edit', raise_exception=True)
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_list')
    return render(request, 'posts/edit.html', {'post': post})

@permission_required('yourapp.can_delete', raise_exception=True)
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')
@permission_required('bookshelf.can_view', raise_exception=True)
def article_list(request):
    journal = journal.objects.all()
    return render(request, 'bookshelf/journal_list.html', {'journal': journals})
@permission_required('bookshelf.can_create', raise_exception=True)
def journal_create(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'bookshelf/journal_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def journals_edit(request, journal_id):
    article = get_object_or_404(journal, id=journal_id)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'app_name/journal_form.html', {'journal':journal})

@permission_required('bookshelf.can_delete', raise_exception=True)
def journal_delete(request, journal_id):
    journal = get_object_or_404(journal, id=journal_id)
    journal.delete()
    return redirect('journal_list')
