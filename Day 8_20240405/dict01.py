# 딕셔너리의 요소에 접근하기

# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 출력
print("name: ", dictionary["name"])
print("type: ", dictionary["type"])
print("ingredient: ", dictionary["ingredient"])
print("origin: ", dictionary["origin"])

# 값을 변경합니다.
dictionary["name"] = "8D 건조 망고"
print("name: ", dictionary["name"])

# 딕셔너리 내부의 리스트를 호출
print("두번째 재료 : ", dictionary["ingredient"][1])
