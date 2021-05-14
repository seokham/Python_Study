
#* 반복문을 3번 반복할 것이라고 고정해놨을 때
members = ['hoppang', 'h1234','son']
i = 0
while i < 3:
    print(members[i])
    i = i + 1


#* [컨테이너와 반복문의 만남]
#* 리스트의 값이 몇개냐에 따라서 달라지도록 가변성을 준다.
members = ['hoppang', 'h1234', 'son']
i = 0
while i < len(members):
    print(members[i])
    i = i + 1


#* [달콤한 for문의 등장]
#* for (변수) in (컨테이너)
#* 반복을 위해서 필요한 코드가 한줄로 끝난다.
#* 대상이 컨테이너 안에 있을 때 사용할 수 있다.
members = ['hoppang', 'h1234', 'son']
for member in members:
    print(member)


#* [for문의 활용]
i=[0,1,2,3,4]
for item in i:
    print('hello')


#* ↑ 위의 코드를 아래처럼 줄일 수 있다.
for item in [0,1,2,3,4]:
    print('hello')


#* range(5) = [0,1,2,3,4]
for item in range(5):
    print(item)


#* range(5, 11) = [5,6,7,8,9,10,11]
for item in range(5, 11):
    print(item)


#* [로그인 애플리케이션에 투입]
#* input_id의 입력값이 members의 요소들 중에 일치하는 값이 있다면 "Hello!, (요소값)" 을 출력한다.
#* input_id의 입력값이 members의 요소들 중에 일치하는 값이 없다면 "Who are you?" 를 출력한다.
#* import sys, sys.exit() 이 두줄이 없다면 "Hello!, (요소값)" 와 "Who are you?" 가 모두 출력된다.
input_id = input("Please enter your ID.\n")
members = ['hoppang', 'h1234', 'son']
for member in members:
    if member == input_id:
        print('Hello!, '+member)
        import sys
        sys.exit()
print('Who are you?')