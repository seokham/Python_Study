
#? 여러가지 모듈

#* sys
#* 파이썬 인터프리터를 제어할 수 있는 방법을 제공
#* sys 모듈을 사용하면 이 프롬프트를 바꿀 수가 있다
import sys
sys.ps1                 #* 현재의 프롬프트는?
                        #* 결과값 '>>> '
sys.ps1 = '^^; '        #* 요걸로 바꿔!
^^; 5 * 3               #* 결과값 15
^^; sys.exit()          #* 인터프리터 종료


#* os
#* 운영체제(OS : Operating System)를 제어할 수가 있다
#* os 모듈의 getcwd()는 현재 작업 디렉터리를 알려줍니다.
#* 구해라(get)! 무엇을? 현재 작업 디렉터리(current working directory) 를.....
import os
os.getcwd()


#* re
#* re 모듈은 정규 표현식(regular expression)을 이용해 문자열을 다룰 수 있다
#* 다음 예제에서 두번째 줄의 괄호 안에 쓴 것이 정규 표현식인데, 마침표(.)는 문자 아무거나 한 개를 뜻하고,
#* 별표(*)는 0개 이상의 문자를 뜻합니다. 그래서 현재 디렉토리에서 p 다음에 n이 나오는 이름을 갖고 있는
#* 파일들을 모두 찾아주게 된다
import re, glob
p = re.compile('.*p.*n.*')
for i in glob.glob('*'):
    m = p.match(i)
    if m:
            print m.group()


#* webbrowser
import webbrowser
url='http://www.python.org/'
webbrowser.open(url)