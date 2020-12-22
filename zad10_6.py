d = {}
with open('dictionary.txt','r',encoding='utf8') as fo:
    for line in fo:
        (key, val) = line.rstrip("\n").split(':')
        d[key] = val
    fo.close()
    print(d.keys(),d.values(),sep="\n")