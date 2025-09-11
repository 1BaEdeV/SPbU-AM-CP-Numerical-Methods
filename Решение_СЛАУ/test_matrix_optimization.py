#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Тестирование оптимизированного класса Matrix
"""

from class_matrix import Matrix
from funcs import sqrtt, is_2d_array, is_vector, create_identity_matrix

def test_matrix_creation():
    """Тест создания матриц"""
    print("=== Тестирование создания матриц ===")
    
    # Создание матрицы из списка
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m = Matrix(data)
    print(f"Матрица 3x3:\n{m}")
    print(f"Размеры: {m.dim()}")
    
    # Создание единичной матрицы
    identity = Matrix(rows=3, cols=3, identity=True)
    print(f"Единичная матрица 3x3:\n{identity}")
    
    # Создание нулевой матрицы
    zero = Matrix(rows=2, cols=4)
    print(f"Нулевая матрица 2x4:\n{zero}")

def test_matrix_operations():
    """Тест математических операций"""
    print("\n=== Тестирование математических операций ===")
    
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    
    print(f"Матрица A:\n{m1}")
    print(f"Матрица B:\n{m2}")
    
    # Сложение
    add_result = m1 + m2
    print(f"A + B:\n{add_result}")
    
    # Вычитание
    sub_result = m1 - m2
    print(f"A - B:\n{sub_result}")
    
    # Умножение
    mul_result = m1 * m2
    print(f"A * B:\n{mul_result}")
    
    # Определитель
    print(f"det(A) = {m1.det()}")
    print(f"det(B) = {m2.det()}")
    
    # След
    print(f"trace(A) = {m1.trace()}")
    print(f"trace(B) = {m2.trace()}")

def test_matrix_properties():
    """Тест свойств матриц"""
    print("\n=== Тестирование свойств матриц ===")
    
    # Симметричная матрица
    symmetric = Matrix([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
    print(f"Симметричная матрица:\n{symmetric}")
    print(f"Является симметричной: {symmetric.is_symmetric()}")
    
    # Диагональная матрица
    diagonal = Matrix([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
    print(f"Диагональная матрица:\n{diagonal}")
    print(f"Является диагональной: {diagonal.is_diagonal()}")
    
    # Максимальный и минимальный элементы
    m = Matrix([[1, -5, 3], [2, 8, -1]])
    print(f"Матрица:\n{m}")
    print(f"Максимальный элемент: {m.max_element()}")
    print(f"Минимальный элемент: {m.min_element()}")

def test_norms():
    """Тест норм"""
    print("\n=== Тестирование норм ===")
    
    m = Matrix([[3, 4], [0, 5]])
    print(f"Матрица:\n{m}")
    print(f"Норма Фробениуса: {m.frobenius_norm()}")
    
    # Вектор
    vector_data = [[3], [4], [0]]
    v = Matrix(vector_data)
    print(f"Вектор:\n{v}")
    print(f"Норма вектора: {v.vecnorma()}")

def test_helper_functions():
    """Тест вспомогательных функций"""
    print("\n=== Тестирование вспомогательных функций ===")
    
    # Квадратный корень
    print(f"sqrt(16) = {sqrtt(16)}")
    print(f"sqrt(2) = {sqrtt(2)}")
    
    # Проверка 2D массива
    arr_2d = [[1, 2], [3, 4]]
    arr_1d = [1, 2, 3]
    print(f"[[1, 2], [3, 4]] является 2D: {is_2d_array(arr_2d)}")
    print(f"[1, 2, 3] является 2D: {is_2d_array(arr_1d)}")
    
    # Проверка вектора
    vector = [[1], [2], [3]]
    matrix = [[1, 2], [3, 4]]
    print(f"[[1], [2], [3]] является вектором: {is_vector(vector)}")
    print(f"[[1, 2], [3, 4]] является вектором: {is_vector(matrix)}")

def test_performance():
    """Тест производительности"""
    print("\n=== Тестирование производительности ===")
    
    import time
    
    # Создание большой матрицы
    size = 100
    start_time = time.time()
    big_matrix = Matrix(rows=size, cols=size, identity=True)
    creation_time = time.time() - start_time
    print(f"Создание единичной матрицы {size}x{size}: {creation_time:.4f} сек")
    
    # Операции с большими матрицами
    m1 = Matrix([[i+j for j in range(50)] for i in range(50)])
    m2 = Matrix([[i*j+1 for j in range(50)] for i in range(50)])
    
    start_time = time.time()
    result = m1 + m2
    add_time = time.time() - start_time
    print(f"Сложение матриц 50x50: {add_time:.4f} сек")
    
    start_time = time.time()
    det_result = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 10]]).det()
    det_time = time.time() - start_time
    print(f"Вычисление определителя 3x3: {det_time:.4f} сек, результат: {det_result}")

if __name__ == "__main__":
    try:
        test_matrix_creation()
        test_matrix_operations()
        test_matrix_properties()
        test_norms()
        test_helper_functions()
        test_performance()
        print("\n✅ Все тесты пройдены успешно!")
    except Exception as e:
        print(f"\n❌ Ошибка в тестах: {e}")
        raise
