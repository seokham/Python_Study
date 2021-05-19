
#? Function

#* 여러번 출력하고 싶다면 출력하고 싶은 수 만큼 print()로 호출해주면 되겠지만....
print('large: "Do you want to be beaten by me?"')
print('small: "no, fxxk your self"')
print('large: "Do you want to be beaten by me?"')
print('small: "no, fxxk your self"')
print('large: "Do you want to be beaten by me?"')
print('small: "no, fxxk your self"')
print('large: "Do you want to be beaten by me?"')
print('small: "no, fxxk your self"')


#* chat() 함수를 여러번 호출하면 print() 호출을 여러번 사용할 필요 없다
def chat():
    print('large: "Do you want to be beaten by me?"')
    print('small: "no, fxxk your self"')

chat()
chat()
chat()
chat()


#* large, small 이라는 이름을 바꿀 때 직접 수정하여 바꿀 수도 있지만 틀을 만들어서 바꾸는 것이 좋다
def chat(name1, name2, age):
    print('%s: "how old are you?"' % name1)
    print('%s: "i am %d"' % (name2, age))

chat('large', 'small', 10)
chat('men', 'women', 20)


#* 연산이 반복된다
a = 1
b = 2
c = a + b

x = 1
y = 2
z = x + y


#* 연산이 반복되는 부분도 틀을 만들어 놓을 수 있다
def dsum(a, b):
    result = a + b
    return result

d = dsum(1, 2)
print(d)


#! print 와 return 문법 사용시 주의사항!
#* 실행 결과는 None 으로 출력되는데 이것은 인자에 아무런 것도 들어가지 않았다는 뜻이다
def dsum(a, b):
    result = a + b
    print(result)   #* return 이 아닌 print

d = dsum(1, 2)
print(d)