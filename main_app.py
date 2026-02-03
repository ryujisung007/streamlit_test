import streamlit as st
import pandas as pd  # 데이터 표를 다루기 위한 필수 라이브러리

# 페이지 설정
st.set_page_config(page_title="식품 배합비 시뮬레이터", layout="wide")

st.title("🥗 식품 개발 데이터 관리 시스템")

# --- 입력 섹션 ---
st.subheader("1. 성분 입력")
col1, col2, col3 = st.columns(3)

with col1:
    ing_name = st.text_input("원료명", "정제수")
with col2:
    ing_ratio = st.number_input("배합비(%)", value=0.0, format="%.2f")
with col3:
    ing_purpose = st.text_input("사용 목적", "용매")

# --- 데이터 저장 (세션 상태 활용) ---
if 'ingredient_list' not in st.session_state:
    st.session_state.ingredient_list = []

if st.button("배합비 추가"):
    st.session_state.ingredient_list.append({
        "원료명": ing_name,
        "배합비(%)": ing_ratio,
        "사용 목적": ing_purpose
    })
    st.success(f"{ing_name} 추가 완료!")

# --- 표 출력 섹션 (핵심 수정 부분) ---
st.divider()
st.subheader("2. 배합비 표준 리스트")

if st.session_state.ingredient_list:
    # 리스트 데이터를 표(DataFrame)로 변환
    df = pd.DataFrame(st.session_state.ingredient_list)
    
    # 1. 인터랙티브 표 (정렬, 검색 가능)
    st.write("📊 데이터프레임 형식 (조작 가능)")
    st.dataframe(df, use_container_width=True)
    
    # 2. 정적 표 (보고서용)
    st.write("📋 일반 표 형식 (출력용)")
    st.table(df)

    # 합계 계산 및 표시
    total_ratio = df["배합비(%)"].sum()
    st.info(f"현재 총 배합비 합계: {total_ratio:.2f} %")
    
    if st.button("초기화"):
        st.session_state.ingredient_list = []
        st.rerun()
else:
    st.info("추가된 원료가 없습니다. 상단에서 원료를 입력하고 '배합비 추가'를 눌러주세요.")