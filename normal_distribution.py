#aidan's code
import math

TOLERANCE = 1e-8

def f(t):
    return math.exp(-t ** 2 / 2) / math.sqrt(2 * math.pi)

def choose_n(z, tol = TOLERANCE):
    K = 3 / math.sqrt(2 * math.pi)
    n = math.ceil((K * z ** 5 / (180 * tol)) ** 0.25)
    n = max(n, 2)
    if n % 2 == 1:
        n += 1
    return n

def simpson(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's Rule")
    h = (b - a) / n
    total = func(a) + func(b)
    for i in range(1 , n):
        total += (4 if i % 2 == 1 else 2) * func(a + i * h)
    return total * h / 3

def normal_area(z):
    if z == 0:
        return 0.0, 0
    sign = 1 if z > 0 else -1
    n = choose_n(abs(z))
    return sign * simpson(f, 0, abs(z), n), n


def main():
    while True:
        raw = input("Enter a z-score (or 'q' to quit): ").strip()
        if raw.lower() in ("q", "quit", ""):
            break
        try:
            z = float(raw)
        except ValueError:
            print(" Please enter a number. \n")
            continue
        area, n = normal_area(z)
        print(f" Subintervals used (n) : {n}")
        print(f" Area from 0 to z      : {area:.5f}")

if __name__ == "__main__":
    main()
