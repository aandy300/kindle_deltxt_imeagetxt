# 圖片辨識 / 轉繁體
from PIL import Image, ImageEnhance
from zhconv import convert #簡轉繁
import pytesseract
# tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open('C:/Users/admin/Desktop/0.jpeg')

# #彩度
# enh_col = ImageEnhance.Color(img)
# color = -3
# image_colored = enh_col.enhance(color)
# image_colored.show()

# #對比
# enh_con = ImageEnhance.Contrast(img)
# contrast = 1.5
# image_contrasted = enh_con.enhance(contrast)
# image_contrasted.show()

# #亮度
# enh_bri = ImageEnhance.Brightness(img)
# brightness = 1.2
# image_brightened = enh_bri.enhance(brightness)
# image_brightened.show()

# L 灰色
img = img.convert('L') 
# img.show()

#銳利度
enh_sha = ImageEnhance.Sharpness(img)
sharpness = 3.0
image_sharped = enh_sha.enhance(sharpness)
image_sharped.show()

text = pytesseract.image_to_string(img, lang='chi_sim') #辨識
text = text.replace(" ", "") #去除空格
print('------------------')
print(convert(text, 'zh-tw')) #簡轉繁
print('------------------')


