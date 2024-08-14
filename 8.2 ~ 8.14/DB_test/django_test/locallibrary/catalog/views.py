from typing import Any
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import datetime
from django.urls import reverse, reverse_lazy
from catalog.forms import RenewBookForm
from django.contrib.auth.decorators import permission_required, login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Author, Book, BookInstance
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer, BookInstSerializer

# Create your views here.
# URL을 받아서 실제 뷰를 생성한다.

# index라고 하는 함수나 클래스가 필요함.


# 플라스크의 다음 함수와 같다.
# @app.route("@@")
# def aaa():
#     return render_template()

# 함수형 뷰에서 로그인 정보를 체크하는 방법
# @login_required
def index(request):

    # ?keyword=keyword 받을 수 있게 해야한다.
    keyword = request.GET.get('keyword')
    
    # 유저가 로그인되었는지 확인하기
    # request.user.is_authenticated
    
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


# LoginRequiredMixin : 이 클래스를 상속하면 로그인이 필요해진다.
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


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )
    

@login_required
@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':

    # Create a form instance and populate it with data from the request (binding):
    # 폼을 생성하고 요청을 받아옴
        form = RenewBookForm(request.POST)

    # Check if the form is valid:
    # 통과가 되었다면 데이터베이스에 데이터 저장
        if form.is_valid():
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

        # redirect to a new URL:
        # 대여 책 목록으로 이동
            return HttpResponseRedirect(reverse('books'))

        # If this is a GET (or any other method) create the default form.
    else:
        # form에 기본값을 넣어준다.
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }
    # get 요청일때만 책 대여기간 연장 폼으로 이동
    return render(request, 'catalog/book_renew_librarian.html', context)

class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial={'date_of_death' : '05/01/2018',}
    permission_required = 'catalog.add_author'

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = '__all__'
    permission_required = 'catalog.change_author'

class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.delete_author'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return reverse('author-delete', kwargs={'pk': self.object.pk})
            


class LoanedBookListViewForStaff(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = BookInstance

    def get_queryset(self):
        return (
            # borrower가 null이면 안 된다.
            # status가 o 여야 한다.
        BookInstance.objects
        .filter(borrower__isnull=False)
        .filter(status__exact='o')
        .order_by('due_back')
    )
    
    # 관리자 유저일때만 접근 권한 부여
    permission_required = 'user.is_staff'

# API를 리턴하기 위해서는 APIView를 상속받아야 한다.
class BookListAPIView(APIView):
    # 상속 받았으면 get 메소드를 구현해야 한다.
    # get 함수 : 실제 검색어에 맞는 데이터를 리턴함.
    def get(self, request):
        # 데이터를 쿼리
        books = Book.objects.all()
        # 시리얼라이징
        serializer = BookSerializer(books, many=True)
        # response 형태로 리턴
        return Response(serializer.data)
    
    # post 함수 : 받아온 데이터를 실제 데이터베이스에 적용
    def post(self, request):
        # request.data > 폼 데이터 안에 있는 데이터를 Model로 변경해 준다.
        serializer = BookSerializer(data=request.data)
        # 포맷을 통과했을 때
        if serializer.is_valid():
            # Book 형태로 데이터가 변환이 되었으므로, Book을 저장
            serializer.save()

        return Response(serializer.data)


# 실습
# Book_instance가 있는데, Book_id를 가져와서 id에 해당하는 Book_instance의 
# 리스트를 가져오도록 하자.
# 검색할때는 뒤에 ?book_id=id를 붙여서 접속하자.
class BookInstanceAPIView(APIView):

    def get(self, request):
        book_id = request.GET['book_id']
        inst = BookInstance.objects.filter(book__id__exact = book_id)

        serializer = BookInstSerializer(inst, many=True)
        return Response(serializer.data)
        