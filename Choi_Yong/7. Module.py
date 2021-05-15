
#? 모듈

#* import를 사용하면 모듈을 불러올 수 있다
import 모듈             #* 모듈 전체를 불러온다
from 모듈 import 이름   #* 모듈 내에서 필요한 것만 불러온다


#* 모듈을 불러오면 모듈 내의 변수를 사용하기 위해서는 모듈.변수의 형식으로 써주어야 한다
import tkinter
tkinter.widget = tkinter.Label(None, text='I love Python!')
tkinter.widget.pack()


#* 
from tkinter import *
widget = Label(None, text='I love Python!')
widget.pack()


#* 아래의 예에서는 문자열이었던 Label이 임포트 문 실행 후 tkinter의 Label로 바뀌어 버린 것을 볼 수 있다
#* 이런 특성을 이해하고 상황에 맞게 사용하시면 된다
Label = 'This is a Label'
from tkinter import *
Label                       #* 결과값 <class 'tkinter.Label'>


#* 한 번 임포트한 모듈을 다시 불러와야 할 때는 아래와 같이 다시 로드(reload) 할 수 있다
from importlib import reload
reload(모듈)