fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
과일 = input("좋아하는 과일은?")
if 과일 in fruit.values(): #과일이 fruit이 가리키는 딕셔너리 안에 values안에 있다면 참이므로 정답입니다.가 출력되도록한다.
    print("정답입니다.")
else:
    print("오답입니다.") #아니라면 오답입니다.가 출력되도록한다.

