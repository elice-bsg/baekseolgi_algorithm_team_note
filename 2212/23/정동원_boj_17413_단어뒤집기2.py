import sys

word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":  # 열린 괄호를 만나면 증가시키고
        i += 1
        while word[i] != ">":  # 닫힌 괄호를 만날 때 까지 인덱스를 증가시킨다
            i += 1
        i += 1  # 닫힌 괄호를 만난 후 인덱스를 증가시킨다
    elif word[i].isalnum():  # isalnum메소드로 숫자나 알파벳을 만나는지 check
        start = i
        while i < len(word) and word[i].isalnum():  # 숫자나 알파벳일 경우
            i += 1
        aphnum = word[start:i]  # 숫자,알파벳 범위에 있는 것들을
        aphnum.reverse()  # 뒤집고
        word[start:i] = aphnum  # 뒤집은 값들을 다시 대입
    else:  # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i += 1  # 이므로 인덱스 증가

print("".join(word))
