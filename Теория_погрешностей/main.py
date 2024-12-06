from prettytable import PrettyTable
import math

# Заданная погрешность
eps = 0.000001

# Вычисленная погрешность иперболического синуса
eps_sh = (0.000001) / (2 * 2.5)

# Вычисленная погрешность синусa
eps_sin = (0.000001) / (2 * 13.7)

# Вычисленная методическая погрешность корня
eps_sqrtt = (0.0000001) / 2.3


def sh(x):
    # Разложение гиперболического синуса в ряд Тейлора
    val = 0
    n = 0
    while True:
        val_ = val + x**(2 * n + 1) / math.factorial(2 * n + 1)
        if abs(val_ - val) < eps_sh:
            return val_
        val = val_
        n += 1


def sin(x):
    # Разложение синуса в ряд Тейлора
    val = 0
    n = 0
    while True:
        val_ = val + (-1)**n * x**(2 * n + 1) / math.factorial(2 * n + 1)
        if abs(val_ - val) < eps_sin:
            return val_
        val = val_
        n += 1


def sqrtt(x):
    # Разложение корня по формуле Герона
    eps = (0.000001) / 3
    val = 1
    n = 0
    while True:
        val_ = 0.5 * (val + x / val)
        if abs(val_ - val) < eps:
            return val_
        val = val_
        n += 1
    return 0


def insertTOtable(a, c, b):
    x = a
    while x + c <= b:
        mas = []
        x += c
        x = round(x, 3)

        psi = sqrtt(1 + x**2) / (1 - x)
        psi_ = math.sqrt(1 + x** 2) / (1 - x)

        phi = sh(sqrtt(1 + x** 2) / (1 - x))
        phi_ = math.sinh(math.sqrt(1 + x**  2) / (1 - x))

        g = sin(x**  2 + 0.4)
        g_ = math.sin(x ** 2 + 0.4)

        f = phi / g
        f_ = phi_ / g_

        mas.append(x)

        mas.append(psi)
        mas.append(eps_sqrtt)
        mas.append(psi_)
        mas.append(abs(psi_ - psi))

        mas.append(phi)
        mas.append(eps_sh)
        mas.append(phi_)
        mas.append(abs(phi_ - phi))

        mas.append(g)
        mas.append(eps_sin)
        mas.append(g_)
        mas.append(abs(g_ - g))

        mas.append(f)
        mas.append(eps)
        mas.append(f_)
        mas.append(abs(f_ - f))

        MAS.append(mas)


# Итоговые значения
x = PrettyTable()

columns = ["x", "psi(x)", "d_psi", "bi_psi(x)", "bi_d_psi",
           "phi(x)", "d_phi", "bi_phi(x)", "bi_d_phi",
           "g(x)", "d_g", "bi_g(x)", "bi_d_g",
           "f(x)", "d_f", "bi_f(x)", "bi_d_f"]
x.field_names = columns
MAS = []
insertTOtable(0.01, 0.005, 0.06)
for exp in MAS:
    x.add_row(exp)
print(x)