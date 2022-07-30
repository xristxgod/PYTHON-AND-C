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
