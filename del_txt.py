import os, time, random
from zhconv import convert # 簡轉繁

from tkinter.filedialog import askopenfilename
from tkinter import Tk

# 確認檔案是否在 > 去除不要的字元 > 轉繁體 > 另存

# 待更改點  #########
# 要刪除的文字 改成ARRAY多個s

# 檔案是否存在 中文解說
# https://blog.gtwang.org/programming/python-howto-check-whether-file-folder-exists/

# GUI 用 tk
# https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog
# 存檔 GUI
# https://stackoverflow.com/questions/19476232/save-file-dialog-in-tkinter

# 使用說明 #################################

text = "的標註|添加於" # 要刪除的行 包含的文字

# 未實裝 tkinter 
# filename = askopenfilename()
filename = askopenfilename(filetypes=[("Image files", "*.png"), ("All Files", "*.*")]) # 檔案類型 篩選
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing # 隱藏tk ui

openfilename = 'C:/Users/admin/Desktop/test.txt' # 要開啟的檔案路徑
savefilename = 'C:/Users/admin/Desktop/01.txt' # 要存檔的名稱與路徑
x = 0 # 去除的行數 計數用
# 開啟要編輯的檔案
with open (openfilename, 'r', encoding='UTF-8') as f :

    # 確認檔案是否存在 存在的話刪除 防止追加寫入
    if os.path.isfile('C:/Users/admin/Desktop/z.txt'):
        print("檔案存在。")
        os.remove('C:/Users/admin/Desktop/z.txt')
    else:
        print("檔案不存在。")

    # 去除指定文字 將指定文字以外 存入 z.txt
    for line in f :
        # 通過輸入的字 來刪除文本不要的行
        # text = ('您在位置')
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
            with open (savefilename, 'a', encoding='UTF-8') as f : 
                f.write(line)
                f.close()
    print('去除的行數:', x)