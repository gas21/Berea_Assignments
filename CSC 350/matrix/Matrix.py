# MATRIX CLASS ASSIGNMENT


def dot(vec1, vec2):
    if len(vec1) != len(vec2):
        return -1
    return sum(i * j[0] for i, j in zip(vec1, vec2))


class Matrix:
    def __init__(self, matrix):

        assert all([isinstance(matrix, list), isinstance(matrix[0], list)])
        self.matrix = matrix
        self.num_col = len(matrix[0])
        self.num_row = len(matrix)

    def get_row(self, i):
        assert i <= self.num_row - 1
        return self.matrix[i]

    def get_col(self, j):
        assert j <= self.num_col - 1
        return [[self.matrix[i][j]] for i in range(self.num_row)]

    def add(self, other):
        assert len(self.matrix[0]) == len(other.matrix[0])
        assert len(self.matrix == len(other.matrix))
        return [i + j for k, l in zip(self.matrix, other.matrix) for i, j in zip(k, l)]

    def sub(self, other):
        assert len(self.matrix[0]) == len(other.matrix[0])
        assert len(self.matrix) == len(other.matrix)
        return [[i - j for i, j in zip(self.matrix[k], other.matrix[k])] for k in range(len(self.matrix))]

    def mult(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return [[i * other for i in j] for j in self.matrix]
        else:
            return [[dot(self.get_row(i), other.get_col(j)) for j in range(other.num_col)]
                    for i in range(self.num_row)]

    def transpose(self):
        return [list(a) for a in zip(*self.matrix)]


if __name__ == "__main__":
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    matrix3 = Matrix([[1], [0.1], [0.01]])
    print("Multiply2: " + str(matrix1.mult(matrix2)))
    print("Multiply3: " + str(matrix1.mult(matrix3)))
    print("Multiply0.5: " + str(matrix1.mult(0.5)))
    print("Transpose: " + str(matrix1.transpose()))
    print("Dot Helper: " + str(dot([1, 2, 3], [[10], [20], [30]])))

