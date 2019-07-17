T = int(input())

for index in range(1, T+1):
    data = input()
    year = data[0:4]
    month = data[4:6]
    day = data[6:8]

    if int(month) > 0 and int(month) <13:
        if int(month) in [1,3,5,7,8,10,12] and int(day) <32 and int(day)>0:
            print('#{} {}/{}/{}'.format(index,year,month,day))
        elif int(month) in [4,6,9,11] and int(day) <31 and int(day) >0:
            print('#{} {}/{}/{}'.format(index,year,month,day))
        elif int(month) == 2 and int(day)<29 and int(day)>0:
        	print('#{} {}/{}/{}'.format(index,year,month,day))
        else:
            print('#{} -1'.format(index))
    else:
            print('#{} -1'.format(index))
    