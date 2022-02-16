i,j = input().split()
i = int(i)
j = int(j)
i_o = i
j_o = j

if i>j:
    temp = i
    i = j
    j = temp

def cycle_len(a):
    c = 1
    while a!=1:
        
        if a%2==0:
            a = a/2
        else:
            a = 3*a+1
        c = c+1
    return c

l = 0
while i<=j:
    k = cycle_len(i)
    if k>l:
        l = k
    i = i+1

print(i_o, j_o, l)