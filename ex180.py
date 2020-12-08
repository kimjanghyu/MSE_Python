low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility  = []   #volatility라는 빈 리스트를 만들고
for i in range(5):  #range를 이용하여 for문이 5번 반복되도록 한다.
    변동폭 = high_prices[i]-low_prices[i]  #변동 폭은 고가와 저가의 차이다.
    volatility.append(변동폭) #append를 이용하여 volatility 리스트에 변동폭들을 추가한다. 

