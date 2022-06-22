# Python-prac
## 가상환경(venv)
독립적인 Python 개발 가상환경을 의미한다. 모듈 간의 버전 문제로 인해 새로운 모듈이 설치되지 않거나 설치되더라도 이전 코드가 작동하지 않을 수 있다. 가상환경은 이러한 모듈 관련 문제를 방지할 수 있다.

## 가상환경 구축
- python -m venv "가상환경 이름"
명령어를 실행하면 가상환경 이름으로 폴더가 생성된다. 처음 가상환경을 구축하면 어떠한 모듈도 설치되어 있지 않으며 가상환경 삭제는 간단히 폴더만 삭제하면 된다.

## 플라스크(Flask)
- pip install flask
노드에 익스프레스 자바의 스프링이 존재한다. Python 프레임워크는 대표적으로 장고와 플라스크가 있다. 플라스크는 확장성이 좋다. 마이크로 프레임워크이며 짦은 코드로 완성도 있는 프로그램을 만들 수 있다. 단독 웹 서버로도 사용되긴 하지만 언어 특성상 이미지 동영상 AI 처리를 별도로 처리하는 상황에 많이 사용한다. 스프링 서버에서 플라스크 서버로 데이터를 전송하여 플라스크 서버에서 처리 후 다시 스프링 서버로 돌려주는 방식이다.

## template
보통 Jinja2 템플릿을 사용한다. Jinja2는 서버 사이드 랜더링(SSR)이며 서버에서 화면을 내려준다. 그 화면에서 변수와 반복문 조건문 등을 사용할 수 있다.

## static 
static 폴더 생성 후 정적 파일(css/js) 설정 방법(2가지)

1.
<<<<<<< HEAD
"<link rel="stylesheet" href="{{ url_for("static", filename="css/style.css") }}">"  
"<script src="{{ url_for("static", filename="js/main.js") }}"></script>"  
 
2.
# <link rel="stylesheet" href="/static/css/style.css">"  
=======
"<link rel="stylesheet" href="{{ url_for("static", filename="css/style.css") }}">"
<script src="{{ url_for("static", filename="js/main.js") }}"></script>

2.
"<link rel="stylesheet" href="/static/css/style.css">"
>>>>>>> master

2번 방법으로 불러올 시 호스팅 서비스별로 충돌이 발생 할 가능성이 있다고 한다. Python에서 권장하는 방법인 url_for 키워드를 통해서 정적 파일을 불러와야한다.

## 폼 데이터
네임값을 request.args.methods("네임속성")받는다.

## global
app.py 상단 변수 선언 후 라우터 안 global "변수명"으로 사용한다.


