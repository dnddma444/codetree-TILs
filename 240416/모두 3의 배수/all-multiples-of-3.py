sat=True

for i in range (5):
    n=int(input())
    if n%3==0:
        sat=True
    else:
        sat=False
        break

if sat == True:
    print('1')
else:
    print('0')