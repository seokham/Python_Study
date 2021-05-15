
#? 문자열
x = 'banana'
x[0]        #* 0번 글자는?
'b'
x[2:4]      #* 2번부터 4번 앞(3번)까지는?
'na'
x[:3]       #* 처음부터 3번 앞(2번)까지는?
'ban'
x[3:]       #* 3번부터 끝까지는?
'ana'


#* [리스트 명령어]
prime = [3, 7, 11]
prime.append( 5 )       #* prime에 원소 5를 추가
prime.sort()            #* prime을 원소 크기 순으로 정렬
prime.insert(0, 2)      #* 맨 앞(0번)에 2를 삽입(insert)
del prime[4]            #* prime의 4번 원소를 삭제
prime[0] = 1            #* 문자열과는 달리 원소를 바로 바꿔줄 수도 있다.


#* [문자열을 리스트로 바꾸기]
#* 처음에 characters라는 비어있는 리스트를 만들었다 그리고 sentence라는 변수를 만들어서 'Be happy!'라는 문자열을
#* 가리키도록 했다 sentence가 가리키는 'Be happy!'의 글자 하나하나에 대해서 어떤 일을 수행하게 된다
#* 첫번째 글자인 'B'를 characters라는 리스트의 첫번째 원소로 넣고, 두번째 글자인 'e'를 characters의 두번째 원소로
#* 넣는 식이다
characters = []
sentence = 'Be happy!'
for char in sentence:
    characters.append(char)
print(characters)

#* 사실 아래처럼 문자열을 바로 리스트로 변환해도 같은 결과를 얻을 수 있다
list('Be happy!')


#* [숫자를 문자열로 바꾸기]
#* 정수(int) 123을 가리키는 my_int 변수가 있다고 한다면.....
my_int = 123
type(my_int)    #* 결과값 <class 'int'>

#* 문자열 '123'을 얻고 싶다면 다음과 같이 할 수 있다
str(my_int)

#* 위 출력 결과를 보시면 작은따옴표가 붙어 있다 타입을 확인해보면 더 정확히 알 수 있다
type(str(my_int))    #* 결과값 <class 'str'>

#* 이렇게 얻은 문자열을 다음과 같이 변수에 할당하는 것도 가능하다.
#* '숫자를 문자열로 바꾼' 것이라기보다는, '숫자값을 가지고 새로운 문자열을 얻었다'고 표현하는것이 맞다
my_str = str(my_int)


#* [문자열을 숫자로 바꾸기]
#* 숫자를 나타낸 문자열에서 숫자를 얻어낼 수도 있다
int('123')      #* 123
float('123')    #* 123.0


#* [리스트 원소들의 합 구하기]
#* 1부터 10까지의 정수를 원소로 갖는 리스트 one_to_ten 이 있다
one_to_ten = list(range(1, 11))
one_to_ten

#* for 문을 사용해서 계산할 수도 있겠지만, sum()을 이용하면 손쉽게 구할 수 있다
sum(one_to_ten)