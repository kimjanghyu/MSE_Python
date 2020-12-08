리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트: #리스트 내의 원소들을 i에 대입하여 원소의 개수 만큼 for문이 돌도록한다.
    if i.endswith(('.h','.c')): #if문과 endswith를 사용하여 .h 또는 .c로 끝나는 원소들을 출력하도록 한다. 
        print(i)
