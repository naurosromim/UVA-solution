t = int(input())
for i in range(t):
    a1, b1 = input().split()
    a1 = int(a1)
    b1 = int(b1)

    a2, b2 = input().split()
    a2 = int(a2)
    b2 = int(b2)

    a3, b3 = input().split()
    a3 = int(a3)
    b3 = int(b3)

    a4, b4 = input().split()
    a4 = int(a4)
    b4 = int(b4)

    ab = (a1-a2)**2 + (b1-b2)**2
    cd = (a3-a4)**2 + (b3-b4)**2
    ad = (a1-a4)**2 + (b1-b4)**2
    bc = (a3-a2)**2 + (b3-b2)**2
    ac = (a1-a3)**2 + (b1-b3)**2
    bd = (a2-a4)**2 + (b2-b4)**2

    x = [ab, cd, ad, bc, ac, bd]
    l = len(x)
    

    for a in range(l):
        for b in range(l):
            if x[b]>x[a]:
                temp = x[a]
                x[a]=x[b]
                x[b]=temp

    print(x)

    if x[0]==x[1]==x[2]==x[3]:
        if x[5] == x[0] + x[2]:
            print('Case 1: Square')
        else: print('Case 3: Rhombus')
    elif x[0]==x[1] and x[2]==x[3]:
        if x[5] == x[0] + x[2]:
            print('Case 2: Rectangle')
        else: print('Case 4: Parallelogram')
    elif (a1==a2 and a3==a4) or (b1==b2 and b3==b4) or (a1==a3 and a2==a4) or (b1==b3 and b2==b4) or (a1==a4 and a2==a3) or (b1==b4 and b2==b3):
        print('Case 5: Trapezium')
    else:
        print('Case 6: Ordinary Quadrilateral')