t = int(input())

for i in range(t):
    sum, dif = input().split()
    sum = int(sum)
    dif = int(dif)

    x= (sum+dif)//2
    y = abs(sum-dif)//2

    if x+y == sum and abs(x-y)==dif:
        print(x,y)
    else:
        print('impossible')


T = int(input())
for i in range(T):
    a, b = map(int,input().split())
    y = abs(a - b) // 2
    x = a - y
    
    if (x+y) == a and abs(x - y) == b:
        print(max(x, y), min(x, y))
    else:
        print("impossible")

