#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Демонстрация работы оптимизированного класса Matrix без numpy
"""

import class_matrix
import funcs
from task_data import *
from Methods import *

def solve_exact_gauss(A, b):
    """
    Точное решение СЛАУ методом Гаусса без numpy
    """
    # Создаем расширенную матрицу [A|b]  
    rows, cols = A.dim()
    augmented = []
    
    for i in range(rows):
        row = A.matrix[i][:] + [b.matrix[i][0]]
        augmented.append(row)
    
    n = len(augmented)
    
    # Прямой ход метода Гаусса
    for i in range(n):
        # Поиск главного элемента
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented[k][i]) > abs(augmented[max_row][i]):
                max_row = k
        
        # Обмен строк
        augmented[i], augmented[max_row] = augmented[max_row], augmented[i]
        
        # Исключение
        for k in range(i + 1, n):
            if augmented[i][i] != 0:  # Избегаем деления на ноль
                factor = augmented[k][i] / augmented[i][i]
                for j in range(i, n + 1):
                    augmented[k][j] -= factor * augmented[i][j]
    
    # Обратный ход
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = augmented[i][n]
        for j in range(i + 1, n):
            solution[i] -= augmented[i][j] * solution[j]
        if augmented[i][i] != 0:
            solution[i] /= augmented[i][i]
    
    return solution

def main():
    eps = 10 ** -5
    print("=== Демонстрация оптимизированного класса Matrix ===\n")
    
    for i in range(3):  # Уменьшили до 3 тестов для краткости
        try:
            A = class_matrix.Matrix(testdata(i).A)
            b = class_matrix.Matrix(testdata(i).b)
            print(f'{"="*20} Тест {i} {"="*20}')
            
            print(f"Матрица A ({A.dim()[0]}x{A.dim()[1]}):")
            A.PrintM()
            
            print(f"Вектор b ({b.dim()[0]}x{b.dim()[1]}):")
            b.PrintM()
            
            # Точное решение методом Гаусса
            print("\n📊 Точное решение (метод Гаусса):")
            exact_solution = solve_exact_gauss(A, b)
            exact_matrix = class_matrix.Matrix([[x] for x in exact_solution])
            exact_matrix.PrintM()
            
            # Решение методом простых итераций
            print("\n🔄 Решение методом простых итераций:")
            try:
                res_si, n_si = MoSI(A, b, eps)
                res_si.PrintM()
                # Преобразуем решение в правильный формат для сравнения
                if res_si.dim()[1] == 1:  # Это вектор-столбец
                    error_si = (res_si - exact_matrix).vecnorma()
                else:  # Преобразуем к вектору-столбцу
                    res_si_col = class_matrix.Matrix([[res_si.matrix[0][i]] for i in range(len(res_si.matrix[0]))])
                    error_si = (res_si_col - exact_matrix).vecnorma()
                print(f"Итераций: {n_si}, Заданная точность: {eps}, Абсолютная погрешность: {error_si:.2e}")
            except Exception as e:
                print(f"Ошибка в методе простых итераций: {e}")
            
            print("\n" + "-" * 60)
            
            # Решение методом Зейделя
            print("\n🎯 Решение методом Зейделя:")
            try:
                res_seidel, n_seidel = Seidel(A, b, eps)
                res_seidel.PrintM()
                # Преобразуем решение в правильный формат для сравнения
                if res_seidel.dim()[1] == 1:  # Это вектор-столбец
                    error_seidel = (res_seidel - exact_matrix).vecnorma()
                else:  # Преобразуем к вектору-столбцу
                    res_seidel_col = class_matrix.Matrix([[res_seidel.matrix[0][i]] for i in range(len(res_seidel.matrix[0]))])
                    error_seidel = (res_seidel_col - exact_matrix).vecnorma()
                print(f"Итераций: {n_seidel}, Заданная точность: {eps}, Абсолютная погрешность: {error_seidel:.2e}")
            except Exception as e:
                print(f"Ошибка в методе Зейделя: {e}")
                
            print("\n" + "=" * 60 + "\n")
            
        except Exception as e:
            print(f"Ошибка в тесте {i}: {e}")
            continue

def demo_matrix_features():
    """Демонстрация дополнительных возможностей оптимизированного класса"""
    print("=== Демонстрация дополнительных возможностей ===\n")
    
    # Создание различных типов матриц
    print("1. Создание матриц:")
    identity = class_matrix.Matrix(rows=3, cols=3, identity=True)
    print("Единичная матрица 3x3:")
    identity.PrintM()
    
    zero = class_matrix.Matrix(rows=2, cols=4)
    print("Нулевая матрица 2x4:")
    zero.PrintM()
    
    # Демонстрация свойств
    print("\n2. Анализ свойств матрицы:")
    test_matrix = class_matrix.Matrix([[1, 2, 3], [2, 5, 6], [3, 6, 9]])
    print("Тестовая матрица:")
    test_matrix.PrintM()
    print(f"Симметричная: {test_matrix.is_symmetric()}")
    print(f"Квадратная: {test_matrix.is_square()}")
    print(f"Определитель: {test_matrix.det():.4f}")
    print(f"След: {test_matrix.trace()}")
    print(f"Норма Фробениуса: {test_matrix.frobenius_norm():.4f}")
    
    # Демонстрация операций
    print("\n3. Матричные операции:")
    A = class_matrix.Matrix([[1, 2], [3, 4]])
    B = class_matrix.Matrix([[5, 6], [7, 8]])
    print("Матрица A:")
    A.PrintM()
    print("Матрица B:")
    B.PrintM()
    print("A + B:")
    (A + B).PrintM()
    print("A * B:")
    (A * B).PrintM()

if __name__ == "__main__":
    try:
        demo_matrix_features()
        main()
        print("\n✅ Демонстрация завершена успешно!")
    except Exception as e:
        print(f"\n❌ Ошибка в демонстрации: {e}")
        raise
