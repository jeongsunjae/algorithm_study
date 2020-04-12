N, S = input(), input()

score, bonus = 0, 0

# enumerate 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가집니다
# range([strat,] stop [,step]) 필요한 만큼의 숫자를 만들어내는 유용한 기능입니다.
# S => O X O O X O 이런식으로 나오면 0 : O 1 : X 이런식으로 나옴
for idx, OX in enumerate(S):
    if OX == 'O':
        score += idx+1+bonus
        bonus += 1
    else:
        bonus = 0


print(score)
