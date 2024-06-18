
import numpy as np

def tridiagonal_solve(a, b, c, d):
    n = len(d)
    alpha = np.zeros(n-1)
    beta = np.zeros(n)
    
    # Прямой ход
    alpha[0] = -c[0] / b[0]
    beta[0] = d[0] / b[0]
    
    for i in range(1, n-1):
        alpha[i] = -c[i] / (b[i] + a[i] * alpha[i-1])
        beta[i] = (d[i] - a[i] * beta[i-1]) / (b[i] + a[i] * alpha[i-1])
    
    beta[n-1] = (d[n-1] - a[n-2] * beta[n-2]) / (b[n-1] + a[n-2] * alpha[n-2])
    
    # Обратный ход
    x = np.zeros(n)
    x[n-1] = beta[n-1]
    
    for i in range(n-2, -1, -1):
        x[i] = alpha[i] * x[i+1] + beta[i]
    
    return x

a = [0, 7, 21, 7]
b = [8, 19, -23, -7]
c = [-2, 5, 9, 0]
d = [-14, 55, 49, 8]

solution = tridiagonal_solve(a, b, c, d)
print("Решение методом прогонки:", solution)
