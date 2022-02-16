while True:
    h, u, d, f = input().split()
    h = int(h)
    u = int(u)
    d = int(d)
    f = int(f)

    if h==0 and u==0 and d==0 and f==0:
        break

    f = u * f / 100

    current_h = 0
    day = 0

    while True:
        current_h = current_h + (u - day*f)
        current_h = current_h - d
        #print(day, current_h)

        if current_h > h:
            result = 'success'
            day = day+1
            break
        elif current_h < 0:
            result = 'failure'
            day = day+1
            break
        day = day+1

    print(result + ' on day ' + str(day))