j = 0
while True:

    n,m,c = input().split()
    n = int(n)
    m = int(m)
    c = int(c)
    j = j+1
    if n==0 and m==0 and c==0:
        break

    d = {}
    for i in range(n):
        x = int(input())
        d[str(i+1)] = [x, 0]


    action = []
    for i in range(m):
        action.append(input())

    result = 'not blown'
    for i in action:
        try:
            if d[i][1] == 0:
                d[i][1] = 1
            else:
                d[i][1] = 0
        except KeyError:
            True
        
        consumption = 0
        for f in d.keys():
            consumption = consumption + d[f][1]*d[f][0]

        if consumption > c:
            result = 'blown'
            break
        
        else:
            continue
            
    print('Sequence ' + str(j))
    print('Fuse was '+result+'.')
    if result == 'blown':
        print('Maximal power consumption was ' + str(consumption) + ' amperes.')
    print('\n')

