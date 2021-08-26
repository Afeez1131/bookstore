from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .forms import SearchForm
from .models import Book

# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "book/book_list.html"
    context_object_name = 'books'
    login_url = "account_login"
    # permissions


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'


class SearchResultView(ListView):
    model = Book
    context_object_name = 'search_result_list'
    template_name = 'books/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query != '':
            queryset = Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query))
            print(type(queryset))

            return queryset
