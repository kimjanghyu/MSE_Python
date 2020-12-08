def message1():     #함수를 정의하여 A가 출력 되도록 했다.   
    print("A")

def message2():     #함수를 정의하여 B가 출력 되도록 한다.
    print("B")

def message3():     
    for i in range (3) :   #range를 이용하여 3번 for문이 돌도록 하였고 
        message2()      #message2를 호출한다.  ->B가 출력된다.
        print("C")      #C가 출력되도록 한다. --->C가 출력된다.
    message1()          #BC가 3번 반복된후 A가 출력된다.

message3()  #------> BCBCBCA가 출력된다.

