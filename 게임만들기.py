import turtle as t      # turtle 패키지란? 파이썬에서 기본 제공하는 모듈 코드에 따라 그림을 그려준다 as t turtle 대신 t를 사용
import random       # random 패키지란? 랜덤 숫자를 생성 뿐만 아니라 다양한 랜덤 관련 함수 제공

def com_choice():
    rand_choice = random.randint(0, 2)      # randint()함수는 인자로 들어온 a, b 사이의 랜덤한 정수(int)를 반환합니다.
    com.shape(images[rand_choice])      # shape() 이미지설정 함수  choice()리스트 형태, 튜플 형태, 딕셔너리 형태의 자료형에서 선언한 데이터 값을 random하게 골라 한개를 반환한다.
    return com_list[rand_choice]        # return  수식을 계산해서 그 결과값을 돌려주는 것

def result_print(user_c, com_c):
    global user_score, com_score        # 함수 안의 지역변수를 함수 바깥의 영역에서는 호출하여 사용할 수 없기 때문에 전역변수인 global 사용
    t.clear()       # 그림을 지워주는 함수
    t.goto(0, -100)         # 괄호안에 이동하고 하는 곳의 x,y 좌표를 넣으면 된다.
    if user_c == com_c:
        t.write("무승부", False, "center", ("", 50))       # turtle 위치에 문자열 출력
    elif winning_case[user_c] == com_c:
        user_score += 1
        user_pen.clear()            # 그림을 지워주는 함수
        user_pen.write(user_score, False, "center", ("", 50))
        t.write("승", False, "center", ("", 50))         # turtle 위치에 문자열 출력
    else:
        com_score += 1
        com_pen.clear()         # 그림을 지워주는 함수
        com_pen.write(com_score, False, "center", ("", 50))
        t.write("패", False, "center", ("", 50))

def rock(x, y):
    user.shape(rock_gif)        # shape() 이미지설정 함수
    com = com_choice()          # choice()리스트 형태, 튜플 형태, 딕셔너리 형태의 자료형에서 선언한 데이터 값을 random하게 골라 한개를 반환한다.
    result_print("rock", com)

def scissors(x, y):
    user.shape(scissors_gif)        # shape() 이미지설정 함수
    com = com_choice()              # choice()리스트 형태, 튜플 형태, 딕셔너리 형태의 자료형에서 선언한 데이터 값을 random하게 골라 한개를 반환한다.
    result_print("scissors", com)

def paper(x, y):
    user.shape(paper_gif)       # shape() 이미지설정 함수
    com = com_choice()          # choice()리스트 형태, 튜플 형태, 딕셔너리 형태의 자료형에서 선언한 데이터 값을 random하게 골라 한개를 반환한다.
    result_print("paper", com)

# 기본 설정
t.bgcolor("sky blue")  # 배경 색깔 설정 함수
t.title("가위바위보 게임")     # 제목 함수
t.ht()     # pen.ht() pen이 보이지 않게 설정하는 함수
t.up()      # pen.up() 좌표를 이동할때 pen이 그어지지 않도록 펜을 들어올린다는 명령어

rock_gif = "D:/work/게임/py/rock.gif"
scissors_gif = "D:/work/게임/py/scissors.gif"
paper_gif = "D:/work/게임/py/paper.gif"
t.addshape(rock_gif)        # 랜덤값에 추가 # 대부분의 경우 PNG는 GIF보다 압축률이 더 높다. GIF의 단색 투명층과 달리 8비트 알파 채널을 이용한 투명층을 지원한다. 256색을 지원하는 GIF와 달리 트루 컬러를 지원한다. GIF에서는 제공되는 애니메이션을 PNG는 지원하는 않는다.
t.addshape(scissors_gif)        # 랜덤값에 추가
t.addshape(paper_gif)       # 랜덤값에 추가

images = [rock_gif, scissors_gif, paper_gif]
com_list = ["rock", "scissors", "paper"]
winning_case = {"rock" : "scissors", "scissors" : "paper", "paper" : "rock"}
user_score = 0
com_score = 0

# 나의 선택 이미지
user = t.Turtle()
user.up()           # pen.up() 좌표를 이동할때 pen이 그어지지 않도록 펜을 들어올린다는 명령어
user.speed(0)           # 그림이 그려지는 속도가 1~10 이지만 10 이상일때 0으로 표시 따라서 0은 최고속도
user.goto(-200, 200)        # 괄호안에 이동하고 하는 곳의 x,y 좌표를 넣으면 된다.
user.write("나의 선택", False, "center", ("", 30))
user.goto(-200, -100)       # 괄호안에 이동하고 하는 곳의 x,y 좌표를 넣으면 된다.
user.shape(rock_gif)        # shape() 이미지설정 함수

# 컴퓨터 선택 이미지
com = t.Turtle()        # turtle.pen 은 기본값이 화면중앙에 위치하고, 오른쪽 방향을 가르킨다. 따라서 다른위치나 방향을 지정해야한다.
com.up()            # pen.up() 좌표를 이동할때 pen이 그어지지 않도록 펜을 들어올린다는 명령어
com.speed(0)             # 그림이 그려지는 속도가 1~10 이지만 10 이상일때 0으로 표시 따라서 0은 최고속도
com.goto(200, 200)      # 괄호안에 이동하고 하는 곳의 x,y 좌표를 넣으면 된다.
com.write("컴퓨터 선택", False, "center", ("", 30))
com.goto(200, -100)     # 괄호안에 이동하고 하는 곳의 x,y 좌표를 넣으면 된다.
com.shape(rock_gif)     # shape() 이미지설정 함수

# 유저 점수 판
user_pen = t.Turtle()
user_pen.ht()       # pen.ht() pen이 보이지 않게 설정하는 함수
user_pen.up()       # pen.up() 좌표를 이동할때 pen이 그어지지 않도록 펜을 들어올린다는 명령어
user_pen.goto(-200, 100)        # 괄호안에 이동하고 하는 곳의 x,y 좌표를 넣으면 된다.
user_pen.write(user_score, False, "center", ("", 60))

# 컴퓨터 점수 판
com_pen = t.Turtle()
com_pen.ht()        # pen.ht() pen이 보이지 않게 설정하는 함수
com_pen.up()        # pen.up() 좌표를 이동할때 pen이 그어지지 않도록 펜을 들어올린다는 명령어
com_pen.goto(200, 100)      # 괄호안에 이동하고 하는 곳의 x,y 좌표를 넣으면 된다.
com_pen.write(com_score, False, "center", ("", 60))         # write()함수를 통해 출력 하고싶은 문자열과 크기를 지정


t.onscreenclick(rock, 1) # 마우스 좌 클릭
t.onscreenclick(scissors, 2) # 마우스 스크롤 클릭
t.onscreenclick(paper, 3) # 마우스 우 클릭

t.done()        # done() 프로그램 종료
