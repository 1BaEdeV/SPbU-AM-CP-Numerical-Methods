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