
#* [상속]
#* 기존에 자신이나 타인이 이미 만든 객체(원본)를 그대로 상속하면서 기능을 추가하여 만든 것


#* 클래스1
class Class1(object):
    def method1(self):
        return 'm1'
c1 = Class1()
print(c1.method1())


#* 클래스1을 상속없이 해결(기능을 추가) 하는 예시
class Class1(object):
    def method1(self):
        return 'm1'
c1 = Class1()
print(c1.method1())

class Class2(object):
    def method1(self):
        return 'm1'
    def method2(self):
        return 'm2'
c2 = Class2()
print(c2.method1())
print(c2.method2())


#* 클래스1을 그대로 상속하면서 새로운 기능을 추가하는 예시
class Class3(Class1):       #* Class3는 Class1을 상속한다.
    def method2(self):      #* Class3s는 Class1을 가지면서 method2를 추가한것이다.
        return 'm2'
c3 = Class3()               
print(c3.method1())
print(c3.method2())


#? [실행된 결과값이 어떤 코드의 실행 결과값인지 확인하는 방법]
#* 위 코드들을 실행해보면 m1 m1 m1 m2 m1 m2 이렇게 결과값이 출력된다. 이렇게 출력이 되버리면
#* 어디서 어떻게 출력되었는지 한눈에 파악하기 어려울 때가 있다.
#* print() 함수는 여러개의 인자를 받을 수 있다. 첫번째 인자로 print(c1, c1.method1()) 를 입력하고 실행하면
#* <__main__.Class1 object at 0x000001C26FB5F0D0> m1 이렇게 결과값이 나오는데 
#* <__main__.Class1 object at 0x000001C26FB5F0D0> 는 c1의 결과값 이고, m1 은 c1.method1() 의 결과값이 된다.
#* 이렇게 하면 화면에 출력된 내용을 쉽게 확인할 수 있다.

class Class1(object):
    def method1(self):
        return 'm1'
c1 = Class1()
print(c1, c1.method1()) #* c1 이라는 인자를 추가