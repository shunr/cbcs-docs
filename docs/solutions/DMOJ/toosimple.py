ONE = True
TWO = ONE + ONE
THREE = TWO + ONE
FOUR = TWO + TWO
FIVE = FOUR + ONE
SIX = FIVE + ONE
SEVEN = SIX + ONE
EIGHT = SEVEN + ONE
NINE = SEVEN + TWO
TEN = TWO * FIVE

H = TEN * SEVEN + TWO
e = ONE + TEN * TEN
l = TEN * TEN + EIGHT
o = TEN + TEN * TEN + ONE
COMMA = FOUR * TEN + FOUR
SPC = THREE * TEN + TWO
W = EIGHT * TEN + SEVEN
r = TEN * TEN + TEN + FOUR
d = TEN * TEN
EX = TEN * THREE + THREE

meme = [H, e, l, l, o, COMMA, SPC, W, o, r, l, d, EX]

kek = str()
for m in meme:
  kek += chr(m)
print(kek)