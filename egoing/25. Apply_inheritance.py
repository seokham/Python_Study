
#* [상속 응용]
#* CalMultiply 클래스는 multiply 메소드만 가지고 있지만 Cal의 자식 클래스 이기 때문에
#* add(), multiply() 라는 메소드를 사용할 수 있다. 
#* 즉, CalMultiply 라는 클래스는 Cal 이 가지고 있는 모든 메소드를 상속받은 것이라고 할 수 있다.
#* CalMultiply 나 CalDivide 라는 클래스 안의 self.v1, self.2 들은 class Cal(object) 안에만 정의
#* 되어 있다. 상속은 메소드만을 상속하는 것이 아닌 그 부모 객체가 가지고 있는 변수도 상속 받는다.
class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
class CalMultiply(Cal):
    def multiply(self):
        return self.v1*self.v2
class CalDivide(CalMultiply):
    def divide(self):
        return self.v1/self.v2
c1 = CalMultiply(10,10)
print(c1.add())
print(c1.multiply())
c2 = CalDivide(20,10)
print(c2, c2.add())
print(c2, c2.multiply())
print(c2, c2.divide())
