# try except 구문 끝난 후 파일닫기
# finally가 파일 처리할 때 사용한다는 것은 말도안됨.
# 단지 finally 키워드를 사용하면 코드가 깔끔해질 것 같을 때 사용한다.

# try except 구문을 사용합니다.
try:
    # 파일을 엽니다.
    file = open("info.txt", "w")
    # 여러가지 처리 수행
    예외.발생해라() #일부러 예외를 발생시킵니다.
    
except:
    print("오류가 발생했습니다.")

# 파일을 닫습니다.   
file.close() 
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed : ", file.closed)