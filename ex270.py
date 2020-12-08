class Stock: #Stock 클래스를 생성한다.
    def __init__(self, name, code,per,pbr,dividend):
        self.name = name #self에 name이라는 이름을 만들고, 바깥에서 넘어온 name을 바인딩 해준다.
        self.code = code #self에 code라는 이름을 만들고, 바깥에서 넘어온 code를 바인딩 해준다.
        self.per = per #self에 per이라는 이름을 만들고, 바깥에서 넘어온 per을 바인딩 해준다.
        self.pbr = pbr #self에 pbr이라는 이름을 만들고, 바깥에서 넘어온 pbr을 바인딩 해준다.
        self.dividend = dividend #self에 dividend이라는 이름을 만들고, 바깥에서 넘어온 dividend를 바인딩 해준다.
    def set_name(self, name): #객체에 종목명을 입력할 수 있는 set_name 메서드를 추가한다.
        self.name = name

    def set_code(self, code): #객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가한다.
        self.code = code

    def get_name(self):  #종목명을 리턴하는 get_name 메서드를 추가한다.
        return self.name

    def get_code(self): #종목코드를 리턴하는 get_code 메서드를 추가한다.
        return self.code

    def set_per(self, per):  #객체에 per을 입력할 수 있는 set_per메서드를 추가한다.
        self.per = per

    def set_pbr(self, pbr): #객체에 pbr을 입력할 수 있는 set_pbr 메서드를 추가한다.
        self.pbr = pbr

    def set_dividend(self, dividend): #객체에 dividend을 입력할 수 있는 set_dividend 메서드를 추가한다.
        self.dividend = dividend
종목 = [] #종목이라는 빈 리스트를 만든다.

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83) #Stock 클래스의 객체를 만들어 삼성이라는 변수로 바인딩 한다.
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27) #Stock 클래스의 객체를 만들어 현대차이라는 변수로 바인딩 한다.
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37) #Stock 클래스의 객체를 만들어 LG전자이라는 변수로 바인딩 한다.

종목.append(삼성) #리스트에 삼성이라는 변수가 가리키는 객체를 넣어준다.
종목.append(현대차) #리스트에 현대차라는 변수가 가리키는 객체를 넣어준다.
종목.append(LG전자) #리스트에 LG전자라는 변수가 가리키는 객체를 넣어준다.

for i in 종목: #종목이라는 리스트 안에 있는 객체가 i에 대입된다. 
    print(i.code, i.per) #.code와 .per을 이용하여 변수를 접근할 수 있다. i라는 변수가 Stock클래스의 객체를 바인딩하기 떄문이다.

