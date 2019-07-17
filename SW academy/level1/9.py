T = map(ord, input())
for i in T:
    if i>=97:
        print(chr(i-32), end='')
    else:
        print(chr(i),end='')