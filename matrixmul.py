import random
m1=input("enter no. of rows in the first matrix: ")
n1=input("enter no. of columns in the first matrix: ")
a = [[random for col in range(n1)] for row in range(m1)]
for i in range(m1):
    for j in range(n1):
        a[i][j]=input()
m2=input ("enter no. of rows in the second matrix: ")
n2=input ("enter no. of columns in the second matrix: ")
b = [[random for col in range(n2)] for row in range(m2)]
for i in range(m2):
    for j in range(n2):
        b[i][j]=input()
c=[[random for col in range(n2)]for row in range(m1)]
if (n1==m2):
    for i in range(m1):
        for j in range(n2):
            c[i][j]=0
            for k in range(n1):
                c[i][j]+=a[i][k]*b[k][j]
            print c[i][j]
