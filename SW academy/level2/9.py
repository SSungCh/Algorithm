T = int(input())

for index in range(1, T+1):
    N, K = map(int, input().split())
    tot = {}
    temp = []
    grade = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
      
    for i in range(N):
        data = list(map(int, input().split()))
        tot[i+1]=data[0]*0.35 + data[1]*0.45 + data[2] * 0.2
        temp.append(data[0]*0.35 + data[1]*0.45 + data[2] * 0.2)   
    for idx,value in enumerate(sorted(temp)):
        if value == tot[K]:     
            print('#{} {}'.format(index, grade[int(idx//(N/10))]))
        
        