def cipher(s):
    return ''.join(chr(219-ord(si)) if 'a'<=si<='z' else si for si in s)

print(cipher("iphone"))
print(cipher("rkslmv"))
