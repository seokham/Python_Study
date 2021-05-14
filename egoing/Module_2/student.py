
#* 모듈을 통한 중복의 제거 & 재활용성의 증대
#* student.py 로 함수를 분리시키면 module1, 2 코드의 양이 줄어들었고
#* student.py 의 return 값을 바꾼다고 하면 모듈을 사용하는 코드들의
#* 결과 값이 한꺼번에 바꿀 수도 있어 유지보수에 용의하다.
def a():
    return 'a'
def b():
    return 'b'
def c():
    return 'c'