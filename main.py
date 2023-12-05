import random
import timeit
import tracemalloc
import matplotlib.pyplot as plt
import numpy as np


from dp import partition_problem_dp
from bnb import partition_problem_bnb

TC_SIZE = [10, 40, 80]
TOTAL_SUM = [100, 1000, 100000]
OPTION = ["small", "medium", "large"]

run_time_40 = []

def generate_tc(size, option):
    tc = []
    sets = set()
    for i in range(size):
        num = random.randint(1, TOTAL_SUM[option])
        while num in sets:
            num = random.randint(1, TOTAL_SUM[option])
        
        sets.add(num)
        tc.append(num)

    if partition_problem_dp(tc) == None:
        return generate_tc(size, option)
    else:
        write_tc_to_file(f"tc/tc_{size}_{OPTION[option]}.txt", tc)
        return tc

def write_tc_to_file(filename, data):
    with open(filename, 'w') as f:
        for num in data:
            f.write(str(num) + '\n')

def generate_tc_with_option(size):
    for i in range(3):
        generate_tc(size, i)

def main():
    # generate_tc_with_option(10)
    # generate_tc_with_option(40)
    for size in TC_SIZE:
        print("Testing size: ", size)
        if size == 80:
            loop = 1
        else:
            loop = 3

        for i in range(loop):
            print("Option: ", OPTION[i])
            # open file tc
            if size == 80:
                filename = f"tc/tc_{size}.txt"
            else:
                filename = f"tc/tc_{size}_{OPTION[i]}.txt"
            with open(filename, 'r') as f:
                tc = []
                for line in f:
                    tc.append(int(line.strip()))

            print("TC: ", tc)
            print()
            # Dynamic Programming
            tracemalloc.start()
            start = timeit.default_timer()
            print("- DP: ", partition_problem_dp(tc))
            stop = timeit.default_timer()
            current, peak = tracemalloc.get_traced_memory()
            print('\tMemory usage DP: Peak %s bytes' % (peak))
            runtime = float("%.5f" % (stop - start)*1)
            print('\tDP Time: ', runtime, "seconds")
            tracemalloc.stop()
            print()
            # Branch and Bound
            tracemalloc.start()
            start = timeit.default_timer()
            print("- BNB: ", partition_problem_bnb(tc))
            stop = timeit.default_timer()
            current, peak = tracemalloc.get_traced_memory()
            print('\tMemory usage BNB: Peak %s bytes' % (peak))
            runtime = float("%.5f" % (stop - start)*1)
            print('\tBNB Time: ', runtime, "seconds")
            tracemalloc.stop()
            print('----------------------------------')


if __name__ == "__main__":
    main()