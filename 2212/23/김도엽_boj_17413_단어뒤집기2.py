import sys
input = sys.stdin.readline

sentence = input().rstrip()

'''
1. 태그가 진행중이지만, 끝을 만나지 못한 경우 -> 계속 만나는 단어들을 붙여준다
2. 태그가 진행중인데, 끝을 만난 경우 -> isTag를 False로 돌린다
3. 태그가 진행중이지 않고, 태그의 시작도 만나지 않은 경우 -> 계속 wordStack에 쌓는다
4. 태그가 진행중인건 아니었지만, 태그의 시작 지점을 만난 경우 -> wordStack을 후처리하고, isTag를 true로 맞추고, wordStack을 비운다
'''

# 태그의 시작을 만났기 때문에 쌓여있는 문자열을 처리하는 함수
def flush_sentence(sentence):
    result = ""
    word_list = sentence.split()

    for i, word in enumerate(word_list):
        result += word[len(word) - 1::-1]
        if i != len(word_list) - 1:
            result += ' '

    return result
def solution(sentence):
    answer = ""
    is_tag = False
    word_stack = ""

    for token in sentence:
        if not is_tag and token != '<':
            word_stack += token
        elif not is_tag and token == '<':
            tmp = flush_sentence(word_stack)
            answer += (tmp + token)
            is_tag = True
            word_stack = ""
        elif is_tag and token != '>':
            answer += token
        elif is_tag and token == '>':
            is_tag = False
            answer += token

    answer += flush_sentence(word_stack)

    return answer

print(solution(sentence))