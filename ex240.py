def 함수0(num) :  #함수0이 num을 받으면 num*2 값을 리턴한다.
    return num * 2

def 함수1(num) : #함수1이 num을 받으면 함수0(num + 2)을 리턴한다.
    return 함수0(num + 2)

def 함수2(num) : #함수2가 num을 받으면 num = num + 10인 새로운 num을 가지고 함수1(num)을 리턴한다.
    num = num + 10 
    return 함수1(num) 

c = 함수2(2)    
print(c)
#함수2가 호출되어 num은 2를 가리킨다.
#num+10이므로 12이고 num이 12가 된다.
#다음으로 함수1이 호출되어 함수 1의 num은 12를 가리킨다.
#함수0을 호출하면서 num+2이므로 함수0의 num은 14를 가리킨다. 
#함수0의 num은 14이므로 14*2는 28이된다.
#28은 계속 리턴되어 가장 바깥에 있는 c=28이 된다.
#따라서 28이 출력될 것이다.
