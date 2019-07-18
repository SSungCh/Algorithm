# 양의 정수 x를 입력 받아 제곱근의 근사값을 반환하는 함수
def my_sqrt(n):
    result = 0
    data = n-1
    data2 = n
    while abs(result**2 -n) <= 1e-10:
        print(f'{data**2} < root({n}) < {data2**2}')
        data2 = (data+data2) / 2
        result = data2
        print(f'{data**2} < root({n}) < {data2**2}')
        data = data2/2
     