T = int(input())

def array_sum(i):
    result = []
    for idx in range(array_num):
        if idx+fly_num == len(data[i])+1:
            break       
        result.append(sum(data[i][idx:idx+fly_num]))
    return result

def hang_sum(data):
    result = []
    for i in range(array_num-fly_num+1):         
        for j in range(len(data[0])): 
            temp = 0
            for k in range(fly_num):
                temp+=data[i+k][j]
            result.append(temp)           
    return(max(result))
for index in range(1, T+1):
    array_num, fly_num = map(int,(input().split()))
    data = []
    for i in range(array_num):
    	data.append(list(map(int, input().split())))
    result = []
    for i in range(array_num):
        result.append(array_sum(i))
    result = hang_sum(result)
    print('#{} {}'.format(index, result))
    