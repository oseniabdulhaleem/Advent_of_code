# import re
# with open(r'C:\Users\HP\Desktop\advent_of_code\Day_1\data.txt') as f:
#     x = 0
#     total = []
#     for line in f:
#         line = re.sub('(\d+)\n', lambda x: x.group(1), line)
#         if line == '\n':
#             total.append(x)
#             x = 0
#             continue
#         x += int(line)

#     print(max(total))


X = [c.strip() for c in open('data.txt')]
x,Y = 0, []
for c in X:
    if c == '':
        Y.append(x)
        x = 0
        continue
    x += int(c)
print(Y) 
p = 0
for _ in range(3):
    p += max(Y)
    Y.remove(max(Y))
print(p)



