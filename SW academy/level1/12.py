T = int(input())

for index in range(1, T+1):
    data1, data2 = map(int,input().split())
    print('#{} {} {}'.format(index, data1//data2, data1 % data2))