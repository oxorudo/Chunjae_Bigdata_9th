import streamlit as st
import pandas as pd
import altair as alt

#  streamlit 앱 설정
st.title('사용자 데이터 시각화 대시보드')
st.sidebar.title('필터')

# 데이터
data = {
    'age_category' : ['10대', '20대', '30대', '40대', '50대', '60대', '70대', '80대', '90대', '100대'],
    'sex' : ['M', 'F', 'F' ,'F', 'F', 'F', 'M', 'M', 'F', 'M'],
    'city' : ['서울', '부산', '서울', '대구', '수원', '대구', '부산', '서울', '부산', '수원']
}

df = pd.DataFrame(data)


# 나이대 필터
age_category = st.sidebar.multiselect('나이대 선택 : ', df['age_category'].unique(), default=df['age_category'].unique())
filtered_data = df[df['age_category'].isin(age_category)]

# 1. 나이대별 인원수 시각화
age_chart = (
    alt.Chart(filtered_data)
    .mark_bar()
    .encode(
        x=alt.X('age_category', sort='-y', title='나이대'),
        y=alt.Y('count()', title='인원수'),
        color = 'age_category'
    )
    .properties(title='나이대별 인원 분포')

)
# 2. 성별 인원수 시각화
gender_chart = (
    alt.Chart(filtered_data)
    .mark_bar()
    .encode(
        x=alt.X('sex', title='성별'),
        y=alt.Y('count()', title='인원수'),
        color = 'sex'
    )
    .properties(title='성별 분포')

)

# 3. 지역별 인원수 시각화
city_chart = (
    alt.Chart(filtered_data)
    .mark_bar()
    .encode(
        x=alt.X('city', sort='-y', title='지역'),
        y=alt.Y('count()', title='인원수'),
        color = 'city'
    )
    .properties(title='지역별 인원 분포')

)

# 시각화 결과 출력
st.altair_chart(age_chart, use_container_width=True)
st.altair_chart(gender_chart, use_container_width=True)
st.altair_chart(city_chart, use_container_width=True)
