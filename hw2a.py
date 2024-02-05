import math


def Probability(PDF, args, c, GT=True):
    """In this function, we are defining the probability of a function being less or equal to a certain
    variable. 'PDF' is the probability density function of the variable. 'args' is the tuple, which are the
    of the 'PDF.' 'c' is the float of the variable. 'GT' is the Boolean of the variable."""
    def integrate_simpsons13(func, a, b, N=1000):
        """In this function, we are defining how we are going to integrate using Simpson's 1/3rd rule. 'func' is
        the function to be integrated. 'a' is the upper limit, while 'b' is the lower limit. 'N' is the number of
        intervals for the integration. This is going to output the numerical approximation for the integral."""
        h = (b - a) / N
        x_values = [a + i * h for i in range(N + 1)]
        y_values = [func(x, *args) for x in x_values]
        integral = h / 3 * sum(y_values[i - 1] + 4 * y_values[i] + y_values[i + 1] for i in range(1, N, 2))
        return integral

    mu, sigma = args

    if GT:
        a = mu - 5 * sigma
        b = c
    else:
        a = mu - 5 * sigma
        b = mu + 5 * sigma

    result = integrate_simpsons13(PDF, a, b)

    return result


def normal_pdf(x, mu, sigma):
    """This function calculates the probability density function of a normal distribution at a given point.
    'x' is the point where we are evaluating the PDF. 'mu' is the mean of the normal distribution. 'sigma'
    is the standard deviation of the normal distribution."""
    return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu) ** 2 / (2 * sigma ** 2))


def main():
    """This function runs the whole process. It is going to use everything else we have defined to print
    out the calculated probabilities for specific events."""
    result1 = Probability(normal_pdf, (100, 12.5), 105, GT=False)
    print(f'P(x<105|N(100,12.5)) = {result1:.2f}')

    result2 = Probability(normal_pdf, (100, 3), 100 + 2 * 3, GT=True)
    print(f'P(x>{100 + 2 * 3}|N(100,3)) = {result2:.2f}')


if __name__ == "__main__":
    main()
