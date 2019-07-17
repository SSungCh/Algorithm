T = int(input())

for index in range(1, T+1):
    data = list(map(int,input().split()))
    result = round(sum(data)/len(data))
    print('#{}'.format(index), result)