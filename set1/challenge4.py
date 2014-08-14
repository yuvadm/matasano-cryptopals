from challenge3 import get_max_single_char_xor

res = []
with open('challenge4.txt', 'r') as f:
    for line in f.readlines():
       res.append(get_max_single_char_xor(line))

print max(res, key=lambda x: x[0]) 
