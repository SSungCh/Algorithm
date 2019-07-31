T = int(input())

for index in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    result_h = 12 if (h1+h2+(m1+m2)//60)%12 == 0 else (h1+h2+(m1+m2)//60)%12
    result_m = (m1+m2)%60

    
    print('#{} {} {}'.format(index, result_h, result_m))