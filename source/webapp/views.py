from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import GuestBook, STATUS_CHOICES
from webapp.forms import GuestBookForm
from django.http import HttpResponseNotAllowed


def index_view(request):
    goests_list = GuestBook.objects.filter(status='active').order_by('-created_time')
    return render(request, 'index.html', context={
        'goests_list': goests_list
    })


def note_create_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'note_create.html', context={
            'form': GuestBookForm()
        })
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            GuestBook.objects.create(name=name, email=email, text=text)
            return redirect('index')
        else:
            return render(request, 'note_create.html', context={'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def note_update_view(request, pk):
    note = get_object_or_404(GuestBook, pk=pk)
    if request.method == "GET":
        form = GuestBookForm(data={
            'name': note.name,
            'email': note.email,
            'text': note.text,
        })
        return render(request, 'note_update.html', context={'form': form, 'note': note})
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            note.name = form.cleaned_data['name']
            note.email = form.cleaned_data['email']
            note.text = form.cleaned_data['text']
            note.save()
            return redirect('index')
        else:
            return render(request, 'note_update.html', context={'form': form, 'note': note})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def note_delete_view(request, pk):
    note = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'note_delete.html', context={'note': note})
    elif request.method == 'POST':
        note.delete()
        return redirect("index")

