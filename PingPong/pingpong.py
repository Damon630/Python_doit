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

#핑퐁 볼 이동 xy 픽셀
ball_mov_pixel = 2

# 핑퐁 볼 반지름, 핑퐁 바의 두께의 반
dot_radius = 10

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
