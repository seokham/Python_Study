
#* [인스턴스 변수와 메소드]
#* self.v1, self.v2 를 이용해서 def __init__ 안의 v1과 v2를 def add 에서도 사용이 가능하게 한다.
#* 즉, 인스턴스에 있는 모든 메소드에 접근할 수 있는 v1과 v2의 값을 사용할 수 있다.
#* 첫번째 매개변수 self 를 이용해서 인스턴스에 소속되는 변수를 지정할 수 있다.

class Cal(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2


c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())
c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())