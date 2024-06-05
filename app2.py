import os
import pandas as pd
import streamlit as st
import plotly.express as px
import chardet

# Streamlit 앱 제목
st.title("Traffic Accident Statistics")

# 현재 디렉토리에서 CSV 파일 목록 가져오기
csv_files = [f for f in os.listdir('./') if f.endswith('.csv')]
print(os.curdir)
# CSV 파일 선택
selected_file = st.selectbox("Select a CSV file", csv_files)

print(selected_file)
# 감지된 인코딩을 사용하여 파일 읽기
df = pd.read_csv('./'+selected_file, encoding='cp949')
print(df.head())

# 열 이름을 리스트로 변환
columns = df.columns.tolist()
print(columns)



# 파일을 성공적으로 읽은 경우에만 열 이름을 리스트로 변환
if df is not None:
    columns = df.columns.tolist()
    print(columns)
else:
    columns = []

# X축 컬럼 선택
x_column = st.selectbox("Select X-axis column", columns)
# Y축 컬럼 선택
y_column = st.selectbox("Select Y-axis column", columns)
# 차트 타입 선택
chart_type = st.selectbox("Select chart type", ["bar", "line", "pie"])
try:
    
    df = df[df['발생지시도'] == '서울']
    # 선택된 컬럼과 차트 타입이 있는 경우
    if x_column and y_column and chart_type:
        data = df[[x_column, y_column]].groupby(x_column).sum().reset_index()
except:
    print("터진다")

    # # Plotly를 사용하여 차트 생성
    # if chart_type == 'bar':
    #     fig = px.bar(data, x=x_column, y=y_column, title=f'{chart_type.capitalize()} Chart')
    # elif chart_type == 'line':
    #     fig = px.line(data, x=x_column, y=y_column, title=f'{chart_type.capitalize()} Chart')
    # elif chart_type == 'pie':
    #     fig = px.pie(data, names=x_column, values=y_column, title=f'{chart_type.capitalize()} Chart')
    #
    # # 차트 표시
    # st.plotly_chart(fig, use_container_width=True)
