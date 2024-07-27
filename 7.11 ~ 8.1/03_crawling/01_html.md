# HTML 구조

## [1] HTML (Hyper Text Markup Language)

- 웹 페이지를 만들기 위한 언어입니다.
- HTML 문서는 요소(element)로 구성되어 있습니다.
- 각 요소는 태그(tag), 속성(attribute), 글(text)로 구성되어 있습니다.
- 태그에 따라 고유한 속성을 가지고 있습니다.

## [2] 요소(element)

### (1) 태그(tag)

- HTML의 요소는 `<태그>` 와 `</태그>` 로 감싸져 있습니다.
- 요소의 시작을 나타내는 태그는`여는 태그 <태그>` 끝을 나타내는 태그는`닫는 태그 </태그>` 입니다.

```html
<p>p 태그는 문단을 의미합니다. </p>
<h1> h1 태그는 헤더(제목)을 의미합니다. </h1>
```

### (2) 속성(attribute)

- 태그에 대한 추가 정보를 정의할 수 있습니다.

```html
<a href="http://www.naver.com/"> a 태그는 href 속성으로 이동할 링크를 정의합니다.</a>
<img src="https://www.iana.org/_img/2022/iana-logo-header.svg"/>
```

### (3) 공통 속성(attribute)

- 클래스(class)
    - 모든 요소에 적용되는 속성이며 요소에 스타일 적용을 위한 이름을 지정합니다.
- 아이디(id)
    - 고유 식별자(Identification)를 지정합니다.
    - 각 요소마다 고유한 id를 가져야합니다.

### (4) 주석

- HTML 문서내에 주석을 작성할 수 있습니다.
- `<!-- 주석 내용 -->`

## [3] 주요 요소

`<p>문단</p>`

- 문단을 나타냅니다.

`<div></div>`

- HTML 문서의 구역을 정의하는데 사용합니다.
- div 태그를 활용하여 구역을 나누고, 내부에 다른 태그를 작성해서 문서를 만들어 나갑니다.

`<a href=”이동 링크”> </a>`

- href 속성을 가지며 링크를 나타냅니다.

`<img src=”이미지 파일 경로”>`

- src 속성을 가지며 이미지를 나타냅니다.
- 닫는 태그가 필요하지 않습니다.

`<button>버튼</button>`

- 사용자가 클릭할 수 있는 버튼

`<form> </form>` 과 `<input>`

- 사용자에게 정보를 입력 받고, 해당 정보를 서버로 제출합니다.

```html
<form>
    <input type="text" placeholder="이름을 입력하세요">
    <input type="email" placeholder="이메일을 입력하세요.">
    <input type="number" placeholder="나이를 입력하세요.">
    <button type="submit">정보 제출</button>
</form>
```

# 요청(request)과 응답(response)

## [1] HTTP 프로토콜(Protocol)

- HTTP 프로토콜은 사용자와 웹 서버가 서로 대화하기 위한 하나의 약속입니다.
- 사용자가 웹 브라우저에서 주소를 입력한다는 것은 해당 주소의 서버에게 웹 페이지를 `요청(request)` 을 보낸 것입니다.
- 서버가 서버의 주소를 입력한 사용자에게 웹 페이지를 제공 하는 건 서버가 사용자에게 웹 페이지로 `응답(response)` 을 보낸 것입니다.

### (1) HTTP 상태 코드

- 사용자가 서버에 요청을 보낸 후 서버가 응답으로 보내는 3자리 숫자입니다.
- 이 3자리 숫자는 요청이 어떻게 처리 됐는지 나타내는 `상태 코드` 입니다.
- 상태 코드 예시
    - `200 : 요청을 성공적으로 처리`
    - 400 : 잘못된 요청
    - 404 : 요청한 결과물을 찾을 수 없음
    - 500 : 서버 오류 발생

## [2] requests

### (1) requests 란?

- **Requests** is an elegant and simple HTTP library for Python, built for human beings.
- `requests` 라이브러리는 개발자가 간편하고, 효율적으로 `HTTP 프로토콜`을 처리할 수 있게 도와주는 도구입니다.

### (2) HTTP 요청

`get(주소)` 메서드

- 특정 주소에 대해 HTTP 요청을 보내고 응답을 받습니다.

```python
import requests

response = requests.get('https://example.com')

print(response)
print(type(response))
```

```bash
<Response [200]>
<class 'requests.models.Response'>
```

### (3) HTTP 요청 상태 코드 확인

`status_code` 속성

- HTTP 요청에 대한 응답 상태 코드를 반환합니다.
- 반환 값은 정수형입니다.

```python
import requests

response = requests.get('https://example.com')
status_code = response.status_code

print(status_code)
print(type(status_code))
```

```bash
200
<class 'int'>
```

### (4) 상태 코드 맞춤 코드 제어

- 조건문을 사용해서 상태 코드에 따른 코드를 나눠서 작성할 수 있습니다.

```python
import requests

response = requests.get('https://example.com')
status_code = response.status_code

if status_code == 200:
    print('정상적인 요청입니다.')
else:
    print('비정상적인 요청입니다.')
```

```bash
정상적인 요청입니다.
```

### (5)  HTML 문서 출력

`text` 속성

- HTTP 요청에 대한 응답의 본문을 반환합니다.

```python
import requests

response = requests.get('https://example.com')
status_code = response.status_code

if status_code == 200:
    print(response.text)
else:
    print('비정상적인 요청입니다.')
```

```html
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>

```