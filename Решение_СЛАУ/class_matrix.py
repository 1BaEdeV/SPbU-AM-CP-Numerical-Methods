
class Matrix:
    def __init__(self, matr=[]):
        self.matrix = matr

    def dim(self):
        """Возвращает размерность матрицы в виде (n, m) - tuple.
        Если это вектор, корректно обрабатывает его."""

        rows = len(self.matrix)  # Количество строк

        # Проверка на вектор-строку или вектор-столбец
        if rows == 0:
            return (0, 0)  # Пустая матрица
        if isinstance(self.matrix[0], list):
            cols = len(self.matrix[0]) if rows > 0 else 0  # Количество столбцов в первой строке
        else:
            cols = 1  # Если первый элемент — не список, значит это вектор-столбец

        return rows, cols
    def add_row(self, row):
        """Добавление строки в матрицу"""
        self.matrix.append(row)
        return self
    def add_col(self, col):
        """Добавление столбуа в матрицу"""
        for i in range(len(self.matrix)):
            self.matrix[i].append(col[i])
        return self
    def add_matrix(self, matrix):
        """Добавление матрицы в пустой объект"""
        for i in range(len(matrix)):
            self.matrix.append(matrix[i])
        return self

    def PrintM(self):
        """Вывод матрицы с выравниванием, включая случай с вектором"""
        rows, cols = self.dim()  # Получаем размерность матрицы

        # Проверка на вектор-строку (одна строка) или вектор-столбец (один столбец)
        if rows == 1 or cols == 1:
            result = []
            for i in range(len(self.matrix)):
                result.append(self.matrix[i])
            print("".join(f"{num:3}" for num in result))
        else:
            # Обычный вывод матрицы
            for row in self.matrix:
                print(" ".join(f"{num:3}" for num in row))
    def getitem(self, type, idx=0):
        """Возвращает строку/столбец/элемент матрицы, raw-строка, сlm-столбец, elm-элемент"""
        if type == "raw":
            return self.matrix[idx]
        if type == "clm":
            result = []
            for i in range(len(self.matrix)):
                result.append(self.matrix[i][idx])
            return result
        if type == "dig":
            result = []
            for i in range(len(self.matrix)):
                result.append(self.matrix[i][i])
            return result
        if type == "elm":
            return self.matrix[idx[0]][idx[1]]

    def __eq__(self, other):
        """A==B - возвращает T/F"""
        return self.matrix == other.matrix
    def __ne__(self, other):
        """A!=B - возвращает T/F"""
        return self.matrix != other.matrix
    def __add__(self, other):
        """Сложение 2 матриц"""
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)

        return Matrix(result)
    def __sub__(self, other):
        """Разность 2 матриц"""
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return Matrix(result)
    def __mul__(self, other):
        """Умножение матрицы на скаляр или на матрицу этого же рзмера"""
        result = []
        if isinstance(other, Matrix):
            if self.dim() == other.dim():
                result=[]
                for i in range(len(self.matrix)):
                    rawr = self.getitem("raw", i)
                    rawrres = []
                    for j in range(len(self.matrix)):
                        rawrprom=rawr
                        sum=0
                        clmr = other.getitem("clm", j)
                        for l in range(len(self.matrix)):
                            sum += rawrprom[l]*clmr[l]
                        rawrres.append(sum)
                    result.append(rawrres)
                return Matrix(result)
        else:
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[i])):
                    row.append(self.matrix[i][j] * other)
                result.append(row)
            return Matrix(result)

    def E(self):
        "Единичная матрица размерности этой"
        result = []
        for i in range(len(self.matrix)):
            res = []
            for j in range(len(self.matrix[i])):
                if i == j:
                    res.append(1)
                else:
                    res.append(0)
            result.append(res)
        return Matrix(result)
    def norma1(self):
        """Вычисление единичной нормы матрицы(максимальная из сумм элементво по столбцам)"""
        res=[]
        for i in range(len(self.matrix)):
            clm = self.getitem("clm", i)
            res.append(sum(abs(clm[j]) for j in range(len(clm))))
        return max(res)
    def norma2(self):
        э


obj1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
obj2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
norm1=obj1.norma1()
obj1.PrintM()
print(norm1)