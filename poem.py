import re
# 选择字典，可以自行替换为其他语言
lines = open('zyenpheng.txt', encoding='utf-8').readlines()

# 读取字典
chars = []
dictionary = {}

for line in lines:
    char = line.split()
    # 将每个字及其读音添加至dictionary中，多音字的多个读音合并为一个并用/分割
    if char[0] in dictionary:
        pron = dictionary[char[0]]
        dictionary[char[0]] = pron + '/' + char[1]
    else:
        dictionary[char[0]] = char[1]

# 输入输出文件
poem = open('input.txt', encoding='utf-8').readlines()
out = open('output.txt', 'w', encoding='utf-8')

for line in poem:
    # 将所有标点符号替换为空格
    line = line.replace("[", "")
    line = line.replace("]", "")
    line = re.sub("\d+", "", line)
    line = re.sub("[，。？！：；“”「」『』、]+", " ", line)

    # 分成上下联
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
