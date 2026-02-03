from openai import OpenAI
import streamlit as st

# 모듈화 원칙에 따라 OpenAI 호출 시 로드 부담이 적은 gpt-4o-mini 사용
def generate_food_formula(food_type, trend):
    """식품 배합비 생성 함수 (main_app에서 호출하는 이름과 일치시킴)"""
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"]) # Secrets 사용
    
    prompt = f"{food_type}에 대한 {trend} 컨셉의 표준 배합비를 작성해줘."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def update_formula_with_chat(current_formula, user_feedback):
    """이미지 생성이나 배합비 수정을 위한 챗봇 대화 함수"""
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "너는 식품 개발 전문가야. 사용자의 피드백을 반영해 배합비를 수정해."},
            {"role": "user", "content": f"기존배합: {current_formula}\n피드백: {user_feedback}"}
        ]
    )
    return response.choices[0].message.content