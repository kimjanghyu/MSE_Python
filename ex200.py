ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
total_profit = 0  #총 수익은 0부터 시작해서 for문을 돌면서 총 수익을 계산할 수 있도록 만든다.

for day_profit in ohlc[1:]: #하루 수익을 for문을 이용하여 만든다. 0번 리스트는 필요하지 않으므로 1번째 부터 시작되도록 한다.
    profit = day_profit[0] - day_profit[3]  #수익 = 하루 수익의 시가 - 하루 수익의 종가로 정의한다.
    total_profit= total_profit + profit # 총 수익 = 총수익+이익으로 정의하여 for문을 돌도록한다.
print(total_profit)


# In[ ]:




