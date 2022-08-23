import pandas as pd

성별시리즈 = pd.Series({
    '102365':'남',
    '206587':'여',
    '185365':'',
    '589655':'남'
})

이름시리즈 = pd.Series({
    '102365':'장홍기',
    '206587':'김진주',
    '185365':'이범',
    '589655':'김진주'
})

딕_회원={'성별':성별시리즈,'이름':이름시리즈}
헬스장회원 = pd.DataFrame(딕_회원)

헬스장회원2=pd.DataFrame({
    '회원번호':['102365','206587','185365','589655'],
    '성별':['남','여','','남'],
    '이름':['장홍기','김진주','이범','김진주']
})

헬스장회원3=헬스장회원2.set_index('회원번호')


#헬스장회원.loc['185365']['이름']='이범수'
헬스장회원2.loc[0]['성별']='여'
헬스장회원3.loc['206587']['성별']='남'
#헬스장회원.iloc[2][1]='이수'

print(헬스장회원)
print(헬스장회원2)
print(헬스장회원3)

헬스장회원.to_csv('회원명부.csv')