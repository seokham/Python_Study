
#* [while]
while False:
    print('Hello world')
print('After while')


#* [while 조건]
#* (while 문을 3번만 반복하게 한다.)
i = 0
while i < 3:
    print('Hello world')
    i = i + 1


#* [while 활용]
#* (hellow world 뒤에 i의 변수까지 출력되게 한다.)
i = 0
while i < 10:
    print('print("Hello world '+str(i*9)+'")')
    i = i + 1

i = 0
while i < 10:
    print('Hello world '+str(i*9)+'')
    i = i + 1


#* [조건문과 반복문의 합체 - 1]
#* i가 4일 때만 출력한다.
i = 0
while i < 10:
    if i == 4:
        print(i)
    i = i + 1


#* i가 4가 아닐 때의 모든 값을 출력한다.
i = 0
while i < 10:
    if i != 4:
        print(i)
    i = i + 1


#* [조건문과 반복문의 합체 - 2]
#* i가 4일 때, break를 만나고 반복문이 끝나며, after while을 출력한다.
i = 0
while i < 10:
    if i == 4:
        break
    print(i)
    i = i + 1
print('after while')