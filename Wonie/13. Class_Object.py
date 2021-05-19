
#? Class & Object

#* Class = 빵 모양을 찍어내는 기계
#* Object = 빵 기계로 찍어낸 빵
#* Class = Fuction + Variable
#* Object = Class로 만든 물체
#* Object = Instance


#* 클래스 안의 함수 사용 방법
class Person:
    def say_hello(self):
        print("hello!")

p = Person()                #* p라는 object
p.say_hello()


#* 클래스 안에 변수도 줄 수 있다
class Person:
    name = "doge"                           

    def say_hello(self):
        print("hello! i'm " + self.name)

bitcoin = Person()
ethereum = Person()
ripple = Person()

bitcoin.say_hello()     
ethereum.say_hello()
ripple.say_hello()


#* 위의 코드를 실행하면 bit, ether, ripple 이름을 가진 3명이 전부 i'm doge 라고 출력하게 된다
#* 그래서 name 변수를 doge로 고정하지 않고 object를 만들때 새로 이름을 짖게 해야한다
#* name 이라는 변수를 만들 때 Person 이라는 object 만들 때, 바로 할당하게 한다
class Person:
    def __init__(self, name):   #* init 함수는 self를 첫 인자로 받고 Person에 쓸 새로운 변수를 설정할 수 있다
        self.name = name        #* bitcoin 이라는 person을 만들 때, 첫번째 인자로 name이 들어간다

    def say_hello(self):
        print("hello! i'm " + self.name)

bitcoin = Person("bitcoin")
ethereum = Person("ethereum")
ripple = Person("ripple")

bitcoin.say_hello()
ethereum.say_hello()
ripple.say_hello()


#* 이 코드는 위 코드에서 hello 라고 말하려는 대상까지 추가하는 코드
#* person 이라는 name 만들때 name 이라는 인자를 받아서 name이라는 변수 안에 넣어라
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self, to_name):       # to_name
        print("hello! " + to_name + " i'm " + self.name)

bitcoin = Person("bitcoin")
ethereum = Person("ethereum")
ripple = Person("ripple")

bitcoin.say_hello("eos")
ethereum.say_hello("ada")
ripple.say_hello("vechain")


#* introduce 함수를 추가하여 나이까지 출력 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("hello! " + to_name + " i'm " + self.name)

    def introduce(self):
        print("i'm " + self.name + " and i " + str(self.age) + " years old")

coin = Person("doge", 23)
coin.introduce()