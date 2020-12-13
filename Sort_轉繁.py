# 簡轉繁
from zhconv import convert # 簡轉繁
import os

openfilename = 'C:/Users/admin/Desktop/test-摘出.txt' # 要開啟的檔案路徑
savefilename = 'C:/Users/admin/Desktop/test.txt' # 要存檔的名稱與路徑

#region 開啟要編輯的檔案 Sample用
# with open (openfilename, 'r', encoding='UTF-8') as file :
    # print('開檔案讀取')
#endregion

with open (savefilename[:-4] + '-轉繁.txt', 'a', encoding='UTF-8') as f :               
    
    #region 轉繁體 str ver
    text = '下面介绍一个5分钟之内即可完成的认知行为疗法的练习。 这种练习心理的训练，我称它为“心练”。 你不需要考虑过多，凭直觉回答以下七个问题即可。'
    text = convert(text, 'zh-tw')
    f.write(text)
    #endregion 
    
    #region 轉繁體 array ver
    text_array = []
    text_array.append('下面介绍一个5分钟之内即可完成的认知行为疗法的练习')
    text_array.append('这种练习心理的训练')

    for line in text_array:
        line = convert(line, 'zh-tw')
        f.write(line)
    #endregion

    f.close()   