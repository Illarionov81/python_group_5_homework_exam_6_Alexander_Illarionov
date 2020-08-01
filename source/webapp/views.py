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
            guest = GuestBook.objects.create(name=name, email=email, text=text)
            return redirect('index')
        else:
            return render(request, 'note_create.html', context={'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])



# def product_delete_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         return render(request, 'product_delete.html', context={'product': product})
#     elif request.method == 'POST':
#         product.delete()
#         return redirect("index")
#
#
# def product_update_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == "GET":
#         form = ProductForm(data={
#             'name': product.name,
#             'category': product.category,
#             'description': product.description,
#             'amount': product.amount,
#             'price': product.price
#         })
#         return render(request, 'product_update.html', context={'form': form, 'product': product})
#     elif request.method == 'POST':
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             product.name = form.cleaned_data['name']
#             product.category = form.cleaned_data['category']
#             product.description = form.cleaned_data['description']
#             product.amount = form.cleaned_data['amount']
#             product.price = form.cleaned_data['price']
#             product.save()
#             return redirect('product_view', pk=product.pk)
#         else:
#             return render(request, 'product_update.html', context={'product': product, 'form': form})
#     else:
#         return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
#
#
