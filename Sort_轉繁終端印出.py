# 直接開文件 > 轉繁體 > 終端機印出

# 簡轉繁
from zhconv import convert # 簡轉繁
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import Tk
import os

# tkinter 開始儲存ui
filename = askopenfilename(filetypes=[("Image files", "*.txt"), ("All Files", "*.*")]) # 檔案類型 篩選
# 隱藏tk ui
Tk().withdraw() 

with open (filename, 'r', encoding='UTF-8') as f :            
    
    for line in f:        
        line = convert(line, 'zh-tw')        
        print(line)