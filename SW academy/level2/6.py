T = int(input())

for index in range(1, T+1):
    data = input().strip()
    if data in data[::-1]:
        print('#{} 1'.format(index))
    else:
        print('#{} 0'.format(index))
   