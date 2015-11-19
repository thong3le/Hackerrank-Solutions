from collections import OrderedDict
n = input()
order = OrderedDict()
for _ in range(n):
    item = raw_input().split()
    key = ' '.join(item[:-1])
    if key in order:
        order[key] += int(item[-1])
    else:
        order[key] = int(item[-1])
for k, v in sorted(order.items()):
    print k, v