
#? 상속

#* 상속 예시를 보이기 위해 클래스 예제를 가져옴
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("hello! " + to_name + " i'm " + self.name)

    def introduce(self):
        print("i'm " + self.name + " and i " + str(self.age) + " years old")


#* 