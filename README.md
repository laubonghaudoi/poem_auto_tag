# 为古诗文自动标注中古汉语拼音（polyhedron版）

目前仅限于上下联对仗工整文体的自动注音，且**必须输入繁体字**。

使用方法：
1. 前往[维基文库](https://zh.wikisource.org/wiki/Wikisource:%E9%A6%96%E9%A1%B5)
1. 搜索律诗并粘贴至`poem.txt`中
1. 运行`poem.py`，将自动输出注音于`output.txt`中

此程序可以用来进行其他语言的自动注音，前往此仓库[Chinese_dialect_Rime_dict
](https://github.com/laubonghaudoi/Chinese_dialect_Rime_dict)下载对应的`.dict.yaml`文件并手动修改为txt纯文本，替换`zyenpheng.txt`即可。

计划添加功能：

1. 加入杂体诗和古文的支持，以摆脱上下联必须对仗工整的限制
1. 加入平仄标记