def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """This function will use the secant method to find the roots of a given function. 'fcn' is the
    function where the root is. 'x0' is the first initial guess, and 'x1' is the second initial guess.
    'maxiter' is the minimum number of iterations. 'xtol' is the tolerance for the convergence. The
    output is going to be the approximation of the roots."""
    iter_count = 0
    x_prev = x0
    x_curr = x1

    while iter_count < maxiter:

        x_next = x_curr - fcn(x_curr) * (x_curr - x_prev) / (fcn(x_curr) - fcn(x_prev))

        if abs(x_next - x_curr) < xtol:
            return x_next

        x_prev = x_curr
        x_curr = x_next

        iter_count += 1

    return x_curr


def main():
    """This function is going to use everything that we have defined to run the secant method, and
    it is going to output the solutions for the 3 specific examples."""

    result1 = Secant(lambda x: x ** 2 - 2, 1, 2, maxiter=5, xtol=1e-4)
    print(f'Solution 1: {result1:.5f}')

    result2 = Secant(lambda x: x ** 2 - 2, 1, 2, maxiter=15, xtol=1e-8)
    print(f'Solution 2: {result2:.8f}')

    result3 = Secant(lambda x: x ** 2 - 2, 1, 2, maxiter=3, xtol=1e-8)
    print(f'Solution 3: {result3:.8f}')


if __name__ == "__main__":
    main()
