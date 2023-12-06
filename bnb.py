import math

def partition_values_from_index(values, start_index, 
                                total_value, unassigned_value, 
                                test_assignment, test_value,
                                best_assignment, best_err):
    """
    values: set S
    start_index: index of values to be assigned
    total_value: total value of S
    unassigned_value: total value of unassigned values
    test_assignment: current assignment of values in s1
    test_value: current value of s1
    best_assignment: best assignment so far
    best_err: best error so far
    """
    # calculate error on sum of value in current set s1
    test_err = abs(2 * test_value - total_value)
    # if already find solution then return
    if test_err == 0:
        best_err[0] = 0
        best_assignment[0] = test_assignment.copy()
        return True
    # if index already at end
    if start_index >= len(values):
        if test_err < best_err[0]:
            best_err[0] = test_err
            best_assignment[0] = test_assignment.copy()
            # print(best_err)

            if best_err[0] == 0:
                return True
        return False
    else:
        if test_err - unassigned_value < best_err[0]:
            unassigned_value -= values[start_index]

            # set s1
            test_assignment[start_index] = True
            if partition_values_from_index(values, start_index+1,
                                        total_value, unassigned_value, test_assignment,
                                        test_value+values[start_index],
                                        best_assignment, best_err):
                return True
            
            # undo set s1
            unassigned_value += values[start_index]
            test_assignment[start_index] = False

            # set s2
            if partition_values_from_index(values, start_index+1,
                                        total_value, unassigned_value, test_assignment,
                                        test_value,
                                        best_assignment, best_err):
                return True
            
    return False
                                        

def partition_problem_bnb(S):
    n = len(S)
    total_value = sum(S)
    unassigned_value = total_value
    test_assignment = [False] * n
    best_assignment = [False] * n
    test_value = 0
    best_err = [math.inf]  # Menggunakan list sebagai mutable container
    is_solution = partition_values_from_index(S, 0, total_value, unassigned_value,
                            test_assignment, test_value, best_assignment,
                            best_err)
    
    if is_solution:
        s1 = [S[i] for i in range(n) if best_assignment[0][i]]
        s2 = [S[i] for i in range(n) if not best_assignment[0][i]]

        return s1, s2
    else:
        # no solution
        return None
    
# tc = []
# with open("tc/tc_80.txt", 'r') as f:
#     for line in f:
#         tc.append(int(line.strip()))

# print(partition_problem_bnb(tc))

# tc = [5,2,1,4]

# print(partition_problem_bnb(tc))