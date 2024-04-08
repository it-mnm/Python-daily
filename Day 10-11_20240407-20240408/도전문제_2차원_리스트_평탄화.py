li = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
new = []
for i in li:
    if type(i) == list:
        for j in i:
            new.append(j)
    else:
        new.append(i)

print("{}를 평탄화하면".format(li))
print("{}입니다.".format(new))