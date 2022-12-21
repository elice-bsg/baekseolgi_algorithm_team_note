# 문제에 나와있는 대로 함수 선언

def d(n):
    n = n + sum(map(int, str(n)))
    return n


NotingSelfNum = set() # 중복되는 수 제거 하기 위해서 set으로 선언

# 1부터 10000까지의 숫자중에 생성자가 있는 숫자들 set에 넣기
for i in range(1, 10001):
    NotingSelfNum.add(d(i))

# 1부터 10000까지의 숫자중에서 생성자가 있는 숫자가 아닌 숫자들의 집합에 안들어가는 숫자를 출력한다.
for k in range(1, 10001):
    if k not in NotingSelfNum:
        print(k)
