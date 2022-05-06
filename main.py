import random
import os
import time
import numpy as np
import numpy.linalg


def print_matrix (m):                                                                                                   # функция вывода матрицы
    for i in m:
        for j in i:
            print ('%4d' %j, end= ' ')
        print()
try:
    start = time.time()
    n = int(input())
    while n < 4:
        n = int(input('Введите количество строк(столбцов) квадратной матрицы > 3'))
    k = int(input())
    A = [[0 for i in range (n)]for j in range (n)]                                                                      # задаем матрицу A
    F = [[0 for i in range(n)] for j in range(n)]                                                                       # задаем матрицу F
    for i in range (n):
        for j in range (n):
            A[i][j] = random.randint(-10,10)
            F[i][j] = A[i][j]
    print ('A')
    print_matrix(A)
    s = 0                                                                                                               # введем переменную для подсчета количество нулей в C в нечетных столбцах
    r = 1                                                                                                               # введем переменную для подсчета произведения чисел по периметру С
    for i in range(n):
        for j in range(n):
            if i < (n // 2) and j > (n // 2 - (n - 1) % 2):
                if j % 2 == 0 and A[i][j] == 0:
                    s += 1
                if i == 0 or i == (n // 2 - 1) or j == (n // 2 + n % 2) or j == (n-1):
                    r *= A[i][j]
    print (s,r)
    if s > r:
        for i in range(n // 2 + 1):                                                                                     # если нулей больше то мы симметрично меняем B и C
            F[i] = F[i][::-1]
    else:                                                                                                               # иначе меняем B и E местами несимметрично
        for i in range(n // 2 + 1):
            for j in range(n // 2 + 1):
                if j < n // 2 and i < n // 2:
                    F[i][j], F[i + n // 2 + n % 2][j + n // 2 + n % 2] = F[i + n // 2 + n % 2][j + n // 2 + n % 2],F[i][j]
    print('F')
    print_matrix(F)
    if np.linalg.det(A) > sum(np.diagonal(F)):                                                                          #если определитель матрицы А больше суммы диагональных элементов матрицы F
        At = np.transpose(A)                                                                                            # траснпонируем матрицу A
        print('At')
        print_matrix(At)
        Aobr = np.ones((n,n))                                                                                           # задаём обратную матрицу
        try:
            Aobr = np.linalg.inv(A)
            print ('Aobr')
            print (Aobr)
        except numpy.linalg.LinAlgError:
            print ('матрица A вырожденная')
        Umnozh = [[0 for i in range(n)] for j in range(n)]                                                              # умножаем Aobr на At
        for i in range(n):
            for j in range(n):
                Umnozh[i][j] = sum([Aobr[i][h] * At[h][j] for h in range(n)])
        print('Umnozh')
        print_matrix(Umnozh)
        Fk = [[j * k for j in i] for i in F]
        print('F*k')
        print_matrix(Fk)
        Result = [[0 for i in range(n)] for j in range(n)]                                                              # находим разность умножения и Fk
        for i in range(n):
            for j in range(n):
                Result[i][j] += Umnozh[i][j] - Fk[i][j]
        print ('Result')
        print_matrix(Result)
    else:
        B = np.array(A)
        G = np.tril(A)
        Gobr = np.zeros((n, n))                                                                                         # задаём обратную матрицу G
        try:
            Gobr = np.linalg.inv(G)
            print('Gobr')
            print(Gobr)
        except numpy.linalg.LinAlgError:
            print('матрица A вырожденная')
        Fobr = np.zeros((n, n))                                                                                         # задаём обратную матрицу F
        try:
            Fobr = np.linalg.inv(F)
            print('Fobr')
            print(Fobr)
        except numpy.linalg.LinAlgError:
            print('матрица F вырожденная')
        Summa = [[0 for i in range(n)] for j in range(n)]                                                               # вычисляем сумму матрицы A и Gobr
        for i in range(n):
            for j in range(n):
                Summa[i][j] += A[i][j] + Gobr[i][j]
        print('Summa')
        print_matrix(Summa)
        Vichitanie = [[0 for i in range(n)] for j in range(n)]                                                          # находим разность суммы и матрицы Fobr
        for i in range(n):
            for j in range(n):
                Vichitanie[i][j] += Summa[i][j] - Fobr[i][j]
        print('Vichitanie')
        print_matrix(Vichitanie)
        Result = [[j * k for j in i] for i in Vichitanie]
        print('Result')
        print_matrix(Result)
    print(f"\nВремя выполнения {time.time() - start} секунд")
except ValueError:
    print("Введённые данные не являются числом")



