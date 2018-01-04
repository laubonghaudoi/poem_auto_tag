lines = open('zyenpheng.txt', encoding='utf-8').readlines()

chars = []
dictionary = {}

for line in lines:
    char = line.split()
    if char[0] in dictionary:
        pron = dictionary[char[0]]
        dictionary[char[0]] = pron + '/' + char[1]
    else:
        dictionary[char[0]] = char[1]

poem = open('poem.txt', encoding='utf-8').readlines()
out = open('output.txt', 'w', encoding='utf-8')

for line in poem:
    line = list(line)
    if '，' in line:
        line[line.index('，')] = ' '
    if '。' in line:
        line[line.index('。')] = ' '
    if '？' in line:
        line[line.index('？')] = ' '
    if '！' in line:
        line[line.index('！')] = ' '
    line = ''.join(line)


    sentence = line.split()

    up = sentence[0]
    down = sentence[1]
    
    for char in up:
        try:
            out.write(dictionary[char] + ' ')
        except KeyError:
            out.write('ERR' + ' ')

    out.write('\n')

    for char in down:
        try:
            out.write(dictionary[char] + ' ')
        except KeyError:
            out.write('ERR' + ' ')
    out.write('\n')

    out.write(up + '\n' + down + '\n')

out.close()