x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def score_plaintext(s):
    letters = filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z', s)
    return float(len(letters)) / len(s)

res = []
for i in range(256):
    chrs = [chr(ord(s) ^ i) for s in x.decode('hex')]
    res.append([score_plaintext(chrs), ''.join(chrs)])

print(max(res, key=lambda x: x[0])[1])
