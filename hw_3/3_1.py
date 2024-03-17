import numpy as np


class CustomMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.shape = (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other_matrix):
        if self.shape != other_matrix.shape:
            raise ValueError("matrix must have the same shape")

        result = [
            [self.matrix[i][j] + other_matrix.matrix[i][j] for j in range(self.shape[1])] 
            for i in range(self.shape[0])
        ]

        return CustomMatrix(result)

    def __mul__(self, other_matrix):
        if self.shape != other_matrix.shape:
            raise ValueError("matrix must have the same shape")

        result = [
            [self.matrix[i][j] * other_matrix.matrix[i][j] for j in range(self.shape[1])] 
            for i in range(self.shape[0])
        ]

        return CustomMatrix(result)

    def __matmul__(self, other_matrix):
        if self.shape[1] != other_matrix.shape[0]:
            raise ValueError("matrix must be compatible for matrix multiplication")

        result = []
        for i in range(self.shape[0]):
            a = []
            for j in range(self.shape[1]):
                a.append(0)
            result.append(a)

        for i in range(self.shape[0]):
            for j in range(other_matrix.shape[1]):
                for k in range(self.shape[1]):
                    result[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]

        return CustomMatrix(result)

    def __str__(self):
        s = ""
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                s = s + f' {self.matrix[i][j]:5}'
            s = s + '\n'
        return s


if __name__ == "__main__":
    np.random.seed(0)
    a = CustomMatrix(np.random.randint(0, 10, (10, 10)).tolist())
    b = CustomMatrix(np.random.randint(0, 10, (10, 10)).tolist())

    with open('./artifacts/3.1/matrix_add.txt', 'w') as f_add:
        f_add.write(str(a + b))

    with open('./artifacts/3.1/matrix_mul.txt', 'w') as f_mul:
        f_mul.write(str(a * b))
    
    with open('./artifacts/3.1/matrix_matmul.txt', 'w') as f_matmul:
        f_matmul.write(str(a @ b))
