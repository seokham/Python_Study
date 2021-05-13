
#* [객체 생성자]
#* Cal(10,10) 과 Cal(30,20) 의 첫번째 값이 v1에 두번째 값이 v2에 매개변수 값으로 들어간다.
#* Cal(10,10) 이 실행되면 Cal 이라는 이름의 class가 실행되고 __init__ 메소드가 자동으로 실행되기 때문에
#* 초기화가 되는 것이고, 초기화가 될 때 입력값 (10,10) 을 주면 (v1,v2) 에 들어가서 print(v1, v2)로 출력.

class Cal(object):
    def __init__(self, v1, v2):
        print(v1, v2)

c1 = Cal(10,10)
#* print(c1.add())
#* print(c1.subtract())

c2 = Cal(30,20)
#* print(c2.add())
#* print(c2.subtract())