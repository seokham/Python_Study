
#? List

#* 엘레멘트 여러개를 그루핑할 때 쓴다

#* 결과값은 똑같이 출력
x = list()
y = []

print(x)
print(y)


#* 리스트
x = [1,2,3,4]
y = ['hello', 'world']
z = ['hello', 1,2,3]

print(x)
print(y)
print(z)
print(x + y)
print(x[0])     #* x의 0번째 자리의 있는 값을 출력


#* x의 0번째 자리의 있는 값을 10으로 수정
x[3] = 10       
print(x[3])


#* len
x = [1,2,3,4]

num_elements = len(x)
print(num_elements)


#* sorted(정렬)
x = [4,3,2,1]

y = sorted(x)
print(y)

z = sum(x)      #* 리스트의 원소를 전부 합친다
print(z)


#* n에 x의 원소 4 3 2 1 을 차례대로 들어가게 하고 출력한다
x = [4,3,2,1]

for n in x:
    print(n)


#* index는 원소가 몇번째 자리에 있는지 출력해준다
x = [4,3,2,1]
y = ['hello', 'there']

print(x.index(3))
print(y.index('hello'))


#* 리스트 안에 원소가 있는지 확인만 한다
x = [4,3,2,1]
y = ['hello', 'there']

print('hello' in y)