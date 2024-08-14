from django.urls import path
from catalog import views

# url 선언 목록
# url을 받아서 필요한 처리를 해주기 위해서는
# urls.py에 반드시 urlpatterns라는 리스트가 필요하다.
# path에 이름을 지정하면 <a href="{%url 'index' %}">Home</a> 형태로 지정 가능
urlpatterns = [
    # /catalog/ > 함수로 지정
    path("", views.index, name='index'),
    # /catalog/books/ > 클래스로 생성
    path('books/', views.BookListView.as_view(), name='books'),
    # /catalog/book/??? > 클래스로 생성
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # /catalog/authors > 클래스로 생성
    path('authors/', views.AuthorListView.as_view(), name="authors"),
    # /catalog/author/??? > 클래스로 생성
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),

    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),

    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),

    path('borrowed/', views.LoanedBookListViewForStaff.as_view(), name='all-borrowed'),
]