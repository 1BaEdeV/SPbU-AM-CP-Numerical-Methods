import math

def create_identity_matrix(n):
    """Создаёт единичную матрицу размера n x n."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def matrix_mult(A, B):
    """Перемножает две матрицы A и B."""
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def transpose_matrix(A):
    """Транспонирует матрицу A."""
    n = len(A)
    return [[A[j][i] for j in range(n)] for i in range(n)]

def norm(vector):
    """Возвращает евклидову норму вектора."""
    return math.sqrt(sum(x ** 2 for x in vector))

def householder_hessenberg(A):
    """Приводит матрицу A к форме Хессенберга методом Хаусхолдера."""
    n = len(A)

    for k in range(n - 2):
        # Берём поддиагональный столбец
        x = [A[i][k] for i in range(k + 1, n)]
        e1 = [0] * len(x)
        e1[0] = norm(x) * (1 if x[0] >= 0 else -1)  # Выбираем знак

        # Вычисляем отражающий вектор v
        v = [x[i] + e1[i] for i in range(len(x))]
        v_norm = norm(v)
        if v_norm == 0:  # Избегаем деления на 0
            continue
        v = [v_i / v_norm for v_i in v]

        # Формируем матрицу Хаусхолдера H_k = I - 2 v v^T
        H_k = create_identity_matrix(n)
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                H_k[i][j] -= 2 * v[i - (k + 1)] * v[j - (k + 1)]

        # Применяем преобразование A' = H_k A H_k^T
        A = matrix_mult(H_k, A)
        A = matrix_mult(A, transpose_matrix(H_k))

    return A

# 🔹 Пример
A = [[4, 1, -2, 2],
     [1, 2, 0, 1],
     [-2, 0, 3, -2],
     [2, 1, -2, -1]]

Hessenberg_A = householder_hessenberg(A)

print("Матрица в форме Хессенберга:")
for row in Hessenberg_A:
    print(row)