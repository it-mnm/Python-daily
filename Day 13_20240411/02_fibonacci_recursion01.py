# 재귀 함수로 구현한 피보나치 수열(1)

# 함수를 선언합니다.
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    
# 함수를 호출합니다.
print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))
print("fibonacci(4):", fibonacci(4))
print("fibonacci(5):", fibonacci(5):)

# n이 커지면너무: 오래걸림
print("fibonacci(35):", fibonacci(35))