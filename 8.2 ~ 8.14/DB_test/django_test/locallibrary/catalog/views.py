from typing import Any
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
# URL을 받아서 실제 뷰를 생성한다.

# index라고 하는 함수나 클래스가 필요함.


# 플라스크의 다음 함수와 같다.
# @app.route("@@")
# def aaa():
#     return render_template()

def index(request):

    # ?keyword=keyword 받을 수 있게 해야한다.
    keyword = request.GET.get('keyword')
    
    # 세션을 가져오는 방법
    # request.session.get('my_session')

    # 방문자 수
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits +1
    
    # Django ORM
    # == SELECT COUNT(1) FROM BOOK
    num_books = Book.objects.all().count() 
    num_instances = BookInstance.objects.all().count()
    # SELECT COUNT(1) FROM BookInstance WHERE status = 'a'
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_includes_keywords = Book.objects.filter(title__exact=keyword).count()

    # all()은 생략 가능
    num_authors = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
        'num_includes_keywords' : num_includes_keywords,
        'num_visits' : num_visits,
    }


    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    #  template 안에서 [model]_list 형태로 보여지게 된다.
    model = Book
    
    # 한 페이지에 5권까지 보이고 나머지는 다음 페이지로 가도록 페이징
    paginate_by = 5
    
    # context_object_name > 함수 view의 context와 같다.
    # context_object_name = 'book_list'
    
    # 모델이 보여지는 방식을 지정
    # queryset = Book.objects.all()[:5]

    # queryset은 다음과 같이 지정할 수도 있다.
    # def get_queryset(self):
    #     return Book.objects.all()[:5]
    
    template_name = "books"

    # context=context, context에 리턴할 데이터가 많을 경우
    # 다음 함수를 오버라이드 해서 필요한 데이터를 추가로 넣어줄 수도 있다.
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just data'
        return context
    


# 클래스 기반의 디테일 뷰
class BookDetailView(generic.DetailView):
    model = Book

# 디테일 뷰를 함수로 변경했을 경우 다음과 같이 표현됩니다.
# def book_detail_view(request, pk):
#     try:
#         book= Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         raise Http404('Book does not exist')

#     # 리버스 검색
#     # forign key 가 달려있지 않은 곳에서 연결된 리스트를 찾아주는 함수
#     book_instances = book.BookInstance_set.all()

#     return render(request, 'catalog/book_detail.html', context={'Book': book})

# author_list
class AuthorListView(generic.ListView):
    model = Author

    template_name = 'authors'

# author_detail
class AuthorDetailView(generic.DetailView):
    model = Author