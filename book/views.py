from django.shortcuts import render, get_object_or_404

from store.models import *

def book_list(request):
    book = Product.objects.all()
    livro = Product.products.all()
    return render(request, "store/book.html", {"book": book, "livro": livro})