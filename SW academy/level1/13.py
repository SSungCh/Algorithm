a = ['+','+','+','+','+']
for num in range(len(a)):
    a[num] = '#'
    for n in a:
        print(n,end='')
    a[num] = '+'
    print()