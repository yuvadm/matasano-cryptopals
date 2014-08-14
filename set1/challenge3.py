x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def score_plaintext(s):
    letters = filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z', s)
    return float(len(letters)) / len(s)

def get_max_single_char_xor(s):
    res = []
    for i in range(256):
        chrs = [chr(ord(s) ^ i) for s in x.decode('hex')]
        res.append([score_plaintext(chrs), ''.join(chrs)])
    return max(res, key=lambda x: x[0])

if __name__ == '__main__':
    print get_max_single_char_xor(x)
