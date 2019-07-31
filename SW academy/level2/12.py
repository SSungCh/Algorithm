def f_row(id,data):
    for i in range(9):
        if len(set(data[i])) != 9:
            print('#{} 0'.format(id))
            return 0
    return 1
def f_col(id,data):
    data2 = []
    for i in range(9):
        for j in range(9):

            if data[j][i] in data2:
                print('#{} 0'.format(id))
                return 0
            data2.append(data[j][i])
        data2 = []
    return 1
def f_33(id, data):
    data2 = []
    for t in range(3):
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if data[t*3+j][i*3+k] in data2:
                        print('#{} 0'.format(id))
                        return 0
                    data2.append(data[t*3+j][i*3+k])
            data2 = []

    return 1


T = int(input())

for index in range(1, T+1):
    data = []
    for T in range(9):
        data.append(list(map(int, input().split())))

    t1= f_row(index,data)
    t2= f_col(index,data)
    t3= f_33(index,data)
    if t1*t2*t3 != 0:
        print('#{} 1'.format(index))
