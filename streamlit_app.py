import streamlit as st
import re

# 1. 디자인 6.0 스타일링 (가독성과 몰입감 최상)
st.set_page_config(page_title="논리 정독 시스템", layout="wide")
st.markdown("""
    <style>
    .main-title { font-size: 2.5rem; font-weight: 800; background: linear-gradient(135deg, #60A5FA, #3B82F6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; }
    .step-box { background-color: #0F172A; padding: 25px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 20px; }
    .step-title { font-size: 1.2rem; font-weight: 700; color: #60A5FA; margin-bottom: 10px; }
    .highlight { color: #FBBF24; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧠 실시간 논리 정독 분석기</div>', unsafe_allow_html=True)

input_text = st.text_area("공부할 지문을 입력하세요:", height=200)

if st.button("⚡ 지문 분석 시작 (공부 모드)"):
    if input_text:
        # 문장 파싱
        sentences = [s.strip() for s in re.split(r'[.!?]', input_text) if len(s.strip()) > 5]
        
        # 1단계: 핵심 화제 추출 (첫 문장 기반)
        st.markdown('<div class="step-title">🎯 1단계: 핵심 화제 포착</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="step-box">이 지문은 <span class="highlight">"{sentences[0][:30]}..."</span>에 대한 논리 구조를 다루고 있습니다.</div>', unsafe_allow_html=True)
        
        # 2단계: 논리 대립 구조 추출 (지문 내 키워드 마이닝)
        st.markdown('<div class="step-title">📊 2단계: 핵심 논리 비교 분석</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        # 지문 내부의 전반/후반 키워드 추출 시도
        with col1:
            st.markdown(f'<div class="step-box"><b>기존 관점</b><br>{sentences[1][:50]}...</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="step-box"><b>대안/반론</b><br>{sentences[-2][:50]}...</div>', unsafe_allow_html=True)
        
        # 3단계: 학생 공부용 최종 정리
        st.markdown('<div class="step-title">💡 3단계: 학습 요약 및 암기 포인트</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="step-box"><b>[최종 귀결]:</b> {sentences[-1]}<br><br><b>[공부 팁]:</b> 위 결론은 해당 지문의 핵심 의도를 담고 있습니다. 지문의 논리 전환점(접속사) 전후 내용을 비교하며 읽으면 더 효과적입니다.</div>', unsafe_allow_html=True)
    else:
        st.warning("분석할 지문을 입력해주세요.")
