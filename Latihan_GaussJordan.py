import numpy as np
import sys

n = int(input('Masukkan jumlah variabel : '))

a = np.zeros((n,n+1))
x = np.zeros(n)

print('Masukkan koefisien matriks augmented : ')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input(' a['+str(i)+']['+ str(j)+']='))

for i in range(n):
    if a[i][j] == 0.0:
        sys.exit('Devide by zero detected!')

    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

for i in range(n):
    x[i] = a[i][n]/a[i][i]

print('/nSolusi yang dibutuhkan : ')
for i in range(n):
    print('X%d = %0.6f' %(i,x[i]), end = '\t')