max_value = 0
a = 0
b = 0

for i in range(1,100//2 +1):
    j = 100 -i
    new_value = i*j
    if max_value < new_value:
        max_value = new_value
        a = i
        b = j


print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))
