def sqrtt(x):
    """ Разложение корня по формуле Герона """
    eps = (0.000001) / 3
    val = 1
    n = 0
    while True:
        val_ = 0.5*(val+x/val)
        if abs(val_ - val) < eps:
            return val_
        val = val_
        n += 1
    return 0

def is_2d_array(arr):
    # Проверяем, является ли arr списком
    if isinstance(arr, list):
        # Проверяем, что каждый элемент arr также является списком
        return all(isinstance(row, list) for row in arr)
    return False


def is_vector(matrix):
    """Проверяет, является ли матрица вектором, где первый столбец содержит элементы,
    а остальные столбцы заполнены нулями."""

    # Проверка на пустую матрицу
    if not matrix or not matrix[0]:
        return False

    # Получаем количество строк и столбцов
    rows = len(matrix)
    cols = len(matrix[0])

    # Проверка, что все строки имеют одинаковую длину
    for row in matrix:
        if len(row) != cols:
            return False

    # Проверка первого столбца и остальных столбцов
    for i in range(rows):
        if matrix[i][0] != 0 and any(matrix[i][j] != 0 for j in range(1, cols)):
            return False  # Если первый элемент не равен нулю, а есть ненулевые элементы в других столбцах
        if matrix[i][0] == 0 and any(matrix[i][j] != 0 for j in range(cols)):
            return False  # Если первый элемент равен нулю, но есть ненулевые элементы в других столбцах

    # Если все проверки пройдены, матрица является вектором
    return True


