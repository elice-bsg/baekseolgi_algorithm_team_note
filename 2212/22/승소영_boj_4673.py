numbers = set()
not_self = set()

for i in range(1,10001):
    numbers.add(i)
    for j in str(i):
        i += int(j)
    not_self.add(i)

self_number = sorted(numbers - not_self)
for i in self_number:
    print(i)