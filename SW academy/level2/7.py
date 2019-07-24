T = int(input())

for index in range(1, T+1):
    num = int(input())
    result = 0
    for count in range(1, num+1):
        if count % 2:
            result += count
        else:
            result -= count
    print('#{} {}'.format(index,result))