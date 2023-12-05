def partition_problem_dp(S):
    n = len(S)
    half_sum = sum(S)//2
    
    # no solution
    if half_sum*2 != sum(S):
        return None
    
    # Tabulation initialization
    dp = [[False for x in range(half_sum+1)] for y in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True


    i = 1
    for num in S:
        for j in range(1, half_sum+1):
            dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
        i += 1

    # no solution
    if not dp[n][half_sum]:
        return None
    
    sisa = half_sum
    s1 = []
    i = n
    while sisa != 0:
        if not dp[i][sisa]:
            s1.append(S[i])
            sisa -= S[i]
        i -= 1

    s2 = []
    s1_copy = s1.copy()
    for num in S:
        if num not in s1_copy:
            s2.append(num)
        else:
            s1_copy.remove(num)

    return s1, s2