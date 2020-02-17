# 去除不要字元 / 轉繁體 / 另存
import time
import random
import progressbar #進度條 測試用
from zhconv import convert #簡轉繁

datas = []
cleartext = []

x = 0
bar = progressbar.ProgressBar(max_value=1000000) #進度條 測試用

with open ('C:/Users/admin/Desktop/z.txt', 'r', encoding='UTF-8') as f :
    print(f)
    for line in f :
        text = ('不要的行 裡面的字')
        line = line.replace(" ", "") #去除空格
        line = convert(line, 'zh-tw')

        print(line)

        if text in line:
            x +=1
            print(x)
        else:
            with open ('C:/Users/admin/Desktop/z.txt', 'a', encoding='UTF-8') as f : #另存為z.txt
                f.write(line)
                print('------------------------', line, '分隔線分隔線分隔線分隔線分隔線分隔線分隔線')
                f.close()
