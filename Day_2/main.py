outcome = { 'Draw': 3, 'Win': 6, 'Loss': 0}

val =  {
            'rock' :  ('A', 'X'),
            'paper' : ('B', 'Y'),
            'scissors' : ('C', 'Z')
        }
n_val = {
        'rock' : 1,
        'paper' : 2,
        'scissors': 3
        }

total = []


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






#check for the of input given

l_val = { 'paper': ' rock', 'scissors': 'paper' }

w_val = { 'rock': 'paper', 'scissors': 'rock', 'paper': 'rock'}

with open(r'C:\Users\HP\Desktop\advent_of_code\Day_2\data.txt') as f:
    for x in f:
        base = 0
        in_a, in_b = x.strip().split() #input from file
        # print(base)
        if in_b == 'Y': #draw
        #     in_b = in_a
            for x,v in val.items():
                if in_b in v:
                    base += n_val[x]
                    in_a = x
                    in_b = x
        if in_b == 'X': #lose
            for x,v in val.items():
                if in_b in v:
                    base += n_val[x]
                if in_a in v:
                    in_a = x
            in_b = w_val[in_a]
        if in_b == 'Z': #win
            for x,v in val.items():
                if in_b in v:
                    base += n_val[x]
                if in_a in v:
                    in_a = x
            in_b = w_val[in_a]

        # print(in_a, in_b)
        # print(x)
             #added it play value to base
        if in_a == in_b:
            result =  ('Draw', 'Draw')
        if (in_a, in_b) == ('rock', 'paper'):
            result = ('Loss', 'Win')
        if (in_a, in_b) == ('rock', 'scissors'):
            result = ('Win', 'Loss')
        if (in_a, in_b) == ('paper', 'scissors'):
            result = ('Loss', 'Win')
        if (in_a, in_b) == ('paper', 'rock'):
            result = ('Win', 'Loss')
        if (in_a, in_b) == ('scissors', 'paper'):
            result = ('Win', 'Loss')
        if (in_a, in_b) == ('scissors', 'rock'):
            result = ('Loss', 'Win')
        base += outcome[result[1]]
        # print(base)
    
    
        total.append(base)
        # base = 0
print(sum(total))
