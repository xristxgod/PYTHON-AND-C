import os
from ctypes import CDLL


LIB = CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_lib.dll"))


def test_function() -> int:
    return LIB.test_function()


if __name__ == '__main__':
    print(test_function())