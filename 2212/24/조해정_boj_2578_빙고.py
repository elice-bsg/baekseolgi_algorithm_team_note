import sys

# Q. input = sys.~ 로 하면 왜 맨 처음 입력만 받을까요? or 인식할까요?

# bing: 플레이어, answer_sheet: 빙고 외칠 숫자
bingo = []
answer_sheet = []
for _ in range(10):
    if _ < 5:
        bingo.append(list(map(int, sys.stdin.readline().split())))
    else:
        answer_sheet.extend(list(map(int, sys.stdin.readline().split())))

# 플레이어의 빙고 속 숫자 1~25의 위치를 기록합니다.
idx_dic = {}
for i in range(5):
    for j in range(5):
        num = bingo[i][j]
        idx_dic[num] = i * 5 + j

# 숫자를 외칠 때마다 X 칠 빙고판을 기록합니다.
X_bingo = [[False for i in range(5)] for j in range(5)]

# 빙고판을 보고 3빙고가 맞는지 확인하는 함수
def is_bingo(sheet):
    cnt = 0
    for line in sheet:
        if line == [True] * 5:
            cnt += 1
    for line in list(map(list, zip(*sheet))):
        if line == [True] * 5:
            cnt += 1
    if sheet[2][2]:
        if [sheet[0][0], sheet[1][1], sheet[3][3], sheet[4][4]] == [True] * 4:
            cnt += 1
        if [sheet[4][0], sheet[3][1], sheet[1][3], sheet[0][4]] == [True] * 4:
            cnt += 1
    if cnt >= 3:
        return True
    else:
        return False

# 빙고 3개가 나올 수 있는 숫자 최솟값은 12개
# 만약 중심에 X가 없으면 최솟값은 13개
# 11개까지는 빙고가 나올 수 없으니 X만 기록한다.
# 그 후로는 is_bingo로 빙고 3줄인지 확인하기
# X는 true로 표기

t = 0  # 숫자 몇 개째 불렀는지 확인
for n in answer_sheet:
    idx = idx_dic[n]
    X_bingo[idx // 5][idx % 5] = True
    t += 1
    if t == 12 and X_bingo[2][2]:
        if is_bingo(X_bingo):
            print(t)
            break
    elif t > 12:
        if is_bingo(X_bingo):
            print(t)
            break