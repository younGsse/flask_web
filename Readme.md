# Flask로 웹 페이지 제작

## 초기설정
### venvs로 파이썬 가상환경 설정
<pre>
<code>
>> PATH> python -m venvs project
</code>
</pre>

### 가상환경 실행
<pre>
<code>
>> PATH\Scripts> activate
</code>
</pre>

### 가상 환경 내 플라스크 설치
<pre>
<code>
>> PATH\Scripts> pip install Flask
>> PATH\Scripts> python -m pip install --upgrade pip
</code>
</pre>

### Flask 실행
flask run을 입력하면 run.py를 찾아 실행하지만, 실행하는 python파일을 다른 이름으로 지정하는 경우 환경변수로 지정함.
<pre>
<code>
set FLASK_APP=pybo
set FLASK_ENV=development
flask run
</code>
</pre>

## Blue print 사용하기
라우트 함수를 구조적으로 관리할 수 있음

## DB 설정
### ORM
라이브러리 설치
<pre>
<code>
> pip install Flask-Migrate
</code>
</pre>

ORM을 이용하면 직접 쿼리문을 작성하지 않아도 데이터 베이스의 데이터를 처리
루트 경로에 config파일 추가
<pre>
<code>
import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
</code>
</pre>

초기화 파일에 전역변수로 Migrate, SQLAlchemy 선언 후
함수 내에서 초기화 선언

### DB 초기화하기
<pre>
<code>
> flask db init
</code>
</pre>

### DB 사용하기
python 코드로 컬럼을 설정한 후 2가지만 기억하자
<pre>
<code>
> flask db migrate
> flask db upgrade
</code>
</pre>
설정한 것 적용하는 것과 적용된 것을 실행하는 것

## Issue
### Issue 1.
DB에 comment와 관련된 모델을 넣을 때,
question, answer에 대해서 nullable=False 성격을 부여했는데,
question에 대한 댓글 추가시 answer_id가 None 값이고,
answer에 대한 댓글 추가시 question_id가 None 값이 부여됨.

#### Solution
생각해보니, Question에 대한 댓글은 answer_id가 Null이 가능하고,
Answer에 대한 댓글은 question_id가 Null이 가능함. nullable=True로 변경.
추가로, 댓글에 대한 수정, 삭제의 경우 파라미터 값이 comment_id로 전달된다.

### Issue 2.
새 글 등록시 제목이 내용에 써지는 상황
#### Solution
question_views.py 29 line, content=form.subject.data -> content=form.content.data