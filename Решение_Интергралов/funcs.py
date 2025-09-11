import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate


def f(x):
    return 3 * math.cos(0.5 * x) * math.exp(x / 4) + 5 * math.sin(2.5 * x) * math.exp(-x / 3) + 2 * x

def F(x):
    return f(x)*(3.2-x)**(-1/4)


def left_triangle(f, a, b, parts=100):
    res = 0
    for i in range(parts):
        lborder = a + i * (b - a) / parts
        rborder = a + (i + 1) * (b - a) / parts
        res += (rborder - lborder) * f(lborder)

    return res


def right_triangle(f, a, b, parts=100):
    res = 0
    for i in range(parts):
        lborder = a + i * (b - a) / parts
        rborder = a + (i + 1) * (b - a) / parts
        res += (rborder - lborder) * f(rborder)

    return res


def average_triangle(f, a, b, parts=100):
    res = 0
    for i in range(parts):
        lborder = a + i * (b - a) / parts
        rborder = a + (i + 1) * (b - a) / parts
        res += (rborder - lborder) * f((lborder + rborder) / 2)
    return res


def trapezoid(f, a, b, parts=100):
    res = 0
    for i in range(parts):
        lborder = a + i * (b - a) / parts
        rborder = a + (i + 1) * (b - a) / parts
        res += (rborder - lborder) * (f(rborder) + f(lborder)) / 2
    return res


def Simpson(f, a, b, parts=100):
    res = 0
    for i in range(parts):
        lborder = a + i * (b - a) / parts
        rborder = a + (i + 1) * (b - a) / parts
        res += (rborder - lborder) * (f(lborder) + 4 * f((lborder + rborder) / 2) + f(rborder)) / 6
    return res


def richardson(quad, f, a, b, alpha, beta, eps=1e-6, min_part=2, max_part=np.inf):
    """Метод Ричардсона с оценкой скорости сходимости по Эйткену"""
    r, R = 2, np.inf
    best_step, best_part = 0, 0
    interval_length = b - a

    while R > eps and 2 ** r * min_part <= max_part:
        # Вычисляем интегралы на последовательных сетках
        values = [quad(f, a, b, alpha, beta, parts=2 ** i * min_part) for i in range(r + 1)]
        # Оценка скорости сходимости по Эйткену
        m = -np.log((values[-1] - values[-2]) / (values[-2] - values[-3])) / np.log(2)
        print("изменение m ",m)
        steps = [interval_length / (2 ** i * min_part) for i in range(r + 1)]

        # Формируем матрицу для экстраполяции Ричардсона
        # Размер матрицы (r+1) x (r+1)
        step_matrix = []
        for j in range(r + 1):  # по строкам
            row = [-1]  # первый элемент строки всегда -1
            for i in range(r):  # по столбцам (кроме первого)
                element = steps[j] ** (m + i)
                row.append(element)
            step_matrix.append(row)

        # Преобразуем в numpy массивы
        step_matrix = np.array(step_matrix)
        values_vec = np.array(values)

        # Уточнение по Ричардсону
        J = np.linalg.solve(step_matrix, -values_vec)
        toch, error=integrate.quad(F,a,b)
        cur_R = abs(J[0] - toch)
        if cur_R < R:
            best_part = int(interval_length / steps[-1])
            best_step = steps[-1]
            R = cur_R
        r += 1
    print("r= ",r)
    return R, best_step, best_part


def calc_h_opt(quad, f,a,b,alpha,beta,h_list3,eps = 1e-6):
    values = [quad(f, a, b, alpha, beta, i) for i in h_list3]
    m = -np.log((values[-1] - values[-2]) / (values[-2] - values[-3])) / np.log(2)
    h_opt = h_list3[0] * (eps * (1 - 2 ** (-m)) / abs(values[0] - values[1])) ** (1 / m)
    return h_opt



def plot_error_vs_partitions(flag,f,methods_dict, exact_value, a, b, al,bet, max_parts=1000, step=1):
    """
    Строит график зависимости абсолютной погрешности от количества разбиений
    для различных квадратурных формул.

    Параметры:
    methods_dict - словарь {название_метода: функция_метода}
    exact_value - точное значение интеграла
    a, b - границы интегрирования
    max_parts - максимальное количество разбиений
    step - шаг увеличения количества разбиений
    """

    # Создаем массив количества разбиений
    partitions = list(range(step, max_parts + 1, step))

    plt.figure()

    # Для каждого метода вычисляем погрешности
    for method_name, method_func in methods_dict.items():
        errors = []

        for parts in partitions:
            # Вычисляем приближенное значение интеграла
            if flag == 1:
                approx_value = method_func(f, a, b, parts)
            if flag == 2:
                approx_value = method_func(f, a, b, al, bet, parts)
            # Вычисляем абсолютную погрешность
            error = abs(exact_value - approx_value)
            errors.append(error)

        # Строим график для данного метода
        plt.semilogy(partitions, errors, '--', label=method_name, linewidth=2, markersize=4)

    plt.xlabel('Количество разбиений', fontsize=12)
    plt.ylabel('Абсолютная погрешность (логарифмическая шкала)', fontsize=12)
    plt.title('Зависимость абсолютной погрешности от количества разбиений', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def compare_integration_methods(flag,f,methods,a=0, b=2, al=0,bet=0, exact_value=None, max_parts=1000):
    """
    Сравнивает все доступные методы интегрирования для функции f(x).

    Параметры:
    a, b - границы интегрирования
    exact_value - точное значение интеграла (если известно)
    max_parts - максимальное количество разбиений для анализа
    """

    # Если точное значение не задано, вычисляем его с высокой точностью
    if exact_value is None:
        # Используем метод Симпсона с большим количеством разбиений как эталон
        if flag ==1:
            exact_value, error = integrate.quad(f, a, b, )
        if flag ==2:
            exact_value, error = integrate.quad(F, a, b )
        print(f"Точное значение интеграла (вычислено): {exact_value}")
    else:
        print(f"Точное значение интеграла: {exact_value}")


    # Строим график сравнения
    plot_error_vs_partitions(flag,f,methods, exact_value, a, b,al,bet ,max_parts)

    # Выводим численные результаты для нескольких значений разбиений
    test_partitions = [10, 50, 100]
    print("\nСравнение методов для различного количества разбиений:")
    print(f"{'Метод':<25} {'n=10':<15} {'n=50':<15} {'n=100':<15}")
    print("-" * 70)

    for method_name, method_func in methods.items():
        results = []
        for parts in test_partitions:
            if flag == 1:
                approx = method_func(f, a, b, parts)
            if flag == 2:
                approx = method_func(f, a, b, al, bet, parts)
            error = abs(exact_value - approx)
            results.append(f"{error:.2e}")

        print(f"{method_name:<25} {results[0]:<15} {results[1]:<15} {results[2]:<15}")
