n = int(input())

for j in range(n):

    k = int(input())

    d = {}
    for i in range(k):
        x, y = input().split()
        d[x] = int(y)

    m = int(input())
    money = 0

    for i in range(m):
        sen = input()
        for w in sen:
            if w in d.keys():
                money=money+d[w]


    a = money/100
    print(str(a)+'$')


