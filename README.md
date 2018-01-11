# 为古诗文自动标注中古汉语拼音（polyhedron版）

目前仅限于繁体字输入，未来将加入自动简繁转换。

使用方法：
1. 前往[维基文库](https://zh.wikisource.org/wiki/Wikisource:%E9%A6%96%E9%A1%B5)
1. 搜索律诗或绝句并粘贴至`poem.txt`中，或搜索古文、杂言诗粘贴至`article.txt`中
1. 运行`poem.py`  或`article.py`，将自动输出注音于`output.txt`中

此程序可以用来进行其他语言的自动注音，前往此仓库[Chinese_dialect_Rime_dict
](https://github.com/laubonghaudoi/Chinese_dialect_Rime_dict)下载对应的`.dict.yaml`文件并手动修改为txt纯文本，替换`zyenpheng.txt`即可。

输出示例在`\示例输出`文件夹中，以下为参考效果：

```
chyih ghrua/ghruah/hrua jeu/jeuh jeu/jeuh ghang/ghangh/ghrang/ghrangh biuh/biuk cjix 
se chjyih/chjyt to muon prak jo lix 
翠華搖搖行復止
西出都門百餘里
liuk kyon piu/piux/puot/pyot pyat myo nad/nah gha/ghax 
qyan/qyanx tryenh/tryenx nga/ngiex mii mrax zen siix 
六軍不發無奈何
宛轉蛾眉馬前死
hrua den/denh qye/qyex diih myo njin sju/sjuh 
chyih gjeu/gjeuh kim ciak ngyuk sau du 
花鈿委地無人收
翠翹金雀玉搔頭
kyon yang/yangh qiemx mjenh kiuh piu/piux/puot/pyot tok 
ghuai khan/khanh huet lyih siang/siangh ghua/ghuah liu 
君王掩面救不得
回看血淚相和流


yon sieu yoh/yox ceh 
雲銷雨霽
chaix driet/thriet khyo/qu mieng 
彩徹區明
lak ghra jo/joh/jox ko muk/myoh ze/zeh/crai pyoi
落霞與孤鶩齊飛
chiu sjyix gyungh/kyung driang/driangh/triangx then qjit srik 
秋水共長天一色
ngio cju chjangh myanx 
漁舟唱晚
hiangx giung brang lex/lie/lua cji pjin 
響窮彭蠡之濱
ngranh drinh kieng ghan 
雁陣驚寒
sjeng duanx/tuanh/tuanx ghrang jang cji phox 
聲斷衡陽之浦
```

计划添加功能：

1. [x] 加入杂言诗和古文的支持，以摆脱上下联必须对仗工整的限制
2. [ ] 自动将简体字转换为繁体字
1. [ ] 加入平仄标记