import streamlit as st
import re

st.set_page_config(page_title="정직한 분석기", layout="wide")
st.title("지문 분석 결과")

input_text = st.text_area("지문을 입력하세요:", height=200)

if input_text:
    # 1. 문장 분리 (단순 점/물음표 기준)
    sentences = [s.strip() for s in re.split(r'[.!?]', input_text) if len(s.strip()) > 5]
    
    if len(sentences) > 3:
        # 2. 강제 분할 (앞 1/3, 뒤 1/3) - 분석 루프 없이 바로 슬라이싱
        part_a = sentences[:len(sentences)//2]
        part_b = sentences[len(sentences)//2:]
        
        st.subheader("1. 주요 관점")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**관점 A:**", " ".join(part_a[:2]))
        with col2:
            st.write("**관점 B:**", " ".join(part_b[:2]))
            
        st.subheader("2. 요약 및 결론")
        st.write("**결론:**", sentences[-1])
    else:
        st.write("지문이 너무 짧습니다. 조금 더 긴 지문을 넣어주세요.")
