def GaussSeidel(Aaug, x, Niter=15):
    """
    Use the Gauss-Seidel method to estimate the solution to a set of linear equations expressed in matrix form.

    Parameters:
    - Aaug: list of lists, an augmented matrix containing [A | b] having N rows and N+1 columns.
    - x: list, a vector (array) containing the values of the initial guess.
    - Niter: int, the number of iterations (new x vectors) to compute. Default is 15.

    Returns:
    - list: the final new x vector.
    """
    rows, cols = len(Aaug), len(Aaug[0]) - 1

    for _ in range(Niter):
        for i in range(rows):
            sigma = sum(Aaug[i][j] * x[j] for j in range(cols) if j != i)
            x[i] = (Aaug[i][cols] - sigma) / Aaug[i][i]

    return x


Aaug1 = [
    [3, 1, -1, 2],
    [1, 4, 1, 12],
    [2, 1, 2, 10]
]

Aaug2 = [
    [1, -10, 2, 4, 2],
    [3, 1, 4, 12, 12],
    [9, 2, 3, 4, 21],
    [-1, 2, 7, 3, 37]
]

initial_guess1 = [0, 0, 0]
initial_guess2 = [0, 0, 0, 0]
iterations = 15

result1 = GaussSeidel(Aaug1, initial_guess1.copy(), Niter=iterations)
result2 = GaussSeidel(Aaug2, initial_guess2.copy(), Niter=iterations)

print("Final solution for Matrix 1:", result1)
print("Final solution for Matrix 2:", result2)
