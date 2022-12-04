#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        new_t_a = tuple_a[0], 0
    else:
        new_t_a = tuple_a
    if len(tuple_b) == 1:
        new_t_b = tuple_b[0], 0
    else:
        new_t_b = tuple_b
    t0 = new_t_a[0] + new_t_b[0]
    t1 = new_t_a[1] + new_t_b[1]
    result = t0, t1
    return tuple(result)
