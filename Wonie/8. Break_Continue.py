
#? Break & Continue

#* i가 2 보다 크면 바로 반복을 중지한다
i = 0
while True:
    print(i)
    print('large: "Do you want to be beaten by me?"')
    print('small: "no, fxxk your self"')
    i = i + 1

    if i > 2:
        break


#* i=3 일때 문장 2개와 함께 출력하고 나서 중지된다
for i in range(10):
    print(i)
    print('large: "Do you want to be beaten by me?"')
    print('small: "no, fxxk your self"')

    if i > 2:
        break


#* 0 부터 2까지 세번을 출력하는데 마지막 세번째만 middle 메시지가 출력된다
#* continue는 어떠한 조건에서 continue 밑의 코드를 실행시키고 싶지 않을 때 사용한다
for i in range(10):
    print(i)
    print('large: "Do you want to be beaten by me?"')
    print('small: "no, fxxk your self"')

    continue

print('middle: "Do you wanna fight me?"')


#* 첫번째와 세번째는 middle의 메시지가 출력되지만 두번째는 출력하지 않는 예시
for i in range(3):
    print(i)
    print('large: "Do you want to be beaten by me?"')
    print('small: "no, fxxk your self"')

    if i == 1:
        continue

print('middle: "Do you wanna fight me?"')