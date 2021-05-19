
#? Tuple

#* 리스트와 비슷하여 결과값이 같다
x = tuple()
y = ()

print(x)
print(y)


#* 리스트와 문법이 비슷하다
x = (1,2,3)
y = ('a','b','c')
z = (1, 'hello','there')

print(x)
print(y)
print(z)

print(x + y)
print('a' in y)
print(z.index[1])


#* 리스트는 mutable(가변) 이지만 튜플은 immutable(불변) 이다
x = (1,2,3)

x[0] = 10