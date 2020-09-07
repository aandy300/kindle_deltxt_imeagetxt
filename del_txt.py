# 確認檔案是否在 > 去除不要的字元 > 轉繁體 > 另存

# 待更改點 要刪除的文字 改成ARRAY多個? 追加INPUT?

# 檔案是否存在 中文解說
# https://blog.gtwang.org/programming/python-howto-check-whether-file-folder-exists/

import os, time, random
import progressbar # 進度條 測試用
from zhconv import convert # 簡轉繁

x = 0
# 進度條 測試用(方便瞭解進度)
bar = progressbar.ProgressBar(max_value=1000000) 

# 開啟要編輯的檔案 C:/Users/admin/Desktop/1.txt 檔名 1.txt
with open ('C:/Users/admin/Desktop/1.txt', 'r', encoding='UTF-8') as f :

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