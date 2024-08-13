from django.db import models
from django.urls import reverse
# uuid : 랜덤값을 만들어 냄.
import uuid
from django.conf import settings
from datetime import date

# Create your models here.
# ORM을 위한 객체를 정의하는 곳이다.
# 클래스 == 테이블, 변수 == 열

class Genre(models.Model):
    # CharField = varchar(200)
    name = models.CharField(max_length=200, help_text = 'Enter a book genre(e.g. Science Fiction)')

    # print(genre) 이렇게 했을 때 
    # genre.name이 출력되도록 함.
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    # ForeignKey 옵션은 외부 테이블과의 연관 관계를 나타낸다.
    # on_delete는 해당 열과 관련된 열의 값이 지워졌을 때 해당 열 값을 어떻게 처리할 것인지 정하는 것이다.
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of th book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    # admin 화면에서 genre를 보여주기 위한 커스텀 필드(열)
    # genre 필드는 ManyToManyField이기 때문에 list_display에 직접적으로 특정할 수 없다.
    # (거대한 데이터베이스 접근 "비용"이 발생할 수 있기 때문에 장고는 이것을 방지).
    def display_genre(self):
        # data = []
        # for genre in self.genre.all():
        #   data += genre.name

        # return '. '.join(data[:3])
        # 위의 코드와 같음.
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = "Genre"
    


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True) # blank : 빈 값을 허용할 것인가?
    # AUTH_USER_MODEL : django에서 기본으로 제공하는 유저 모델
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    # 공통코드
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    # choices로 인해 m, o, a, r 중에 하나만 허용.
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (('can_mark_returned', 'Set book as returned'),)

    def __str__(self):
        return f'{self.id} ({self.book.title})'
    
    @property
    def is_overdue(self):
        return bool(self.due_back and date.today() > self.due_back)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    

