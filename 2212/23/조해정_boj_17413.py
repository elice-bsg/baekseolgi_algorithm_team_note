import sys

input = sys.stdin.readline().strip()
ss = input
rss = []
part = []
tag = False
for val in ss:
    # 일단 태그인 거 전부 제외
    if tag:
        if val == ">":
            tag = False
        rss.append(val)
        continue
    # 태그 시작일 때, 기존 문자열 거꾸로 더하기
    if val == "<":
        tag = True
        if part:
            rss += reversed(part)
            part = []
        rss.append(val)
        continue
    # 태그 제외 후, 공백일 때 그 전 단어 거꾸로 더하기
    if val == " ":
        rss += reversed(part)
        rss.append(" ")
        part = []
    else:
        part.append(val)
# 마지막 문자열 남은 거 있으면 더해주기
if part:
    rss += reversed(part)
print("".join(rss))

