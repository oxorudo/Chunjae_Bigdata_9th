from django.contrib import admin

from catalog.models import Author, Book, BookInstance, Genre

# Register your models here.
# 설정을 통해서 관리자(admin) 사이트에서 우리 모델을 관리할 수 있게 해준다.
# book, bookinstance, author, genre를 여기서 C,R,U,D를 쉽게 할 수 있도록 지원

# admin 사이트에 등록
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

class BooksInline(admin.TabularInline): # 인라인 창에 책 정보 수정 기능 추가(상세 창에서 책 정보 수정 가능)
    model = Book

# admin 인터페이스에서 모델이 보여지는 방식을 바꿈.
class AuthorAdmin(admin.ModelAdmin):
    # 목록 화면에서 데이터를 보여주는 방식을 결정 : 표 형식으로 튜플의 원소들에 대응되는 데이터를 표시
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # 상세 화면에서 데이터를 보여주는 방식을 결정 : 같이 튜플로 묶인 것은 한 섹션에 묶여서 표시
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline] # 저자 상세 창에서 책 수정 기능 추가

admin.site.register(Author, AuthorAdmin) # admin 사이트에 등록


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance # 인라인 창에 책의 instance 정보 수정 기능 추가


# 다음과 같이 데코레이터를 사용해서 줄여 쓸 수도 있다.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline] # 인라인 추가 : 책의 상세 창에서 해당 책의 instance들을 수정할 수 있음


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status',  'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back') # 목록에서 필터링 기능 추가
    fieldsets = ( # 상세 창의 필드 섹션을 연관된 것들끼리 그룹화
        (None, {
            'fields' : ('book', 'imprint', 'id')
        }),
        ('Availabillity', {
            'fields' : ('status', 'due_back', 'borrower')
        })
    ) 