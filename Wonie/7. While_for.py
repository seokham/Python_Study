
#? Wile & for

#* 여러번 출력하고 싶다면 출력하고 싶은 수 만큼 print()로 호출해주면 되겠지만....
print('large: "Do you want to be beaten by me?"')
print('small: "no, fxxk your self"')
print('large: "Do you want to be beaten by me?"')
print('small: "no, fxxk your self"')
print('large: "Do you want to be beaten by me?"')
print('small: "no, fxxk your self"')
print('large: "Do you want to be beaten by me?"')
print('small: "no, fxxk your self"')


#* for 를 사용하면 print() 호출을 여러번 사용할 필요 없다
for i in range(10):                     #* i = 몇 번째인지 i라는 변수에 넣으라는 뜻 (10) = 10번 반복
    print('large: "Do you want to be beaten by me?"')
    print('small: "no, fxxk your self"')


#* 
for i in range(3):
    print(i)
    print('large: "Do you want to be beaten by me?"')
    print('small: "no, fxxk your self"')


#* 위 코드와 같은 결과값이 출력되는데, for 와 다르게 while은 조건을 넣어서 표현한다
i = 0
while i < 3:
    print(i)        #* 0 부터 시작
    print('large: "Do you want to be beaten by me?"')
    print('small: "no, fxxk your self"')
    i = i + 1   #* i = 0 + 1 = 1
                #* i = 1 + 1 = 2
                #* i = 2 + 1 = 3


#* for 보다 while 구문이 편한 경우 중 하나의 예시는 '무한루프'이다
i = 0
while True:         #* True 라고 하면 무한루프
    print(i)
    i = i + 1