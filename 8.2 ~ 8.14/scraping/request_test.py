import requests
from bs4 import BeautifulSoup


# TODO 로그인이 가능하도록 만들자 > 세션 이용
url = "http://127.0.0.1:8000/catalog/books/"

# 세션을 가져온다.
with requests.Session() as session:
    # form을 넣고 데이터를 전송
    form = {
        "username" : 'xorud',
        'password' : 'xorud',
        'csrfmiddlewaretoken' : 'mUdkPjUSS82oczj8OpqqcBjiGCxRtWO5I72vDUmxakkrEXg4HlZIIKUylIpBe61c'
    }
    
    cookies = {
        'csrftoken' : 'wnZlYLCPsmsdCy7636JsGjLqPg2UVknh'
    }

    # 로그인
    response = session.post("http://127.0.0.1:8000/accounts/login/", data=form, cookies=cookies) 
    
    response = session.get(url)
    
    # 페이지를 가져옴
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # page 1 of 2.를 가져옴.
    page = soup.select_one('.page-current > p')
    
    # string을 잘라보자.
    total_page = int(page.text.split('of')[1].strip()[0]) # 페이지 갯수(int)
    
    # total_page 만큼 반복하여 순회할 필요가 있다.

    # D.D에 저장 [{name : "", author : ""}]
    result = []
    for i in range(1, total_page+1):
        # url = "http://127.0.0.1:8000/catalog/books/?page="
        book_res = session.get(url, params={'page' : i}).text # params : 파라미터로 만들어 준다.
        books_html = BeautifulSoup(book_res, 'html.parser')
        li_list = books_html.select('div.col-sm-10 > ul > li')
        for li in li_list:
            # str 자르고 나누고..
            books = li.text.strip().split('  ')
            # print(books)
            result.append({'name' : books[0].strip(), "author" : books[1].strip()})
    print(result)






# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')

# # div class=row 아래의 div class=col-sm-10 아래의 ul을 찾음
# ul = soup.select_one('.row > .col-sm-10 > ul')

# li = ul.select("li")

# for tag in li:
#     print(tag.text.strip()) # strip : 공백제거
