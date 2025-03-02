from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import journal

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
