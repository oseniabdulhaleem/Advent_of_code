a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
a_ = list(range(1, 53))
p = {}
for x,y in zip(a, a_):
    p |= [(x,y)]
#to convert the letter to their values
def convert(x, p=p):
        # print(x.translate(p))
    return p[x]

#to split them

def cut(a):
    num = (len(a)// 2)
    # print(num)
    return list(set(a[:num]) & set(a[num:]))[0]

#to get values from file
total = []
with open(r'C:\Users\HP\Desktop\advent_of_code\Day_3\data.txt') as f:
    for x in f:
        x = cut(x.strip())
        # print(x)
        p = convert(x)
        total.append(p)
    print(sum(total))
    

