
T = int(input())
for index in range(1, T+1):
    print('#{}'.format(index))
    row = int(input())
    for rownum in range(row): 
        list_ =1
        Plist = [list_]
        print('1', end =' ')
        for i in range (rownum):
            list_ = list_ * (rownum - i) / (i+1)
            Plist.append(int(list_))
            print(str(int(list_)), end= ' ')
        print()