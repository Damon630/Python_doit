import random

deck = []

shapes = '♥♣♠◆'
nums = []
for i in range(2, 11):
    nums.append(str(i))
for c in 'JQKA':
    nums.append(c)

# 카드 한묶음 만들기
for shape in shapes:
    for num in nums:
        deck.append((shape, num))

deck.append(('Joker', 'black'))
deck.append(('Joker', 'colored'))
random.shuffle(deck)

# 카드 나누기

player = []
computer = []

for i in range(7):
    player.append(deck.pop())
    computer.append(deck.pop())

# 낸 카드에 하나 올려두기
put = []
put.append(deck.pop())

while True:

    print("플레이어 가 낼 차례입니다.")
    print("현재 패 >> ", player)
    print("놓여진 카드 >> ", put[-1])

    available = []
    for card in player:
        if (card[0] == put[-1][0]
                or card[1] == put[-1][1]
                or card[0] == 'Joker'
                or put[-1][0] == 'Joker'):
            available.append(card)

    print("낼 수 있는 카드 : ", available)

    if len(available) > 0:
        i = int(input("몇 번째 카드를 내시겠습니까?"))
        i -= 1
        selected = available[i]
        player.remove(selected)
        put.append(selected)
        print()
    else:
        print("낼 수 있는 카드가 없어서 먹습니다.")
        print()
        player.append(deck.pop())

    if len(player) == 0:
        print("플레이어 승!")
        break

    print("컴퓨터 가 낼 차례입니다.")
    print("놓여진 카드 >> ", put[-1])

    available = []
    for card in computer:
        if (card[0] == put[-1][0]
                or card[1] == put[-1][1]
                or card[0] == 'Joker'
                or put[-1][0] == 'Joker'):
                available.append(card)

    if len(available) > 0:
        selected = random.choice(available)
        computer.remove(selected)
        put.append(selected)
        print("컴퓨터가 ", selected, "를 냈습니다.")
        print()

    else:
        print("낼 수 있는 카드가 없어서 먹습니다.")
        computer.append(deck.pop())
        print()

    if len(computer) == 0:
        print("컴퓨터 승!")
        break
