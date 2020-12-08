import requests 
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#btc딕셔너리 안에 시가, 종가, 최고가.최저가 등이 저장 되어 있으므로 float을 이용한다.
변동폭 = float(btc['max_price']) - float(btc['min_price'])#최고가와 최저가의 차이를 변동폭으로 정의하였으므로 변동폭 = float(btc['max_price']) - float(btc['min_price'])이라 한다.
시가 = float(btc['opening_price'])#시가는 opening_price이므로 시가 = float(btc['opening_price']), 최고가는 최고가 = float(btc['max_price'])라 한다.
최고가 = float(btc['max_price'])
#if문을 사용하여 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하게 만든다
if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")

