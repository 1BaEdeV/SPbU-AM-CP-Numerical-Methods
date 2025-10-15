def call(f, xst: float, yst: np.ndarray, xend: float, step: float = None, method: str = 'rk4', stepsetting: str = 'adaptive', eps = 1e-4) -> np.ndarray:
    if method == 'rk4':
        step_method = runge_kutta_4
        degree = 4
    elif method == 'rk2':
        step_method = runge_kutta_2
        degree = 2
        
    if step is None:
        delta = 1 / max(abs(xst), abs(xend)) ** (degree + 1) + np.linalg.norm(yst) ** (degree + 1)
        step = (eps / delta) ** (1 / (degree + 1))

    x_curr, y_curr = deepcopy(xst), deepcopy(yst)
    x_curr = float(x_curr)
    y_curr = np.asarray(y_curr, dtype=float)

    calc_count = 0  # Количество вычислений f(x, y)
    values = []  # Список последовательно высчитанных значений
    local_errors = []  # Список локальных погрешностей
    steps = []  # Список шагов

    if stepsetting == 'none':
        while x_curr < xend:
            if x_curr + step > xend:
                step = xend - x_curr
            y_curr, calcs = step_method(f, x_curr, y_curr, step)
            x_curr += step
            calc_count += calcs
            values.append(y_curr)
            steps.append(step)
            local_errors.append(0)
    
    # Метод постоянного шага
    elif stepsetting == 'const':
        while True:
            # один полный шаг
            y_whole, calcs_whole = step_method(f, x_curr, y_curr, step)
            # два полу-шага подряд для оценки
            y_half1, calcs_h1 = step_method(f, x_curr, y_curr, step/2)
            y_half2, calcs_h2 = step_method(f, x_curr + step/2, y_half1, step/2)

            calc_count += calcs_whole + calcs_h1 + calcs_h2

            # Считаем погрешность по методу Рунге
            error = (y_half2 - y_whole) / (1 - 2 ** -degree)
            error_norm = np.linalg.norm(error)

            if error_norm < eps:
                x_curr += step
                y_curr = y_half2
                values.append(y_curr)
                steps.append(step)
                local_errors.append(error_norm)
                if x_curr >= xend:
                    break
                continue

            step = step / 2

    return values[-1] if values else y_curr, local_errors, steps, calc_count