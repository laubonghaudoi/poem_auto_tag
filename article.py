import re

# 选择字典，可以自行替换为其他语言
lines = open('zyenpheng.txt', encoding='utf-8').readlines()

# 读取字典
chars = []
dictionary = {}

for line in lines:
    char = line.split()
    # 将每个字机器读音添加至dictionary中，多音字的多个读音合并为一个并用/分割
    if char[0] in dictionary:
        pron = dictionary[char[0]]
        dictionary[char[0]] = pron + '/' + char[1]
    else:
        dictionary[char[0]] = char[1]

# 输入输出文件
article = open('article.txt', encoding='utf-8').readlines()
out = open('output.txt', 'w', encoding='utf-8')

for paragraph in article:
    try:
        line = paragraph.split()[0]
    except:
        continue

    if not line:
        # 如遇到换行符、空段落则跳过
        continue
    else:
        line = line.replace("[", "")
        line = line.replace("]", "")
        line = re.sub("\d+", "", line)
        line = re.sub("[，。？！：；“”「」『』、]+", " ", line)

    sentences = line.split()

    for prose in sentences:
        for char in list(prose):
            try:
                out.write(dictionary[char] + ' ')
            except KeyError:
                out.write('ERR' + ' ')
        out.write('\n')
        out.write(prose)
        out.write('\n')

out.close()
