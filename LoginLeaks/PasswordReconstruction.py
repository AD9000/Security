#!/usr/bin/python3

def reconstruct(parts):
    keys = set(''.join(parts))
    values = [set([]) for i in range(len(keys))]    
    prevChars = dict(zip(keys, values))
    for i in parts:
        for j in range(1, len(i)):
            prevChars[i[j]].add(i[j - 1])
            if (j > 1):
                prevChars[i[j]].add(i[j-2])

    # print(''.join(sorted(prevChars, key=lambda k: len(prevChars[k]), reverse=True)))
    print(''.join(sorted(prevChars, key=lambda k: len(prevChars[k]))))

with open('test.txt') as f:
    problem = [x.strip() for x in f]
    parts = list(set(problem))
    reconstruct(parts)