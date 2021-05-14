
#* [인스턴스 변수의 특징]
#* c1.show() 로 호출하면 결과값 10 20 20 이 잘 출력된다.
#* 인스턴스(객체)의 메소드(함수) 안에 (self.value) 변수가 접근 되는 것이 허용된다.
#* 파이썬은 메소드 바깥쪽에서 직접 인스턴스 변수에 접근하는 것이 허용된다.

class C(object):
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.value)

c1 = C(10)
print(c1.value)
c1.value = 20
print(c1.value)
c1.show()