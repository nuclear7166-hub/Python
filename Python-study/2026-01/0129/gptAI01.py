# 엑셀 파일에 있는 내용을 읽어서 화면에 출력하는 파이썬 코드를 작성해줘

import pandas as pd

# pip install openpyxl
df = pd.read_excel("around.xlsx")
print(pd.read_excel("around.xlsx"))
print(df.iloc[4])

# around.xlsx 파일의 5행을 출력하는 문장을 추가세요
