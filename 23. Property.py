
#* 외부에서 인스턴스 변수에 접근할 수 있는 것을 속성이라고 한다.

#* 파이썬은 기본적으로 외부에서 인스턴스 변수에 접근이 가능하다.
class C(object):
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.__value)
c1 = C(10)
print(c1.value)


#* 어떤 인스턴스는 내부적으로 객체 안에서 내부적으로만 활용되는 변수여서 그 변수값을
#* 외부에서 알 필요가 없으며 외부에서 수정해서는 안되는 변수가 있다면 그 변수를 숨기는
#* 방법이 있다. self.__value = v 처럼 __ 를 앞에 붙여주면 인스턴스 밖에서는 접근 할
#* 수 없다.

#* 밖에서 접근하게 만든 아래 코드는 실행되지 않는다.
class C(object):
    def __init__(self, v):
        self.__value = v
    def show(self):
        print(self.__value)
c1 = C(10)
print(c1.__value)


#* 내부 메소드에서는 접근이 가능함을 확인할 수 있다.
class C(object):
    def __init__(self, v):
        self.__value = v
    def show(self):
        print(self.__value)
c1 = C(10)
c1.show()