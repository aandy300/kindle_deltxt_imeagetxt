import os, time, random
from zhconv import convert # 簡轉繁

from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import Tk
import re

# 結論記憶體出問題?

# 結論 >  用 IF[01234]..... 

del_text = "樊登", "您在" # 要刪除的行 包含的文字
text_array = []
ok_text = []
filename = askopenfilename(filetypes=[("Image files", "*.txt"), ("All Files", "*.*")]) # 檔案類型 篩選

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing # 隱藏tk ui
savefilename = 'C:/Users/admin/Desktop/新增資料夾/01.txt' # 要存檔的名稱與路徑

x = 0

with open (filename, 'r', encoding='UTF-8') as f :

    type(del_text)

    for line in f:
        line = line.replace(" ", "")
        for del_ary in del_text:
            if del_text[0] in line:
                x +=1
            if del_text[1] in line:
                x +=1
            elif line in ok_text:
                print('0')
            else:
                ok_text.append(line)
                


    for line in ok_text:
        with open (savefilename, 'a', encoding='UTF-8') as f : 
            line = convert(line, 'zh-tw')
            f.write(line+'\n')
            f.close()
        print(line)