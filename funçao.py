import math


def trapezios_simples(f, c, d):
    if c > d:
        print("Limites não aceites")
        return None
    else:
        return (d - c) * (f(c) + f(d)) / 2


f1 = lambda x: x ** 2
print(trapezios_simples(f1, 0, 1))


def trapezio_recursivo(f, c, d, n):
    if n == 0:
        return trapezios_simples(f, c, d)
    else:
        metade = (c + d) / 2
        return trapezio_recursivo(f, c, metade, n - 1) + trapezio_recursivo(f, metade, d, n - 1)


def trapezio_iterativo(f, c, d, n):
    if c > d:
        print("Limite inferior tem que ser menor que o limite superior")
        return None
    h = (d - c) / n
    area_total = 0
    for i in range(n):
        lim_i = c + (h * i)
        lim_s = lim_i + h
        area_total += trapezios_simples(f, lim_i, lim_s)
    return area_total


def brute_force(f, c, d, max_iter=100):
    contador = 2
    while contador < max_iter:
        t = trapezio_iterativo(f, c, d, contador)
        t_anterior = trapezio_recursivo(f, c, d, contador - 1)
        if t == t_anterior:
            return f"{t} quando n={contador}"  # encontrou o valor onde Tn == Tn-1
        contador += 1
    return None  # não encontrou nada


print(brute_force(f1, 0, 2))


def simspon_simples(f, c, d):
    if c > d:
        print("Limite inferior tem que ser menor que o limite superior")
        return None
    m = (c + d) / 2
    return (d - c) * (f(c) + 4 * f(m) + f(d)) / 6


print(simspon_simples(f1, 0, 2))


def simpson_iterativo(f, c, d, n):
    if c > d:
        print("Limite inferior tem que ser menor que o limite superior")
        return None
    if n == 0:
        return simspon_simples(f, c, d)
    else:
        m = (c + d) / 2
        return simpson_iterativo(f, c, m, n - 1) + simpson_iterativo(f, m, d, n - 1)


def integral_dinamica(f, c, d, epsilon=1e-6):
    n = 1
    while True:
        T_n = trapezio_iterativo(f, c, d, n)
        S_n = simpson_iterativo(f, c, d, n)

        if abs(T_n - S_n) < epsilon:
            return S_n

        n *= 2


resultado = integral_dinamica(f1, 0, 1, 0.01)
print("Resultado da integral:", resultado)


def greedy(f, c, d, epsilon=1e-6):
    T_anterior = trapezio_iterativo(f, c, d, 1)
    for n in range(1, 30):
        T_novo = trapezio_iterativo(f, c, d, n)
        S_novo = simpson_iterativo(f, c, d, n)
        if abs(T_novo - T_anterior) < epsilon and abs(T_novo - S_novo) < epsilon:
            return T_novo
        T_anterior = T_novo
    return None
