def factorial2(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result
N = int(input())
print(factorial2(N))
