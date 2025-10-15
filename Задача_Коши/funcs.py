import numpy as np
from copy import deepcopy

def diffur(x,y):
    dy = np.array([y[1]/20,-y[0]/25])
    return dy

def compact_list(a: list or np.ndarray, length: int) -> list:
    """Сжимаем список до заданной длины length"""
    return [np.mean(a[i * len(a) // length: (i + 1) * len(a) // length]) for i in range(length)]

def real_y(x_start: float, y_start: np.ndarray, x_end: float) -> np.ndarray:
    """Реальное решение задачи Коши"""
    A = 1/20
    B = 1/25
    omega = np.sqrt(A * B)
    
    dx = x_end - x_start
    arg = omega * dx
    
    # Начальные условия
    y1_0, y2_0 = y_start
    
    # Решение через начальные условия
    y1_end = y1_0 * np.cos(arg) + (A * y2_0 / omega) * np.sin(arg)
    y2_end = y2_0 * np.cos(arg) - (omega * y1_0 / A) * np.sin(arg)
    
    return np.array([y1_end, y2_end])



def runge_kutta_4(f, x: float, y: np.ndarray, xend: float, h: float) -> tuple:
    """Один шаг метода Рунге-Кутты 4-го порядка"""
    calcs = 0
    x_curr = x
    y_curr = y.copy()
    
    while x_curr < xend:
        h = min(h, xend - x_curr)
        
        k1 = f(x_curr, y_curr)
        k2 = f(x_curr + 0.5 * h, y_curr + 0.5 * h * k1)
        k3 = f(x_curr + 0.5 * h, y_curr + 0.5 * h * k2)
        k4 = f(x_curr + h, y_curr + h * k3)
        
        y_curr = y_curr + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x_curr += h
        calcs += 4
    
    return y_curr, calcs

def runge_kutta_2(f, x: float, y: np.ndarray, xend: float, h: float) -> tuple:
    """Один шаг метода Рунге-Кутты 2-го порядка (метод трапеций)"""
    zeta = 1/19
    a = zeta
    c = zeta
    b = np.array([1 - 1/(2*zeta), 1/(2*zeta)])
    
    calcs = 0
    x_curr = x
    y_curr = y.copy()
    
    while x_curr < xend:
        h = min(h, xend - x_curr)
        
        k1 = f(x_curr, y_curr)
        k2 = f(x_curr + h * c, y_curr + a * h * k1)
        
        y_curr = y_curr + h * (b[0] * k1 + b[1] * k2)
        x_curr += h
        calcs += 2
    
    return y_curr, calcs 

def call(f, xst: float, yst: np.ndarray, xend: float, step: float = None, method: str = 'rk4', stepsetting: str = 'adaptive', eps = 1e-4, max_steps: int = 1000) -> np.ndarray:
    
    if method == 'rk4':
        step_method = runge_kutta_4
        degree = 4
    elif method == 'rk2':
        step_method = runge_kutta_2
        degree = 2
        
    if step is None:
        delta = 1 / max(abs(xst), abs(xend)) ** (degree + 1) + np.linalg.norm(yst) ** (degree + 1)
        step = (eps / delta) ** (1 / (degree + 1))

    # Минимальный шаг для избежания бесконечного цикла
    min_step = 1e-10
    step = max(step, min_step)
    
    x_curr, y_curr = deepcopy(xst), deepcopy(yst)
    
    calc_count = 0
    values = [y_curr.copy()]
    x_values = [x_curr]
    local_errors = []
    steps = []
    
    step_attempts = 0
    
    # Режим без контроля шага
    if stepsetting == 'none':
        y_final, calcs = step_method(f, x_curr, y_curr, xend, step)
        return y_final, [], [step], calcs
    
    # Режим постоянного шага
    elif stepsetting == 'const':
        while x_curr < xend and step_attempts < max_steps:
            step_attempts += 1
            
            # Вычисляем с полным шагом и половинным шагом
            y_full, calcs_full = step_method(f, x_curr, y_curr, xend, step)
            y_half, calcs_half = step_method(f, x_curr, y_curr, xend, step/2)
            calc_count += calcs_full + calcs_half
            
            # Оценка ошибки по Рунге
            error = np.linalg.norm(y_half - y_full) / (1 - 2 ** -degree)
            
            if error < eps:
                return y_full , error, step, calc_count
            
            if step_attempts >= max_steps:
                print("Warning: Maximum step attempts reached in const mode")
                break
            step = step / 2

    # Метод автоматического выбора шага
    elif stepsetting == 'adaptive':
        calcs_whole = 0
        calcs_h = 0
        while x_curr < xend:
            step_attempts += 1
            step = min(step, xend - x_curr)  # Если шаг вылетает за пределы, то возвращаем его

            # один полный шаг
            y_whole, calcs_whole = step_method(f, x_curr, y_curr, x_curr+step, step)
            y_half, calcs_h = step_method(f, x_curr, y_curr, x_curr+step, step/2)
            calc_count += calcs_whole + calcs_h
            local_error = (y_half - y_whole) / (1 - 2 ** -degree)
            error_norm = np.linalg.norm(local_error)

            # Критерии выбора шага
            if error_norm > 2 ** degree * eps:
                step = step / 2
            elif eps < error_norm < 2 ** degree * eps:
                x_curr = x_curr + step
                y_curr = y_half
                values.append(y_curr)
                local_errors.append(error_norm)
                steps.append(step)
                step = step / 2
            elif eps / 2 ** (degree + 1) < error_norm < eps:
                x_curr = x_curr + step
                y_curr = y_whole
                values.append(y_curr)
                local_errors.append(error_norm)
                steps.append(step)

            else:
                x_curr = x_curr + step
                y_curr = y_whole
                values.append(y_curr)
                local_errors.append(error_norm)
                steps.append(step)
                step = 2 * step

    final = values[-1] if len(values) > 0 else y_curr
    return final, local_errors, steps, calc_count
