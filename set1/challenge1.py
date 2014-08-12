import base64

s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def hex_str_to_base64(s):
    ba = bytearray([int(s[(i*2):(i*2)+2], 16) for i in range(len(s)/2)])
    return base64.b64encode(ba)

assert hex_str_to_base64(s) == 'expected'
