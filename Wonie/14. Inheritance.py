
#? Inheritance

#* 상속 예시를 보이기 위해 클래스 예제를 가져옴
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("hello! " + to_name + " i'm " + self.name)

    def introduce(self):
        print("i'm " + self.name + " and i " + str(self.age) + " years old")


#* police 클래스가 Person을 상속받아서 위의 코드를 똑같이 한번 더 입력해둘 필요 없이
#* 그대로 가져와서 쓸 수 있게 된다
class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체보됐다, " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야겠다: " + to_program)

bitcoin = Person("bitcoin", 20)
ethereum = Police("ethereum", 21)
ripple = Programmer("ripple", 22)


ethereum.arrest("bitcoin")      #* police인 ethereum에게 bitcoin을 체포 시킨다
ripple.program("hacking")       #* programer인 ripple에게 hacking을 시킨다

bitcoin.arrest("ripple")        #* bitcoin은 person이므로 체포할 수 없어 애러 발생
ethereum.program("hacking")     #* ethereum은 police이므로 해킹을 할 수 없어서 에러 발생
