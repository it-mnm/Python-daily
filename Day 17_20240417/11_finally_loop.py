# 반복문과 함께 사용하는 경우

print("프로그램 시작")

while True:
    try:
        print("try 구문 실행")
        break
        print("try 구문의 break 키워드 뒤")
    except:
        print("excpet 구문 실행")
    finally:
        print("finally 구문 실행")
    print("while 반복문의 마지막 줄")
print("프로그램 종료")