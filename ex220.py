def print_max(a,b,c):   #3개의 숫자를 a,b,c로 하여 print_max함수를 정의한다.
    if a>b and a>c:     #if함수를 통해서 a가 가장 큰 경우 a가 출력되도록 만든다.
        print(a)
    elif b>c and b>a:   #b가 가장 큰 경우 b가 출력되도록 만든다.
        print(b)
    else:
        print(c)         #c가 가장 큰 경우 c가 출력되도록 만든다.

