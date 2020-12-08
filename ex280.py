import random
#계좌 번호가 랜덤으로 생성되도록 import random을 이용한다.
class Account: #Account 클래스를 만든다.
    account_count = 0 #account_count라는 변수의 초기값을 0으로 바인딩한다.
    
    def __init__(self, name, balance): #생성자에서 입력받는 값은 예금주의 이름과 잔고이다.
        self.deposit_count = 0 #객체가 생성될 때, 입금한 횟수를 카운트 해줄 수 있는 변수를 만든다.
        self.deposit_log = [] #객체가 생성될때 비어있는 리스트가 생성되도록 한다.
        self.withdraw_log = [] #객체가 생성될때 비어있는 리스트가 생성되도록 한다.
        
        self.name = name #self가 가리키는 공간에 name이라는 이름을 만들고 name을 저장한다.
        self.balance = balance #self가 가리키는 공간에 balance라는 이름을 만들고 balance를 저장한다.
        self.bank = "SC은행" #self가 가리키는 공간에 bank라는 이름을 만들고 은행 이름은 SC은행으로 저장한다.

        num1 = random.randint(0,999)  #랜덤하게 3자리 수를 만든다.
        num2 = random.randint(0,99) #랜덤하게 2자리 수를 만든다.
        num3 = random.randint(0,999999) #랜덤하게 6자리 수를 만든다.
        
        num1 = str(num1).zfill(3)  #문자열로 정수값을 변경한다. zfill을 이용해 3자리로 만든다.
        num2 = str(num2).zfill(2)  #문자열로 정수값을 변경한다. zfill을 이용해 2자리로 만든다.
        num3 = str(num3).zfill(6)  #문자열로 정수값을 변경한다. zfill을 이용해 6자리로 만든다.
        self.account_number = num1 + '-' + num2 + '-' + num3 #3-2-6자리를 랜덤하게 만들도록 만든다.  
        Account.account_count += 1 #계좌가 만들어질 때 마다 account-count 값이 증가하도록 한다.

    @classmethod #객체에 접근할 필요가 없는 것들은 @classmethod,cls를 사용한다.
    def get_account_num(cls): #Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가한다.
        print(cls.account_count) #cls를 사용하면 객체가 넘어오는 것이 아니라 클래스의 이름이 넘어온다.

    def deposit(self, amount):#Account 클래스에 입금을 위한 deposit 메서드를 추가한다. 잔고에 접근하기 위해서 첫번쨰 인자를 self로 받는다. 입금액을 amount라는 변수로 바인딩한다.
        if amount >= 1: #입금은 최소 1원 이상만 가능하도록 한다.
            self.deposit_log.append(amount) #입금내역을 입금이 일어날 때마다 리스트로 저장되도록 한다.
            self.balance += amount #입금은 잔고에 amount를 더해주면 된다.

            self.deposit_count += 1 #self가 가리키는 공간에 deposit_count가 있는데 그 값을 1 증가시킨다.
            if self.deposit_count % 5 == 0:         
                self.balance = (self.balance * 1.01) #입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 한다.


    def withdraw(self, amount): #Account 클래스에 출금을 위한 withdraw 메서드를 추가한다. 얼마를 출금할 것인지 amount로 받아준다.
        if self.balance > amount: #출금은 계좌의 잔고 이상으로 출금할 수는 없도록한다..
            self.withdraw_log.append(amount) #출금이 일어날 때마다 출금액이 리스트로 저장되도록한다.
            self.balance -= amount #출금은 잔고에서 amount를 빼주면 된다.

    def display_info(self): #Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가한다.
        print("은행이름: ", self.bank) #은행이름을 출력한다.
        print("예금주: ", self.name) #예금주를 출력한다.
        print("계좌번호: ", self.account_number) #계좌번호를 출력한다.
        print("잔고: ", self.balance) #잔고를 출력한다.

    def withdraw_history(self):
        for amount in self.withdraw_log: 
            print(amount) #출금한 금액을 출력한다.

    def deposit_history(self):
        for amount in self.deposit_log: 
            print(amount) #입금액을 출력한다.


k = Account("Kim", 1000)  #이름은 kim이고 처음에 1000원을 입금했다고 하자.
k.deposit(100) 
k.deposit(200)
k.deposit(300) #100,200,300원을 입금한다.
k.deposit_history()  #k가 가리키는 메서드를 호출한다. 예금한 금액이 출력된다.

k.withdraw(100) 
k.withdraw(200) #100,200원을 출금한다.
k.withdraw_history() #k가 가리키는 매서드를 호출한다. 출금한 금액이 출력된다. 


# In[ ]:





# In[ ]:




