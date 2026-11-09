"""
Standard normal area (mean to z) using Simpson's Rule.

Approximates   A(z) = integral from 0 to z of  e^(-t^2/2) / sqrt(2*pi)  dt
and reports    P(Z <= z) = 0.5 + A(z).
"""

import math

TOLERANCE = 1e-8   # demanded error bound (tight enough that rounding to 5 decimals is reliable)


def f(t):
    """Standard normal density: e^(-t^2/2) / sqrt(2*pi)."""
    return math.exp(-t * t / 2) / math.sqrt(2 * math.pi)


def choose_n(z, tol=TOLERANCE):
    """
    Smallest EVEN n guaranteeing Simpson error <= tol.
    Error bound: E_S <= K (b-a)^5 / (180 n^4), with a = 0, b = z.
    For f(t) = phi(t), the 4th derivative is (t^4 - 6t^2 + 3) phi(t), whose
    largest absolute value on any interval starting at 0 is K = 3/sqrt(2*pi).
    """
    K = 3 / math.sqrt(2 * math.pi)
    n = math.ceil((K * z ** 5 / (180 * tol)) ** 0.25)
    n = max(n, 2)
    if n % 2 == 1:          # Simpson's Rule needs an even number of subintervals
        n += 1
    return n


def simpson(func, a, b, n):
    """Simpson's Rule with n (even) subintervals."""
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's Rule")
    h = (b - a) / n
    total = func(a) + func(b)
    for i in range(1, n):
        total += (4 if i % 2 == 1 else 2) * func(a + i * h)
    return total * h / 3


def normal_area(z):
    """Area under the standard normal curve from 0 to z (z may be negative)."""
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
            print("  Please enter a number.\n")
            continue

        area, n = normal_area(z)
        print(f"  Subintervals used (n)     : {n}")
        print(f"  Area from 0 to z          : {area:.5f}")
        print(f"  P(Z <= z)  (= 0.5 + area) : {0.5 + area:.5f}\n")


if __name__ == "__main__":
    main()