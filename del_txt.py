<<<<<<< HEAD
# 確認檔案是否在 > 去除不要的字元 > 轉繁體 > 另存
=======
# 去除不要字元 / 轉繁體 / 另存
import time
import random
# import progressbar #進度條 測試用
from zhconv import convert #簡轉繁
>>>>>>> 81a450842a61196139215da657e34e1085ecf335

# 檔案是否存在 中文解說
# https://blog.gtwang.org/programming/python-howto-check-whether-file-folder-exists/

import os, time, random
import progressbar # 進度條 測試用
from zhconv import convert # 簡轉繁

x = 0
<<<<<<< HEAD
# 進度條 測試用(方便瞭解進度)
bar = progressbar.ProgressBar(max_value=1000000) 

# 開啟要編輯的檔案 C:/Users/admin/Desktop/1.txt 檔名 1.txt
with open ('C:/Users/admin/Desktop/1.txt', 'r', encoding='UTF-8') as f :
=======
# bar = progressbar.ProgressBar(max_value=1000000) #進度條 測試用

with open ('C:/Users/admin/Desktop/1.txt', 'r', encoding='UTF-8') as f :
    print(f)
    for line in f :
        text = ('黃色')
        line = line.replace(" ", "") #去除空格
        line = convert(line, 'zh-tw')
>>>>>>> 81a450842a61196139215da657e34e1085ecf335

    # 確認檔案是否存在 存在的話刪除 防止追加寫入
    if os.path.isfile('C:/Users/admin/Desktop/z.txt'):
        print("檔案存在。")
        os.remove('C:/Users/admin/Desktop/z.txt')
    else:
        print("檔案不存在。")

    # 去除指定文字 將指定文字以外 存入 z.txt
    for line in f :
        # 通過輸入的字 來刪除文本不要的行
        text = ('您在位置')
        # 去除空格
        line = line.replace(" ", "") 
        
        # 去除的行 去1 + x+1
        if text in line:
            x += 1
        # 沒有被去除的存入 z.txt
        else:
            # 簡體字轉繁體字
            line = convert(line, 'zh-tw')
            # "寫入"z.txt  非另存為z.txt
            with open ('C:/Users/admin/Desktop/z2.txt', 'a', encoding='UTF-8') as f : 
                f.write(line)
                f.close()
    print('去除的行數:', x)