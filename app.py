import plotly.express as px
import plotly
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 한글 안깨지게 하는 코드 
plt.rc('font', family='Malgun Gothic')

#plt.figure(figsize=(12,8))

money = pd.read_csv("c:\\9.12\\money_data7.csv")

# 년도 선택 박스 넣기
import streamlit as st

option = st.selectbox(
    'How would you like to choice year ?',
    ('2020', '2021', '2022'))

option2 = int(option)

st.write('You selected:', option)

money = money[:] [money['A_YEAR']== option2]

fig, ax = plt.subplots(2,2, figsize=(12,8))

plt.subplot(221)
plt.plot(  list( money['A_MONTH'] ), list( money['A_RATE'] ), color='red' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('미국금리')


plt.subplot(222)
plt.plot(  list( money['A_MONTH'] ), list( money['K_RATE'] ), color='blue' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('한국금리')

plt.subplot(223)
plt.plot(  list( money['A_MONTH'] ), list( money['KOSPI'] ), color='green' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('코스피 지수')

plt.subplot(224)
plt.plot(  list( money['A_MONTH'] ), list( money['HOUSE_PRICE'] ), color='yellow' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('집값')

st.pyplot(fig)