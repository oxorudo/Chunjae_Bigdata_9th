# ***kwargs는 특정 키의 값을 같이 전달한다.
def my_function(**kwargs):
    print(kwargs.get("first"), kwargs.get("mid"), kwargs.get("last"))

my_function(first="k", mid="t", last="k")
