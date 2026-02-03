import streamlit as st

st.title("🍎 건강식단매니저")
st.write("간단한 칼로리 계산기 예제입니다.")

food_name = st.text_input("식품 이름", "사과")
calories = st.number_input("100g당 칼로리(kcal)", value=52)
weight = st.number_input("먹은 양(g)", value=200)

if st.button("계산하기"):
    total = (calories / 100) * weight
    st.success(f"{food_name} {weight}g의 총 칼로리는 {total:.2f} kcal입니다.")