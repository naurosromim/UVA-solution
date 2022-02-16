while True:

    t = int(input())
    if t==0:
        break

    def inp():
        a,b = input().split()
        a = int(a)
        b = int(b)
        return a,b

    o1, o2 = inp()

    m=[]
    for i in range(t):
        a,b = inp()
        if a == o1 or b == o2:
            m.append('divisa')
        elif a>o1 and b>o2:
            m.append('NE')
        elif a<o1 and b>o2:
            m.append('NO')
        elif a<o1 and b<o2:
            m.append('SO')
        elif a>o1 and b<o2:
            m.append('SE')

    for i in m:
        print(i)