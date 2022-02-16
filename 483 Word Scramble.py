sen = [list(w) for w in input().split()]
print(sen)

for w in sen:
    for i in range(len(w)//2):
        temp = w[i]
        w[i] = w[len(w)-1-i]
        w[len(w)-1-i] = temp

sen = [''.join(w) for w in sen]
sen = " ".join(sen)
print('......')
print(sen)


