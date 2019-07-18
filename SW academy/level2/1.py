import sys
sys.stdin = open("input.txt", "r")

    
T = int(input())         

for index in range(1, T+1):
    temp = int(input())
    data = list(map(int, input().split()))
    result = 0
    index_ = data.index(max(data))
    if index_ == temp-1:
       result += data[index_]*len(data[:index_]) - sum(data[:index_])     
    while index_!=temp-1:
        index_ = data.index(max(data))           
        result += data[index_]*len(data[:index_]) - sum(data[:index_])  
        data = data[index_+1:]
        if data == []:
            break
      
            
       
    print('#{} {}'.format(index, result))  