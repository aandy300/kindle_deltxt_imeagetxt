import os, time, random, re
# 簡轉繁
from zhconv import convert 
# 開啟文件、存檔ui
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import Tk


# 結論記憶體出問題?
# 結論 >  用 IF[01234]..... 

# 要刪除的行 包含的文字
del_text = "樊登", "您在" 
# 暫存取用
text_array = []
ok_text = []
# tkinter 開始儲存ui
filename = askopenfilename(filetypes=[("Image files", "*.txt"), ("All Files", "*.*")]) # 檔案類型 篩選
savefilename= asksaveasfilename(filetypes=[("Image files", "*.txt"), ("All Files", "*.*")]) 
# we don't want a full GUI, so keep the root window from appearing # 隱藏tk ui
Tk().withdraw() 
# count用
x = 0

# 20210722 存檔修改 # savefilename = 'C:/Users/admin/Desktop/00/01.txt' # 要存檔的名稱與路徑
# 20210911 改一下備註

# 開啟檔案叫f
with open (filename, 'r', encoding='UTF-8') as f :

    # type(object_or_name, bases, dict) type(object) -> 印出對象的類型 
    # type(name, bases, dict) -> 製作一個新類型
    type(del_text)

    # 一行一行印出
    for line in f:
        # replace去空白
        line = line.replace(" ", "")
        # 把要刪除的字一個一個跑過一變 有的話挑出並計數 > 沒有的加入到 ok_text.append(line)
        for del_ary in del_text:
            if del_text[0] in line:
                x +=1
            if del_text[1] in line:
                x +=1
            elif line in ok_text:
                print('0')
            else:
                ok_text.append(line)
                
    # 跑過濾掉已經過濾掉刪除字句子 > 開啟文件(準備寫入用) > 轉繁體字 > 寫入並加入換行符號 > 關閉
    for line in ok_text:
        with open (savefilename + '.txt', 'a', encoding='UTF-8') as f : 
            line = convert(line, 'zh-tw')
            f.write(line+'\n')
            f.close()
        print(line)