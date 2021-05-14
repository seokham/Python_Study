
#* [내장모듈]
import math
print(math.ceil(2.9))
print(math.floor(2.9))
print(math.sqrt(16))


#* [모듈에 없을 때]
#* hoppang_a의 함수의 결과값이 나오길 기대 하지만 아래 코드를 실행하면 B가 출력된다.
#* 프로젝트의 복잡도가 높아지면서 문제가 발생한다.

def hoppang_a():
    return 'a'
#* (중간에 있는 수많은 코드)

def h1234_a():
    return 'B'
#* (중간에 있는 수많은 코드)
print(hoppang_a())


#* Next -> [Module_1 ~ 3 folder]
