T = int(input())

for index in range(1, T+1):
    data = map(int, input().split())
    result=max(data)
    print('#{}'.format(index),result)