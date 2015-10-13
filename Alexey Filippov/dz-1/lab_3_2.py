__author__ = 'lelik'

a = [1, -20, 38, 0, 44]
b = [88, -20, 48, 4, 33, 2]
lst = []
for i,x in enumerate(a):
    if i < len(b)-1:
        if x < b[i]:
            print(x)
            lst = a

        else:
            print(b[i])
            lst = b

        y = i
        k = 0

        while k < abs(x - b[i]):
            if y < len(lst)-1:
                 y += 1
            else:
                y = 0
            k += 1
        if (y >= len(lst)):
            print('res: '+ str(lst[0]))
        else:
            print('res: '+str(lst[y]))

        if abs(x - b[i]) < 15:
            print('Congratulation !')

