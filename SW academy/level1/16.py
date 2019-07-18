T = int(input())
for num in range(T+1):
    if not T%(num+1):
        print(num+1,end=' ')