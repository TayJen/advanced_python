import numpy as np
from numbers import Number
from matrix_3_1 import CustomMatrix


class SaveFileMixin:
    def save_to_file(self, filename: str):
        with open(filename, 'w') as f:
            f.write(f"{str(self)}\n")


class StrMixin:
    def __str__(self):
        return str(self.val)


class SetGetMixin:
    def get(self):
        return self.val

    def set(self, val):
        self.val = val


class AllStandardOperationsMixin(np.lib.mixins.NDArrayOperatorsMixin, SaveFileMixin, StrMixin, SetGetMixin):
    def __init__(self, val):
        self.val = val

    _HANDLED_TYPES = (np.ndarray, Number, CustomMatrix)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (AllStandardOperationsMixin,)):
                return NotImplemented

        inputs = tuple(x.val if isinstance(x, AllStandardOperationsMixin) else x for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.val if isinstance(x, AllStandardOperationsMixin) else x
                for x in out
            )
        s = getattr(ufunc, method)
        result = s(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)

    def __matmul__(self, other):
        return AllStandardOperationsMixin(self.val @ other.get())



if __name__ == "__main__":
    np.random.seed(0)
    a = AllStandardOperationsMixin(CustomMatrix(np.random.randint(0, 10, (10, 10)).tolist()))
    b = AllStandardOperationsMixin(CustomMatrix(np.random.randint(0, 10, (10, 10)).tolist()))

    c = a + b
    c.save_to_file('./artifacts/3.2/matrix_add.txt')

    d = a * b
    d.save_to_file('./artifacts/3.2/matrix_mul.txt')

    e = a @ b
    e.save_to_file('./artifacts/3.2/matrix_matmul.txt')
