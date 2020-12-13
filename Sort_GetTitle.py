# 抓標題 
# 透過 === 抓 index +1 = 下一行是標題 > 如果該標題 有出現過 pass 沒有出現過 加入array[] > 輸出array[] > GET 所有出現過的 標題
import os

# 要刪除的行 包含的文字
del_text = "你们告诉我怎样可以做得更"
# 要選取的行 包含的文字
sel_text = "========"

save_file_array = []
save_index_array = []
save_title_array = []
openfilename = 'C:/Users/admin/Desktop/My-Clippings-all.txt' # 要開啟的檔案路徑
savefilename = 'C:/Users/admin/Desktop/test-save.txt' # 要存檔的名稱與路徑
# 開啟要編輯的檔案
with open (openfilename, 'r', encoding='UTF-8') as file :
    
    #region Get_Title
    # 因為進得來的只有 "選擇的" 所以才加入不了
    # 加編號一行一行跑
    file=file.readlines()
    for i,line in enumerate(file):
        # 如果是要選的 抓index +1 存入 array
        if sel_text in line:
            x = i + 1
            save_index_array.append(x)
        # 如果再 array裡 無視 如果不再 加入
        elif i in save_index_array:
            if line in save_title_array:
                print('已有,不加入掠過')
            else:
                save_title_array.append(line)
    # 印出擷取出的 標題
    for i in save_title_array:
        print(i)
    #endregion                


