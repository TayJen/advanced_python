from matrix_3_1 import CustomMatrix
from matrix_3_2 import AllStandardOperationsMixin


hash_cache = {}


class HashMixin:
    def __hash__(self):
        hash = 0
        for row in self.val.matrix:
            for elem in row:
                hash += elem
        return int(hash)


class ProMatrix(HashMixin, AllStandardOperationsMixin):
    def __init__(self, val):
        super().__init__(CustomMatrix(val))

    def __matmul__(self, other):
        hash_0 = hash(self)
        hash_1 = hash(other)

        if (hash_0, hash_1) in hash_cache:
            return hash_cache[(hash_0, hash_1)]

        ans = ProMatrix(super().__matmul__(other).val.matrix)
        hash_cache[(hash_0, hash_1)] = ans

        return ans


if __name__ == '__main__':
    A = ProMatrix([[1, 2, 3], [4, 5, 6]])
    C = ProMatrix([[4, 5, 6], [3, 3, 0]])
    B = ProMatrix([[-1, 1], [2, -2], [3, -3]])
    D = ProMatrix([[-1, 1], [2, -2], [3, -3]])

    A.save_to_file('./artifacts/3.3/A.txt')
    B.save_to_file('./artifacts/3.3/B.txt')
    C.save_to_file('./artifacts/3.3/C.txt')
    D.save_to_file('./artifacts/3.3/D.txt')

    (C @ D).save_to_file('./artifacts/3.3/CD.txt')
    (A @ B).save_to_file('./artifacts/3.3/AB.txt')
    with open('./artifacts/3.3/hash.txt', 'w') as hash_file:
        hash_file.write('AB: ' + str(hash(A @ B)) + ' CD: ' + str(hash(C @ D)))
