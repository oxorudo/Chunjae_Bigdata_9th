import requests

response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')

print(response.json())

'''
.com 까지 : 사이트주소
/facts/random? : uri(요청 주소, 요청 시 정보)
'''