import pandas as pd

df = pd.read_excel(r'C:\Users\user\Desktop\data.xlsx') #임시로 엑셀에서 데이터 받아옴
backup_df = df
print(df)
print(" 콘센트 사용 가능 유무 (1:가능 , 2: 불가능)")
con = input()
print(" pc 사용 가능 유무 (1:가능 , 2: 불가능)")
com = input()