T = int(input())

for index in range(1, T+1):
    data = list(map(int, input().split()))
    for i in range(data.count(max(data))):
        data.remove(max(data))
    for i in range(data.count(min(data))):
        data.remove(min(data))
    
    print('#{} {}'.format(index, round(sum(data)/len(data))))