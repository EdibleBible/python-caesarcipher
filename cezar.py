teskt = input("Input the text")
split = list(teskt)
numer = input("Input the shift (in integers)")
i = len(split)
a = 0
t = ""
m = int(input("Encode: 0, Decode: 1"))
if (m == 1):
    numer = 0 - numer
while (i != 0):
    l = split[a]
    n = ord(l)
    if (n < 65 or n > 90):
        i -= 1
        a += 1
        continue
    n += numer
    while (n > 90):
        n -= 26
    while (n < 65):
        n += 26
    t += chr(n)
    i -= 1
    a += 1
print(t)