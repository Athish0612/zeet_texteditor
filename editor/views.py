from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponse
from .models import Document
from .forms import DocumentForm


# View to display a list of user's documents
@login_required
def document_list(request):
    documents = Document.objects.filter(owner=request.user)
    return render(request, 'editor/document_list.html', {'documents': documents})

# View to retrieve document details as JSON
@login_required
def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk, owner=request.user)
    document_data = {
        'id': document.id,
        'title': document.title,
        'content': document.content,
    }
    return JsonResponse(document_data)

# View to handle creating a new document
@login_required
def document_new(request):
    if request.method == "POST":
        document_name = request.POST.get('document_name')
        if document_name:
            document = Document.objects.create(title=document_name, owner=request.user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid document name'})
    else:
        form = DocumentForm()
    return render(request, 'editor/document_list.html', {'form': form})

# View to handle editing an existing document
@login_required
def document_edit(request, pk):
    document = get_object_or_404(Document, pk=pk, owner=request.user)
    if request.method == "POST":
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'editor/document_edit.html', {'form': form, 'document': document})

# View to handle deleting a document
@login_required
def document_delete(request, pk):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        document_id = request.POST.get('document_id')
        try:
            document = get_object_or_404(Document, pk=document_id, owner=request.user)
            document.delete()
            return JsonResponse({'success': True})
        except Document.DoesNotExist:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})

# View to handle user registration
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('document_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# View to retrieve document details as JSON (without user authentication)
@login_required
def document_detail_json(request, pk):
    document = get_object_or_404(Document, pk=pk)
    data = {
        'title': document.title,
        'content': document.content,
    }
    return JsonResponse(data)

# View to download a document
@login_required
def download_document(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    content = document.content

    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename={document.title}.txt'

    return response

# View to handle user logout
def log_out(request):
    logout(request)
    return redirect('login')
