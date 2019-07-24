
T = int(input())

for index in range(1, T+1):
    data = list(input())
    temp = []  
    for dat_  in data[0:15]:
        if dat_ not in temp:
            temp.append(dat_)  
            if temp == data[len(temp):len(temp*2)]: 
                break
        else:
            if temp == data[len(temp):len(temp*2)]:         
                break										
            temp.append(dat_)
    print('#{} {}'.format(index, len(temp)))