
#* [Set, Get 메소드를 사용하는 이유]
#* 입력 받고 싶은 값이 문자가 아닌 정수만 받고 싶다면 set, get 방식을 사용할 수 있다.
#* 코드를 실행시키면 29행 c1.setV1('one') 에서 one 이라는 문자가 def setV1(self, v) 의 v로 들어온다. 
#* 그럼 매개변수 v는 isinstance(v, int) 의 v로 들어가게 되는데 문자열 one은 int class의 int가 아니기 때문에
#* false가 되면서 self.v1=v 코드는 실행되지 않는다.
#* 즉, 인스턴스 변수가 원하지 않는 값으로 바뀌는 것을 방지할 수 있다는 것이다.
class Cal(object):
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())
c1.setV1('one')
c1.v2 = 30
print(c1.add())


#* 정수가 잘 들어오는지 판별하는 if isinstance(v1, int) 이 코드는 def __init__ 바로 아래에도 들어갈 수 있다.
#* 생성자에 들어오는 값도 어디선가 누군가 정수가 아닌 값을 줄 수 있기 때문이다.
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
c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())
c1.setV1('one')
c1.v2 = 30
print(c1.add())
print(c1.subtract())