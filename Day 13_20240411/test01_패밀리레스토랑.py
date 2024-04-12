min = 2
max = 10
total = 100
memo = {}

def problem(left, sit):
    key = str([left, sit])

    if key in memo:
        return memo[key]
    if left < 0:
        return 0
    if left == 0:
        return 1
    
    count = 0
    for i in range(sit, max + 1):
        count += problem(left - i, i)

    memo[key] = count

    return count

print(problem(total, min))