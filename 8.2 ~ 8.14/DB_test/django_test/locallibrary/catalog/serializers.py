from rest_framework import serializers
from catalog.models import Book, BookInstance


# class를 웹이 이해할 수 있게 JSON이나 XML형태로 쉽게 변환할 수 있게 해주는 기능
# serializer가 자동으로 D.D형태로 만들어주는 것
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields='__all__' # 모든 필드 포함

# 책 카피본 목록을 D.D로 변환
class BookInstSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields='__all__' # 모든 필드 포함