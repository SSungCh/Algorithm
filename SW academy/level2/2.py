T = int(input())
for i in range(1,T+1):
    count=0
    data = list(str(i))
    for num in data:
        if num in ['3', '6', '9']:
            count+=1
    if count != 0:
        print('-'*count, end=' ')
        continue
    else:
        print(i,end=' ')
