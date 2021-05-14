
#* [함수의 필요성]
#* 1. 긴 코드를 짧은 단어로 축약할 때
#* 2. 어떠한 값을 넣었을 때 원하는 방향으로 결과값을 출력시키고 싶을 때

#* [함수 만들기]
#* def=함수를 정의, a3=함수의 이름
#* 7행 a3()은 5행 a3()의 함수를 호출한다.
def a3():
    print('aaa')
a3()


#* [Return 값]
#* 조건에 따라서 어떠한 값을 남기고 싶을 때 사용한다.
def a3():
    return 'aaa'
print(a3())


#* 결과값은 before 와 aaa가 실행된다.
#* return 으로 인한 결과값이 a3()로 반환되었다.
#* return 을 만나는 즉시 함수를 종료시킨다.
def a3():
    print('before')
    return 'aaa'

    print('after')

print(a3())         


#* [입력값]
#* print(a3())을 실행할 때 def a3()의 괄호에 3을 넣어서 실행한다.
def a(num):
    return 'a'*num      #* 함수를 실행하고 나서 return 값을 남긴다.
print(a(3))


#* [여러개의 입력값]
def make_string(str, num):
    return str*num
print(make_string('b', 3))


#* [Login App]
input_id = input("Please enter your ID.\n")
def login(_id):
    members = ['hoppang', 'h1234', 'son']
    for member in members:
        if member == _id:
            return True
    return False
if login(input_id):
    print('Hello, '+input_id)
else:
    print('Who are you?')