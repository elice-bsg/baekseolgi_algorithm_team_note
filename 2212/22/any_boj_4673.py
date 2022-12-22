my_numb_list = []


for a in range(10) :
    for b in range(10):
        for c in range(10):
            for d in range(10):
             my_numb = 1001*a+101*b+11*c+2*d
             my_numb_list.append(my_numb)

my_numb_list.sort()


for x in range(10001):
  if x in my_numb_list:
    continue
  print(x)