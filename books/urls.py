from django.urls import path

from .views import BookDetailView, BookListView, SearchResultView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('detail/<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultView.as_view(), name='search_results'),
]
