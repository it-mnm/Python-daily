# 콜백 함수를 람다로 바꾸기

books = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
},{
    "제목": "혼자 공부하는 머신러닝",
    "가격": 26000
},{
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
}]

print("# 가장 저렴한 책")
print(min(books, key = lambda book: book["가격"]))

print("# 가장 비싼 책")
print(max(books, key = lambda book: book["가격"]))