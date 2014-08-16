from itertools import cycle

s = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = 'ICE'
expected = '''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272\
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''

out = ''.join(['{:02x}'.format((ord(c) ^ ord(k))) for c, k in zip(s, cycle(key))])

assert out == expected 
