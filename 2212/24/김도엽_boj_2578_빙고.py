import sys

input = sys.stdin.readline

count = 0
user_map = []
line_list = []


# 사회자가 부른 정답에 대해서 bingo_list에 원소들을 지워버리는 함수
def solution(number, line_list):
    global count
    for line in line_list:
        # 만약에 bingo에 number이 존재한다면 지워버린다
        if number in line:
            line.remove(number)
            # 만약 라인이 다 지워진다면 count를 증가시킨다
            if len(line) == 0:
                count += 1


# user의 빙고판
for _ in range(5):
    line = list(map(int, input().split()))
    user_map.append(line)
    line_list.append(line)

# 열을 bingo_list에 추가
for j in range(5):
    column = []
    for i in range(5):
        column.append(user_map[i][j])
    line_list.append(column)
    column = []

diagonal = []
# 대각선을 bingo_list로 추가
for i in range(5):
    diagonal.append(user_map[i][i])
line_list.append(diagonal)

diagonal = []
for i in range(5):
    diagonal.append(user_map[i][4 - i])
line_list.append(diagonal)

# 사회자가 부르는 숫자를 저장하는 리스트
called_list = []
for _ in range(5):
    tmp = list(map(int, input().split()))

    for number in tmp:
        called_list.append(number)

for i, given in enumerate(called_list):
    solution(given, line_list)

    # 세줄 이상 지워져서 빙고를 외치게 되는 경우
    if count >= 3:
        print(i + 1)
        break