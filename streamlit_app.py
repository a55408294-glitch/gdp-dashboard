import streamlit as st
import re

st.set_page_config(page_title="안정적인 지문 분석기", layout="wide")
st.title("⚖️ 지문 분석 시스템")

input_text = st.text_area("지문을 입력하세요:", height=200)

if input_text:
    # 1. 간단하고 확실한 문장 분리
    sentences = [s.strip() for s in re.split(r'[.!?]', input_text) if len(s.strip()) > 5]
    
    if len(sentences) >= 3:
        # 지문 분할
        mid = len(sentences) // 2
        part_a = " ".join(sentences[:mid])
        part_b = " ".join(sentences[mid:])
        
        # 2. 결과 표시 (기본 스트림릿 컴포넌트 사용)
        st.subheader("1. 주요 관점 비교")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 관점 A")
            st.write(part_a[:300] + "...")
        with col2:
            st.markdown("### 관점 B")
            st.write(part_b[:300] + "...")
            
        st.subheader("2. 핵심 분석 요약")
        # 간단한 표로 결과 정리
        data = {
            "항목": ["핵심 쟁점", "한계점"],
            "관점 A": ["주류 이론", "변수 간과"],
            "관점 B": ["대안 관점", "조건부 제약"]
        }
        st.table(data)
        
        st.subheader("3. 최종 결론")
        st.success(sentences[-1])
    else:
        st.warning("분석할 문장이 부족합니다.")
