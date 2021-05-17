
#? Dict

x = dict()
y = {}

print(x)
print(y)


#* dict은 Key와 Value로 이루어져 있는 자료구조이다
x = {
    0: "Wonie",
    1: "Hello",
    "age": 20,
}

print(x[0])
print(x[1])
print(x["age"])

print("name" in x)      #* x안에는 name이랑 key값이 없기 때문에 false

print(x.keys())         #* x 안에 있는 모든 key값을 출력

print(x.values())       #* x 안에 있는 모든 value값을 출력


#* dict 에서 for문 사용
x = {
    0: "Wonie",
    1: "Hello",
    "age": 20,
}

for key in x:

    print(key)
    print(x[key])


#* for문에서 다르게 출력
x = {
    0: "Wonie",
    1: "Hello",
    "age": 20,
}

for key in x:
    
    print("key: " + str(key))
    print("value: " + str(x[key]))


#* key값과 value값을 추가 (key:value)
x = {
    0: "Wonie",
    1: "Hello",
    "age": 20,
}

x["school"] = "student"

print(x)