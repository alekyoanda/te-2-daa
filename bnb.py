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
            return True, test_assignment
        # if index already at end
        if start_index >= len(values):
            if test_err < best_err:
                best_err = test_err
                best_assignment = test_assignment.copy()

                print(best_err)

                if best_err == 0:
                    return True, best_assignment
                
            return False, best_assignment
        else:

            unassigned_value -= values[start_index]

            # set s1
            test_assignment[start_index] = True
            is_optimal, best_assignment = partition_values_from_index(values, start_index+1,
                                        total_value, unassigned_value, test_assignment,
                                        test_value+values[start_index],
                                        best_assignment, best_err)
            
            if is_optimal:
                return True, best_assignment
            
            # set s2
            test_assignment[start_index] = False
            is_optimal, best_assignment = partition_values_from_index(values, start_index+1,
                                        total_value, unassigned_value, test_assignment,
                                        test_value,
                                        best_assignment, best_err)
            
            if is_optimal:
                return True, best_assignment
            
            return False, best_assignment
                                        

def partition_problem_bnb(S):
    n = len(S)
    total_value = sum(S)
    unassigned_value = total_value
    test_assignment = [False]*n
    best_assignment = [False]*n
    test_value = 0
    best_err = math.inf
    is_solution, solution = partition_values_from_index(S, 0, total_value, unassigned_value,
                                test_assignment, test_value, best_assignment,
                                best_err)
    
    if is_solution:
        s1 = []
        s2 = []
        for i in range(n):
            if solution[i]:
                s1.append(S[i])
            else:
                s2.append(S[i])

        return s1, s2
    else:
        # no solution
        return None
    
# tc = []
# with open("tc/tc_80.txt", 'r') as f:
#     for line in f:
#         tc.append(int(line.strip()))

# print(partition_problem_bnb(tc))