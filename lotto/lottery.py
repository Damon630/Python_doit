#무조건 따라해보기

import random

class Lotto:
    def __init__(self):
        self.win = set() #6개의 당첨 숫자 / 자료형 : 집합 (중복 없음)
        self.bonus = set() #보너스 번호(2등) / 자료형 : 집합 (중복 없음)
        self.myNum = set() #내가 뽑은 번호 / 자료형 : 집합 (중복없음)

    def init(self):
        self.win.clear() #안에 내용 삭제
        self.bonus.clear()
        while len(self.win) < 6:
            self.win.add(random.randrange(1, 46)) #1~45까지 중에 랜덤 숫자 뽑기

        while True:
            n = random.randrange(1, 46)
            if not (n in self.win): #보너스 번호를 뽑기 위해 이미 뽑은 win 번호랑 다른 번호를 받는다
                self.bonus.add(n)
                break

    def insert(self):
        self.myNum.clear() # 안에 들어있는거 지우기
        while len(self.myNum) < 6:
            print(str([len(self.myNum) + 1]) + "번째 숫자를 입력하세요. (1~45) : ", end="")
            n = int(input())
            if (n<=0) or (n>=46) or (n in self.myNum):
                print("=> 중복된 번호를 넣었거나 잘못된 번호를 넣었습니다. 다시 입력해주세요.")
                continue
            self.myNum.add(n)
            print("현재까지 번호 : "+str(list(self.myNum)))

    def match(self):
        if len(self.myNum) != 6:
            print("=> 2번을 눌러서 번호를 뽑아주세요.")
            return

        self.print()
        self.printMyNum()
        matchingNum = len(self.win.intersection(self.myNum))
        if matchingNum == 6:
            print("[1등] ㅊㅋㅊㅋ~~")
            print("세금 떼고 10억~~")
        elif matchingNum == 5 and self.myNum.intersection(self.bonus):
            print("[2등] 진짜 아쉽다 그래도 ㅊㅋㅊㅋ~~")
            print("세금 떼고 6천? 전세도 못가네ㅜㅜ")
        else:
            print("될놈될인데 우리는 안될놈인가보다..ㅜ")

        self.init() # 게임이 끝나면 clear해줘야함
        self.myNum.clear() # 게임이 끝나면 clear해줘야함

    def printMyNum(self):
        print("내 번호 : ", end="")
        tmp = list(self.myNum)
        tmp.sort()
        print(tmp)

    def print(self):
        if len(self.myNum) != 6: # 번호를 안뽑고 당첨번호를 볼 수 없다
            print("번호 부터 뽑으세요")
            return

        print("당첨 번호 : ", end="")
        arr = list(self.win)
        arr.sort()

        print(arr, end="")
        print(" +", list(self.bonus))

print("불로소득을 향해 ㄱㄱ")
lotto = Lotto()
lotto.init()
while True:
    print("*********************")
    print("1. 이번주 로또 번호를 본다.")
    print("2. 로또 번호를 뽑는다.")
    print("3. 새로운 로또 번호를 받는다.")
    print("4. 당첨 로또번호와 내 번호를 확인한다")
    print("5. 프로그램 종료한다.")

    num = int(input())
    if num == 1:
        print("이번주 로또 당첨 번호는?")
        lotto.print()
    elif num == 2:
        print("번호를 입력하세요.")
        lotto.insert()
        lotto.printMyNum()
    elif num == 3:
        print("새로운 당첨 번호를 받을게요~")
        lotto.init()
        lotto.print()
    elif num == 4:
        print("일확천금의 꿈은!? 두구두구두구두구")
        lotto.match()
    elif num == 5:
        print("잘~가 가지마~")
        break
    print()

