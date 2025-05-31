# part 1:

with open("encoded.bin", "rb") as bin:
    encoded = bin.read()

print(encoded)



translate = '{"showpassword":"no","bgcolor":"#ffffff"}'

print(len(encoded), len(translate))


key = []
for i in range(len(encoded)):
    key.append(chr(encoded[i] ^ ord(translate[i])))

print('(' + "".join(key) + ')')

# part 2:

key = """eDWoODWoeDWxRwV"kJjaHT{	o| FeDW+~"""

pt = '{"showpassword":"yes","bgcolor":"#ffffff"}'

print(len(key), len(pt))

ct = []
for i in range(len(key)):
    ct.append(chr(ord(key[i]) ^ ord(pt[i])))

print('(' + "".join(ct) + ')')

# troubleshooting:

# with open("encoded.bin", "rb") as f:
#     encoded_2 = f.read()
#
# print(encoded_2)

# f$
# '8￾7 � uUG=2Ghu
# 6uUGg1	"1	G9


# x = """f$
# 3'7   uUG*8MIf+; fmMF"1	"1M"""
#
# y = """f$
# 3'7   uUG*8MIf+; fmMF"1	"1M"""
#
# print('(')
# for i in range(len(x)):
#     if x[i] != y[i]:
#         print(f"'{x[i]}' '{y[i]}'")


print(repr("""f$
'8#
6uUGg1	"1	G9"""))