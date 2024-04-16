# 파일 처리 중간에 예외 발생

# try except 구문을 사용합니다.
try:
    # 파일을 엽니다.
    file = open("info.txt", "w")
    # 여러가지 처리 수행
    예외.발생해라() #일부러 예외를 발생시킵니다.
    # 파일을 닫습니다.
    file.close()
except:
    print("오류가 발생했습니다.")

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed : ", file.closed)