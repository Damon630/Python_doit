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
scr.tracer(0)  # 화면의 tracing을 안하겠다

## 핑퐁 바 그리기
# 키보드 입력에 의한 핑퐁바 이동 픽셀
bar_mov_pixel = 20

# 핑퐁바와 좌우벽의 간격
bar_gab = 50

# 핑퐁바 폭
bar_width = 4


# 핑퐁 바 그리는 함수
def draw_bar(pos):
    bar = turtle.Turtle()
    bar.speed(0)
    bar.shape("square")
    bar.shapesize(stretch_wid=bar_width, stretch_len=1)
    bar.color("white")
    bar.penup()
    bar.goto(pos, 0)
    return bar


# 왼쪽 바
bar_a = draw_bar(-(src_width / 2 - bar_gab))

# 오른쪽 바
bar_b = draw_bar((src_width / 2 - bar_gab))

# 핑퐁 볼 이동 xy 픽셀
ball_mov_pixel = 2

# 핑퐁 볼 반지름, 핑퐁 바의 두께의 반
dot_radius = 10

# 핑퐁 볼 그리기
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()  # 이동하는 선을 그리지 않는다
ball.goto(0, 0)
ball.dx = ball_mov_pixel
ball.dy = ball_mov_pixel

## 점수판 그리기
# 점수
score_a = 0
score_b = 0


### 키보드 입력받고, 핑퐁 바 움직이기 ###
## 핑퐁 바 움직이기
def move_bar_a_up():
    bar_a.sety(bar_a.ycor() + bar_mov_pixel)  # 위로 20px

def move_bar_a_down():
    bar_a.sety(bar_a.ycor() - bar_mov_pixel)  # 아래로 20px

def move_bar_b_up():
    bar_b.sety(bar_b.ycor() + bar_mov_pixel)  # 위로 20px

def move_bar_b_down():
    bar_b.sety(bar_b.ycor() - bar_mov_pixel)  # 아래로 20px

## 키보드 입력받기
scr.listen()
scr.onkeypress(move_bar_a_up, "w")
scr.onkeypress(move_bar_a_down, "s")
scr.onkeypress(move_bar_b_up, "Up")
scr.onkeypress(move_bar_b_down, "Down")

while True:
    ## 화면의 변화 업데이트 해주기 ##
    scr.update()

    # 핑퐁 볼 을 대각선으로 움직이기
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # 볼이 위 아래 벽에 부딪히면 튕기기
    y_pos = src_height/2 - dot_radius
    x_pos = src_width/2 - dot_radius

    # 위벽
    if ball.ycor() > y_pos:
        ball.sety(y_pos)
        ball.dy *= -1
    # 아래벽
    if ball.ycor() < -y_pos:
        ball.sety(-y_pos)
        ball.dy *= -1

    # 볼이 좌우 벽에 도달했을 경우 가운데로 이동하고, x축 이동방향 전환
    # 왼쪽 벽
    if ball.xcor() > x_pos:
        ball.goto(0, 0)
        ball.dx *= -1

    # 오른쪽 벽
    if ball.xcor() > -x_pos:
        ball.goto(0, 0)
        ball.dx *= -1

    # bar_b 볼을 튕기기
    # 400 - 50(바와 벽의 간격) - 10 (바의 폭/2) - 10(공의 반지름) = 330
    x_pos_bar_min = src_width / 2 - bar_gab - dot_radius - dot_radius
    x_pos_bar_max = src_width / 2 - bar_gab
    y_pos_bar = 40
    if ball.xcor() > x_pos_bar_min and ball.xcor() < x_pos_bar_max and ball.ycor() < (
            bar_b.ycor() + y_pos_bar) and ball.ycor() > (bar_b.ycor() - y_pos_bar):
        # x좌표 330~350 까지를 부딪혔다고 판단하고, 330을 넘었을 경우
        # 표면에서 부딪힌 것처럼 보이기 위해서 x좌표 330으로 볼을 이동
        ball.setx(x_pos_bar_min)
        ball.dx *= -1 #x축 이동방향 전환

    # bar_a 볼 튕기기
    if ball.xcor() < -x_pos_bar_min and ball.xcor() > -x_pos_bar_max and ball.ycor() < (
            bar_a.ycor() + y_pos_bar) and ball.ycor() > (bar_a.ycor() - y_pos_bar):
        ball.setx(-x_pos_bar_min)
        ball.dx *= -1

    ## 볼이 좌우 벽에 도달하면 점수를 세고 볼을 가운데로 옮기기
    # 왼쪽 벽
    if ball.xcor() > x_pos:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B:{score_b}", align="center", font=("Courier", 24, "normal"))

    # 오른쪽 벽
    if ball.xcor() < -x_pos:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B:{score_b}", align="center", font=("Courier", 24, "normal"))
    # 볼이 핑퐁 바에 부딪혔을 경우 튕기기
