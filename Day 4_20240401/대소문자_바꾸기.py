# upper()와 lower()를 사용해도 원본은 바뀌지 않는다. => 비파괴적 함수
a = "Hello Python Programming...!"
print(a.upper())    # 전부 대문자
print(a.lower())    # 전부 소문자
print(a)            # 원본