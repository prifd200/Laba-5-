import random
import os
import time
import numpy as np
import numpy.linalg

try:
    numpy.set_printoptions(precision=3, linewidth=150)
    start = time.time()
    n = int(input())
    while n < 4:
        n = int(input('Введите количество строк(столбцов) квадратной матрицы > 3'))
    k = int(input())
    A = np.random.randint(-10,10,(n,n))                                                                                 # задаем матрицу A
    F = np.copy(A)                                                                                                      # задаем матрицу F
    print ('A')
    print (A)
    s = 0                                                                                                               # введем переменную для подсчета количество нулей в C в нечетных столбцах
    r = 1                                                                                                               # введем переменную для подсчета произведения чисел по периметру С
    for i in range(n):
        for j in range(n):
            if i < (n // 2) and j > (n // 2 - (n - 1) % 2):
                if j % 2 == 0 and A[i][j] == 0:
                    s += 1
                if i == 0 or i == (n // 2 - 1) or j == (n // 2 + n % 2) or j == (n-1):
                    r *= int(A[i][j])
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
    print (F)
    if np.linalg.det(A) > sum(np.diagonal(F)):                                                                          #если определитель матрицы А больше суммы диагональных элементов матрицы F
        At = np.transpose(np.copy(A))                                                                                   # траснпонируем матрицу A
        print('At')
        print (At)
        Aobr = np.ones((n,n))                                                                                           # задаём обратную матрицу
        try:
            Aobr = np.linalg.inv(A)
            print ('Aobr')
            print (Aobr)
        except numpy.linalg.LinAlgError:
            print ('матрица A вырожденная')
        Umnozh = np.matmul(Aobr,At)                                                                                     # умножаем Aobr на At
        print('Umnozh')
        print (Umnozh)
        Fk = np.dot (F,k)
        print('F*k')
        print (Fk)
        Result = Umnozh - Fk                                                                                           # находим разность умножения и Fk
        print ('Result')
        print (Result)
    else:
        G = np.tril(A)
        Gobr = np.zeros((n, n))                                                                                         # задаём обратную матрицу G
        try:
            Gobr = np.linalg.inv(G)
            print('Gobr')
            print(Gobr)
        except numpy.linalg.LinAlgError:
            print('матрица G вырожденная')
        Fobr = np.zeros((n, n))                                                                                         # задаём обратную матрицу F
        try:
            Fobr = np.linalg.inv(F)
            print('Fobr')
            print(Fobr)
        except numpy.linalg.LinAlgError:
            print('матрица F вырожденная')
        Summa = A + Gobr                                                                                                # вычисляем сумму матрицы A и Gobr
        print('Summa')
        print (Summa)
        Vichitanie = Summa - Fobr                                                                                       # находим разность суммы и матрицы Fobr
        print('Vichitanie')
        print (Vichitanie)
        Result = np.dot(Vichitanie,k)
        print('Result')
        print (Result)
    print(f"\nВремя выполнения {time.time() - start} секунд")
except ValueError:
    print("Введённые данные не являются числом")



