import random
test = "{><!A9-n$)(e*WzqL_&Zf2R6^d}"
runs = 2500

for i in range(runs):
    cp = test
    a = random.randint(0, len(test)-3)
    b = random.randint(a + 1, len(test) - 2)
    c = random.randint(b + 1, len(test) - 1)

    print (test[a] + test[b] + test[c])
