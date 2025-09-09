import random as r

test_dict = [{
    'Jet' : 'a',
    'Belle' : 'b',
    'Jared' : 'c'
}, 'pen']

rand_char = r.choice(test_dict)
print(rand_char)
