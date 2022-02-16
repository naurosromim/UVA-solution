t = int(input())

for k in range(t):

    a = [int(x) for x in input().split()]
    l = len(a)

    for i in range(l):
        for j in range(l):
            if a[i]>a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    print('Case ' + str(k+1) + ': ' + str(a[1]))