#!/usr/bin/env python3

def sumup(n):
    if n == 0:
        return 0

    sum_to_n_minus = sumup(n - 1)
    return n + sum_to_n_minus
