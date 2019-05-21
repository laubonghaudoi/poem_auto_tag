# 為古詩文自動標註中古漢語拼音（polyhedron版）

因為簡體字的歸並問題，本程序僅支持繁體字輸入。

使用方法：

1. 前往[維基文庫](https://zh.wikisource.org/wiki/Wikisource:%E9%A6%96%E9%A1%B5)
2. 搜索繁體版古詩詞或古文並粘貼至`input.txt`中
3. 如果文體是律詩或絕句，則運行`poem.py`，如果是古文、古體詩、雜言詩等則運行`article.py`，註音將自動輸出至`output.txt`中

此程序可以用來進行其他語言的自動註音，前往此倉庫[Chinese_dialect_Rime_dict
](https://github.com/laubonghaudoi/Chinese_dialect_Rime_dict)下載對應的`.dict.yaml`文件並手動修改為txt純文本，替換`zyenpheng.txt`即可。

輸出示例在頂層目錄的各文件夾中。以下為參考效果：

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

## 參考

[rime-middle-chinese](https://github.com/biopolyhedron/rime-middle-chinese