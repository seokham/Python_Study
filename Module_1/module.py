
#* teacher 라는 module로 부터 a라는 함수만을 import 한다.
#* a라는 함수의 이름을 z로 바꾸고 싶을 때 as를 쓴다.
from teacher import a as z
import student as k
print(z())
print(k.a())