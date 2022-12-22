generated_list = []

def generate_number(number):
    tmp = str(number)
    tmp_list = [int(token) for token in tmp]

    return number + sum(tmp_list)

for i in range(1, 10001):
    tmp = generate_number(i)
    if tmp not in generated_list:
        generated_list.append(tmp)

generated_list = set(generated_list)

for i in range(1, 10001):
    if i not in generated_list:
        print(i)