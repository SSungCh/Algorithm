T = int(input())         

for index in range(1, T+1):
    temp = int(input())
    data = list(map(int, input().split()))
    result = 0

    def find_max(data, result=0, index_2 = 0):
        index_ = data.index(max(data))
    
        for num in range(index_-1, -1, -1):
            result += data[index_] -data[num]

        index_2 += index_+1
       

        if index_2 != temp:             
            return find_max(data[index_+1:], result, index_2) 
        else:
            return result          
            
       
    print('#{} {}'.format(index, find_max(data)))  