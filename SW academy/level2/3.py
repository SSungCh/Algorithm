T = int(input())

for index in range(1, T+1):
    data = list(str(input()))
    temp = []
    temp2 = []
    temp3 =[]
    count = 0
    for dat_  in data:
        if dat_ not in temp:
            temp.append(dat_)
        else:
        
            temp2.append(dat_)
            temp3.append(''.join(temp))
            temp.clear()
            temp.append(dat_)
            print(temp, temp2, temp3)
            if ''.join(temp2) in temp3:
                count+= 1
                temp2 =[]
    print(count)