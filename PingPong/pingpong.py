import turtle

### 화면에 아이템의 초기 이미지 그리기 ###
## 게임 화면창 그리기
# 화면창 크기
src_width = 800
src_height = 600

# 화면창 그리기
scr = turtle.Screen()
scr.title("Ping Pong")
scr.bgcolor("black")
scr.setup(width=src_width, height=src_height)
scr.tracer(0) # 화면의 tracing을 안하겠다

## 핑퐁 바 그리기
# 키보드 입력에 의한 핑퐁바 이동 픽셀
bar_mov_pixel = 20

# 핑퐁바와 좌우벽의 간격
bar_gab = 50

# 핑퐁바 폭
bar_width = 4

# 왼쪽 바
bar_a = turtle.Turtle()
bar_a.speed(0)
bar_a.shape("square")
# 점을 늘려서 바로 만들기
bar_a.shapesize(stretch_wid=bar_width, stretch_len=1)
bar_a.color("white")
bar_a.penup()
bar_a.goto(-(src_width/2 - bar_gab), 0) # -350

#오른쪽 바
bar_b = turtle.Turtle()
bar_b.speed(0)
bar_b.shape("square")
bar_b.shapesize(stretch_wid=bar_width, stretch_len=1)
bar_b.color("white")
bar_b.penup()
bar_b.goto((src_width/2 - bar_gab), 0) # 350

#핑퐁 볼 이동 xy 픽셀
ball_mov_pixel = 2

# 핑퐁 볼 반지름, 핑퐁 바의 두께의 반
dot_radius = 10

# 핑퐁 볼 그리기
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup() #이동하는 선을 그리지 않는다
ball.goto(0, 0)
ball.dx = ball_mov_pixel
ball.dy = ball_mov_pixel

## 점수판 그리기
# 점수
score_a = 0
score_b = 0

### 키보드 입력받고, 핑퐁 바 움직이기 ###

while True:
    ## 화면의 변화 업데이트 해주기 ##
    scr.update()
    # 핑퐁 볼 을 대각선으로 움직이기
    # 볼이 위 아래 벽에 부딪히면 튕기기
    # 볼이 좌우 벽에 도달하면 점수를 세고 볼을 가운데로 옮기기
    # 볼이 핑퐁 바에 부딪혔을 경우 튕기기
