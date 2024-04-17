# try 구문 내부에서 return 키워드를 사용하는 경우

# test() 함수를 선언합니다.
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

# test() 함수를 호출합니다.
test()


# 함수 시작: test() 함수가 호출되면, "test() 함수의 첫 줄입니다."가 먼저 출력됩니다.

# try 구문: try 블록 내부로 진입하여 "try 구문이 실행되었습니다."를 출력합니다.

# return 키워드: return 키워드를 만나면 함수는 즉시 리턴을 준비합니다. 이 때문에 return 키워드 다음에 있는 "try 구문의 return 키워드 뒤입니다."는 출력되지 않습니다.

# finally 구문: 파이썬에서는 finally 구문이 항상 실행됩니다. 함수가 return을 만나더라도 finally 블록이 있으면 그 내용이 실행되기 전에 finally 블록이 실행됩니다. 그래서 "finally 구문이 실행되었습니다."가 출력됩니다.

# 함수 종료: finally 블록이 실행된 후, 함수가 종료되며 "test() 함수의 마지막 줄입니다."는 실행되지 않습니다.