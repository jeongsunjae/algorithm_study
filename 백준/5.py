# input 을 받아서 쪼갠다음 있으면 1
N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = input()

for i in list(map(int, input().split())):
    print(A.get(i, 0))
