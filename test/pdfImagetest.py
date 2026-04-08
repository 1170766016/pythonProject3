import pandas as pd
import pdfplumber
from pdfminer.pdftypes import PDFStream

# 加载一个pdf文件
pdf = pdfplumber.open('./test.pdf')
page1 = pdf.pages[0]  # 第一个Page对象
page2 = pdf.pages[1]  # 第二个Page对象



print(page1.images)
print(page2.images)

# 直接提取某一页中的图片
# img = page2.images[0]
# ppoint = (img['x0'], img['top'], img['x1'], img['bottom'])
# page2.crop(ppoint).to_image(antialias=True, resolution=1080).save('test2.png')

# 整个页面全部提取为图片
# page1.to_image(antialias=True, resolution=1080).show()  # antialias=True抗锯齿, resolution=1080高清

ts = '''
 [水果，颜色，价格（美元）] 
[苹果，红色，1.20] 
[香蕉，黄色，0.50] 
[橙子，橙色，0.80] 
[草莓，红色，2.50] 
[蓝莓，蓝色，3.00] 
[猕猴桃，绿色，1.00] 
[芒果，橙色，1.50] 
[葡萄，紫色，2.00]
'''

td = [row.strip().split() for row in ts.strip().split('\n') ]
print(td)

translated_df = pd.DataFrame(td[1:], columns=td[0])

print(translated_df)

import re

print(type(re.split(',|，', '苹果，红色，1.20')))