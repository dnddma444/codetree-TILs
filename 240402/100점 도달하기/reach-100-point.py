n=int(input())

for i in range (n,101):
    if i>=90:
        print('A',end=' ')
        i+=1
    elif i>=80:
        print('B',end=' ')
        i+=1
    elif i>=70:
        print('C',end=' ')
        i+=1
    elif i>=60:
        print('D',end=' ')
        i+=1
    else :
        print('F',end=' ')
        i+=1