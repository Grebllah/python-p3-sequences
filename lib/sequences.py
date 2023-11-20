#!/usr/bin/env python3

def print_fibonacci(length):
    fib_nums = []
    if length == 0:
        print(fib_nums)
    elif length == 1:
        print([0,])
    elif length == 2:
        print([0, 1])
    else:
        fib_nums.append(0)
        fib_nums.append(1)
        for i in range(2, length):
            i_one = fib_nums[i - 2]
            i_two = fib_nums[i - 1]
            new_num = i_one + i_two
            fib_nums.append(new_num)
        print(fib_nums)