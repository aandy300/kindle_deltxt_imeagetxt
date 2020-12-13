# 擷取內文
# 開啟要編輯的檔案 > 擷取 目標標題的index > index +3 = 內文 > 儲存內文置array > 輸出array內文 另存檔案
import os

# 要選取的行 包含的文字
sel_text = "认生的人"

save_file_array = []
save_index_array = []
openfilename = 'C:/Users/admin/Desktop/My-Clippings-all.txt' # 要開啟的檔案路徑
savefilename = 'C:/Users/admin/Desktop/My-Clippings-all-认生的人：如何克服社交焦虑.txt' # 要存檔的名稱與路徑

# 開啟要編輯的檔案 > 擷取 目標標題的index > index +3 = 內文 > 儲存內文置array
with open (openfilename, 'r', encoding='UTF-8') as file :
    #region 擷取標題inde +3

    # 加編號一行一行跑
    file=file.readlines()
    for i,line in enumerate(file):
        # 如果是要選的字 in line : index +3 存進 save_index_array[] 方便之後用編號抓內文
        if sel_text in line:
            x = i + 3
            save_index_array.append(x)
        # 如果 index in save_index_array[] = 是內文 > 存入 save_file_array[] 等之後輸出
        elif i in save_index_array:
            save_file_array.append(line)
    #endregion    

# 輸出內文
with open (savefilename[:-4] + '-Clip摘出.txt', 'a', encoding='UTF-8') as f : 
    for i in save_file_array:
        f.write(i)
    f.close()                


