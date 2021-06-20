# 正則表達列表
# https://www.runoob.com/python/python-reg-expressions.html
# 正則除字+格式化 > 去空白(不知道怎正則去空白) > 存去a1[]
import re
 
 #region txt
txt = """
01	序章-はじまり-	2:24
02	偽りの楽園	3:00
03	蒼穹	1:13
04	少女の想い	1:43
05	仲間	1:37
06	触れ合い	1:22
07	真実	1:27
08	焦り	1:12
09	迷い	1:38
10	苦悩	1:59
11	すれ違う友	2:37
12	流す涙	1:43
13	ワルキューレ	1:47
14	ファフナー-誓い-	2:03
15	予兆	1:49
16	出現	2:07
17	フェストゥム-侵蝕-	1:38
18	あなたはそこにいますか-戦い-	2:10
19	同化危機	1:05
20	決意-旅立ち-	1:47
21	ナイトヘーレ開門	2:42
22	哀しみの蒼穹	3:11
23	翔子-SHOKO-	3:14
24	TSUBAKI-子守唄-	2:00
25	命	1:41
26	希望	1:13
27	いのり	2:14
28	そら	1:31
29	FAFNER in the azure"""
#endregion

# 正則刪字 \s = DEL 空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。 \t 跳格\r 回车\n 换行
# 正則刪字 \d = DEL數字
num = re.sub(r'\s', " ", txt)
num = re.sub(r'\d', " ", num)
# 不知怎刪特殊字元: 順便以它區分文字存成 array
num = num.split(':')
print (num)
a1 = []
# 一筆一筆去空白並寫入 a1[]
for i in num:
    i = i.replace(" ", "")
    print(i)
    a1.append(i)

print(a1)