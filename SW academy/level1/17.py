# 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
A, B = map(int, input().split())
print('A') if A-B in [-2, 1] else print('B')
