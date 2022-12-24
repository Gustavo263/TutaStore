from django.shortcuts import get_object_or_404, render

from store.models import *


def book_list(request):
    book = Product.objects.all()
    livro = Product.objects.all()
    return render(request, "store/book.html", {"book": book, "livro": livro})
