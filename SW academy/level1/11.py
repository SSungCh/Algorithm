T = list(map(int, input().split()))
count = 1
while T[1] != T[0]:
    T[1] += 1
    count += 1
print(count)