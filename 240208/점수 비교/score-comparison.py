A=input().split()
B=input().split()

A_m,A_e=int(A[0]),int(A[1])
B_m,B_e=int(B[0]),int(B[1])

if A_m>B_m and A_e>B_e:
    print("1")
else: print("0")