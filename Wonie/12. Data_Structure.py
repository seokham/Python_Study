
#? 과일 숫자 세는 프로그램

#* for의 f에 사과가 들어가며 d는 비어있는 상태이고 if f in d 는 f에 사과가 들어있는지 확인하고
#* d는 비어있기 때문에 else로 넘어가고 d[f]=1 은 만약 사과가 없다면 사과를 dict에 넣고 value는
#* 1로 만들게 된다 그럼 d={} 에는 "사과" : 1(사과가 1개) 이 생성된다 사과 1개를 체크하면
#* 다시 for 로 돌아와서 fruit의 두번째 속성을 가져온다 그럼 else로는 안가고 if에 걸려서
#* d(f) = 1(사과갯수) + 1 로 갯수를 더한다 그럼 d = {"사과": 2} 가 된다

fruit = ["apple", "apple", "banana", "banana", "Strawberry", "Kiwi", Peach, Peach, Peach]

d = {}
        #* {"사과": 1}

for f in fruit:
    if f in d:              #* "사과" 라는 key 가 d 라는 딕셔너리에 들어있는지 확인
        d[f] = d[f] + 1     #* 그럼 "사과" 갯수를 1개 더하라
    else:
        d[f] = 1            #* 만약 "사과" 라는 애가 없으면, 그걸 dict에 넣고 value는 1로 만들어라

print(d)