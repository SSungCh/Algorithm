# SW academy

```python
# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.
# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////

```



## level 1

1. [홀수만 더하기](./level1/1.py)
2. [평균값 구하기](./level1/2.py)
  3. [큰놈, 작은놈, 같은놈](./level1/3.py)
  4. [최대수 구하기](./level1/4.py)
  5. [중간값 찾기](./level1/5.py)
  6. [자릿수 더하기](./level1/6.py)
  7. [연월일 달력](./level1/7.py) : 3번 시도함
  8. [알파벳을 숫자로 변환](./level1/8.py) : ord() 함수 >> 문자열을 아스키 코드로 변환
  9. [신문 헤드라인](./level1/9.py):  chr() 함수 >> 아스키 코드를 문자열로 변환
* `print(input().upper())`
10. [스탬프찍기](./level1/10.py)
11. [서랍의 비밀번호](./level1/11.py)
12. [몫 과 나머지 출력하기](./level1/12.py)
13. [대각선 출력하기](./level1/13.py)
14. [N줄덧셈](./level1/14.py)
15. [아주 간단한 계산기](./level1/15.py)
16. [간단한 N의 약수](./level1/16.py)
17. [1대1 가위바위보](./level1/17.py)
18. [더블더블](./level1/18.py)
19. [거꾸로 출력해 보아요](./level1/19.py)



## level 2

1. [백만장자 프로젝트](./level2/1.py) : 제귀함수 쓰면 안됨 7번 시도해서 풀음
2. [간단한 369 게임](./level2/2.py) : list(str(int타입)) 을 하면 나눠서 저장됨 숫자가
3. [패턴 마디의 길이](./level2/3.py)
4. [파스칼의 삼각형](./level2/4.py)
5. [파리퇴치](./level2/5.py) *** 다른 방법 찾아보기.
6. [초심자의 회문 검사](./level2/6.py) 수업시간에 한것. [::-1]  .strip()으로 빈칸 제거
7. [지그재그 숫자](./level2/7.py)  ez
8. [중간 평균값 구하기](./level2/8.py)  list.count(),  list.remove()  round(num, num)
9. [조교의 성적 매기기](./level2/9.py)  
10. [어디에 단어가 들어갈 수 있을까](./level2/10.py)  
11. [시각 덧셈](./level2/11.py)  
12. [스도쿠 검증](./level2/12.py)  




​     