# outcome = { 'Draw': 3, 'Win': 6, 'Loss': 0}

# val =  {
#             'rock' :  ('A', 'X'),
#             'paper' : ('B', 'Y'),
#             'scissors' : ('C', 'Z')
#         }


# with open(r'C:\Users\HP\Desktop\advent_of_code\Day_2\data.txt') as f:
#     for x in f:
#         base = 0
#         in_a, in_b = x.strip().split() #input from file
#         # print(base)
#         for x, v in (val.items()):
#             if in_a in v:
#                 in_a = x
#             if in_b in v:
#                 in_b = x
#                 base += n_val[x]
#         # print(x)
#              #added it play value to base
#         if in_a == in_b:
#             result =  ('Draw', 'Draw')
#         if (in_a, in_b) == ('rock', 'paper'):
#             result = ('Loss', 'Win')
#         if (in_a, in_b) == ('rock', 'scissors'):
#             result = ('Win', 'Loss')
#         if (in_a, in_b) == ('paper', 'scissors'):
#             result = ('Loss', 'Win')
#         if (in_a, in_b) == ('paper', 'rock'):
#             result = ('Win', 'Loss')
#         if (in_a, in_b) == ('scissors', 'paper'):
#             result = ('Win', 'Loss')
#         if (in_a, in_b) == ('scissors', 'rock'):
#             result = ('Loss', 'Win')
#         base += outcome[result[1]]
#         # print(base)

#         total.append(base)
#         base = 0


val =  {
            'A':'rock',
            'B':'paper' ,
            'C':'scissors'
        }

n_val = {
        'rock' : 1,
        'paper' : 2,
        'scissors': 3
        }

total = []


#check for the of input given

l_val = { 'paper': 'rock', 'scissors': 'paper', 'rock': 'scissors' }

w_val = { 'rock': 'paper', 'scissors': 'rock', 'paper': 'rock'}

with open(r'C:\Users\HP\Desktop\advent_of_code\Day_2\data.txt') as f:
    for x in f:
        base = 0
        in_a, in_b = x.strip().split() #input from file
        # print(base)
        if in_b == 'Y': #draw
            in_b = val.get(in_a)
            base += 3
            base += n_val[in_b]


        if in_b == 'X': #lose
            in_b = l_val[val.get(in_a)]
            base += n_val[in_b]


        if in_b == 'Z': #win
            in_b = w_val[val.get(in_a)]
            base += n_val[in_b]
            base += 6

        total.append(base)
print(sum(total))

# x = [('A', 'Y'),
# ('B', 'X'),
# ('C', 'Z')]
# tot = []
# for in_a, in_b in x:
#     base = 0
#     # print(base)
#     if in_b == 'Y': #draw
#         in_b = val.get(in_a)
#         base += 3
#         base += n_val[in_b]
#     if in_b == 'X': #lose
#         in_b = l_val[val.get(in_a)]
#         base += n_val[in_b]
#     if in_b == 'Z': #win
#         in_b = w_val[val.get(in_a)]
#         base += n_val[in_b]
#         base += 6
#     tot.append(base)

# print(sum(tot))