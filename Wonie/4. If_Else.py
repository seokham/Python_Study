
#? IF & Else

#* 2가 1보다 크면 hello를 출력하라
if 2 > 1:
    print("hello")

#* 1이 2보다 크면 hello를 출력하라
if 1 > 2:
    print("hello")              #* 1>2는 거짓이므로 hello가 출력되지 않는다

#* 1이 2보다 크다는 것이 거짓이라면 hello를 출력하라
if not 1 > 2:
    print("hello")

#* and -> 2가지 조건이 참인 경우 hello를 출력하라
if 1 > 0 and  2 > 1:
    print("hello")

#* 조건에 해당하면 hello 출력, 아니면 hi 출력
x = 3

if x > 2:
    print('hello')
else:
    print('hi')

#* if 부터 체크하고 그 다음 elif를 체크하고 그 다음 else를 체크한다
if x > 5:
    print("hello")
elif x == 3:
    print('bye')
else:
    print('hi')