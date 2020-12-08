>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>> icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'

#딕셔너리에 누가바라는 키가 없기 때문에 에러가 발생한 것이다.
#딕셔너리에 인덱싱을 할 때는 오직 존재하는 키로만 인덱싱 할 수 있다.
