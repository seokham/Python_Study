
#? 세트

#* 세트는 집합을 표현한다 세트는 중괄호({, })를 사용한다

fruits = {'apple', 'banana', 'orange'}          #* 과일을 나타내는 fruits 세트를 만든다
fruits.add('mango')                             #* 망고를 추가한다
companies = {'apple', 'microsoft', 'google'}    #* 회사를 나타내는 집합을 만든다 


#* 타입을 확인한다
type(fruits)        #* <class 'set'>
type(companies)     #* <class 'set'>


#* 세트를 이용해 집합 연산을 사용할 수 있다
fruits & companies           #* 교집합
                             #* 결과값 {'apple'}
fruits | companies           #* 합집합
                             #* 결과값 {'apple', 'mango', 'microsoft', 'orange', 'google', 'banana'}


#* apple은 fruits에도 속하고 companies에도 속하는데, 위 합집합의 결과에 한 번만 나오는 것을 볼 수 있습니다
#* 이와 같이 세트는 중복 원소를 갖지 않습니다. 또, 원소의 순서가 유지되지 않는 특징도 있다.
alphabet = list('google')
alphabet                    #* 결과값 ['g', 'o', 'o', 'g', 'l', 'e']
set(alphabet)               #* 결과값 {'e', 'o', 'g', 'l'}