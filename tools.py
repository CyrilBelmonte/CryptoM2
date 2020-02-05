def lpowmod(x, y, n):
    """puissance modulaire: (x**y)%n avec x, y et n entiers"""
    result = 1
    while y > 0:
        if y & 1 > 0:
            result = (result * x) % n
        y >>= 1
        x = (x * x) % n
    return result


def lpow(x, y):
    """Calcul rapide de la puissance entière avec x et y entiers """
    result = 1
    while y != 0:
        if y & 1 == 1:  # si y impair
            result *= x
            y -= 1
        else:  # y est pair
            x *= x
            y >>= 1
    return result


def igcd(a, b):
    # Initialisation
    d, u, v, d1, u1, v1 = a, 1, 0, b, 0, 1
    # Calcul
    while d1 != 0:
        q = d // d1
        d, u, v, d1, u1, v1 = d1, u1, v1, d - q * d1, u - q * u1, v - q * v1
    return (d, u, v)


def find_n(a, p, remainder):
    n = 0
    r = (a * n) % p
    while r != remainder:
        n += 1
        r = (a * n) % p
        print("a * ", n, " = ", r, " mod ", p)
    return n, r
