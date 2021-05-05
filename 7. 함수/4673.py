n=list(range(1,10_001))
remove_list = []
for num in n:
    for i in str(num):
        num += int(i)
    if num <= 10_000:
        fomove_list.append(num)

for remove_num in set(remove_list):
    n.remove(remove_num)
for self_num in n:
    print(self_num)