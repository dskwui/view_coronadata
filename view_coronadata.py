#

import streamlit as st
import pandas as pd
from datetime import date

st.title("新型コロナウイルス新規陽性者数")

df=pd.read_csv("newly_confirmed_cases_daily.csv")
df["Date"]=pd.to_datetime(df["Date"])
df=df.set_index("Date")

area_select=st.sidebar.multiselect("都道府県",df.columns, default="Kyoto")
day=st.sidebar.slider("期間",value=(date(2020,1,30),date(2023,5,8)),format="YYYY/M/D")

normdata=st.sidebar.toggle("正規化")


disp=df.loc[day[0]:day[1],:]

if normdata:
    disp=disp/disp.max()
st.line_chart(disp,y=area_select)

st.write("[厚生労働省オープンデータ](https://www.mhlw.go.jp/stf/covid-19/open-data.html)より")
