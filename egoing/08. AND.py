
#* AND 진리표
#* True   and   True	True
#* True	  and	False	False
#* False  and	True	False
#* False  and	False	False


#* [if를 중첩해서 사용한 예제]

input_id = input("Please enter your ID.\n")
input_pwd = input("Please enter your PASSWORD.\n")
real_id = "hoppang"
real_pwd = "11"
if real_id == input_id:
    if real_pwd == input_pwd:
        print("Hello!")
    else:
        print("password is wrong.")
else:
    print("ID is wrong.")


#* [and로 통합한 예제]

input_id = input("Please enter your ID.\n")
input_pwd = input("Please enter your PASSWORD.\n")
real_id = "hoppang"
real_pwd = "11"
if real_id == input_id and real_pwd == input_pwd:
    print("Hello!")
else:
    print("Login failed.")