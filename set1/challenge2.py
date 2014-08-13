a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'
c = '746865206b696420646f6e277420706c6179'

def fixed_xor(a, b):
    return ''.join([hex(ord(i) ^ ord(j))[2:] for i,j in zip(a.decode('hex'), b.decode('hex'))])

assert fixed_xor(a, b) == c
