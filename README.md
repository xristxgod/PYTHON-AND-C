# Python + C

> This repository shows how to use the C language with pit. I use the library: `ctypes`
------
### Let's write a function in C language.
[`C code`](example/main.c) 
> Regular iterator. We get the sum from the number `100_000_000`.
```c
#include <stdio.h>


int test_function() {
    long int num = 0;
    long int value = 100000000;
    int result = 0;

    while (num < value) {
        result++;
        num++;
    };
    return result;
};
```

-----
### Next, let's compile the code.
```shell
# For linux
>>> gcc -shared -Wl, -soname, adder -o test_lib.so -fPIC main.c
# For windows
>>> gcc -shared -Wl, -soname, adder -o test_lib.dll -fPIC main.c
```

-----
### Let's call it in python
[`Python code`](example/main.py) 
```python
import os
# Lib for use C code in Python
from ctypes import CDLL


# Take C module in Windows. Use "test_lib.so" for linux
LIB = CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_lib.dll"))


def test_function() -> int:
    # Call iterator
    return LIB.test_function()


if __name__ == '__main__':
    # Call function
    print("Result: ", test_function())
```
#### Return body:
```shell
>>> python3 main.py
...
>>> Result: 4999999950000000
```

-----
> The question arises, why? And the answer will be banal language C is much faster than python. 
> The C code will be executed in just 1 second, when it takes at least 10-18 seconds in Python.
> You can conveniently and most importantly effectively use the two languages together.
