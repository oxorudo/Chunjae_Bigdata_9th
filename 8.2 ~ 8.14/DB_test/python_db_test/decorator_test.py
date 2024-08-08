# 데코레이터는 함수를 매개변수로 받아 와서 그 함수를 꾸며준다.
def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before 함수의 실행", args, kwargs)
        return_value = func(*args, **kwargs) # 여기서 sum_to_numbers 함수가 실행되고, 결괏값이 return_value에 담긴다.
        print("after 함수의 실행", return_value)

        return return_value

    return inner1

@hello_decorator
def sum_to_numbers(a,b):
    print("함수 실행 중")
    return a+b

print("두 수의 합 : ", sum_to_numbers(3,5))
