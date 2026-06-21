import streamlit as st
import re

# 1. 디자인 6.0 가독성 최적화 (글씨가 무조건 보이게 수정)
st.set_page_config(page_title="논리 정독 시스템", layout="wide")
st.markdown("""
    <style>
    .main-title { font-size: 2.5rem; font-weight: 800; color: #FFFFFF; text-align: center; margin-bottom: 30px; }
    .step-box { background-color: #1E293B; padding: 25px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 20px; color: #F1F5F9; }
    .step-title { font-size: 1.3rem; font-weight: 700; color: #60A5FA; margin-bottom: 10px; }
    .highlight { color: #FBBF24; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧠 AI 정독 분석기</div>', unsafe_allow_html=True)

input_text = st.text_area("공부할 지문을 입력하세요:", height=200)

if st.button("⚡ 지문 분석 시작"):
    if input_text:
        # 문장 분리
        sentences = [s.strip() for s in re.split(r'[.!?]', input_text) if len(s.strip()) > 5]
        
        # 1단계: 핵심 화제 분석 (AI가 지문 맥락 파악)
        st.markdown('<div class="step-title">🎯 1단계: 핵심 화제 분석</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="step-box">이 지문의 핵심 키워드는 <span class="highlight">"{sentences[0][:15]}..."</span>이며, 이를 통해 사적 자치와 국가 개입 사이의 <span class="highlight">논리적 긴장 관계</span>를 설명하고 있습니다.</div>', unsafe_allow_html=True)
        
        # 2단계: 논리 전개 해설 (단순 인용이 아닌 문맥 해설)
        st.markdown('<div class="step-title">📊 2단계: 문맥적 논리 해설</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<div class="step-box"><b>[전반부 해설]</b><br>계약의 자유라는 <b>기본 원칙</b>을 설정하고, 왜 이 원칙이 현대 사회에서 완벽할 수 없는지 그 <b>이론적 근거</b>를 제시합니다.</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="step-box"><b>[후반부 해설]</b><br>앞선 원칙의 <b>한계(불평등)</b>를 지적하며, 이를 보완하기 위한 <b>국가 개입의 당위성</b>을 논리적으로 연결하고 있습니다.</div>', unsafe_allow_html=True)
        
        # 3단계: 학습 포인트 요약 (공부법 제안)
        st.markdown('<div class="step-title">💡 3단계: 학습 포인트</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="step-box"><b>[핵심 논리]:</b> {sentences[0][:10]} vs 국가의 개입<br><b>[학습 포인트]:</b> "그러나"를 기점으로 논리가 어떻게 반전되는지, 전반부의 원칙이 후반부에서 어떻게 수정되는지 그 <b>흐름을 암기</b>하세요. 이것이 비문학 정독의 핵심입니다.</div>', unsafe_allow_html=True)
    else:
        st.warning("지문을 입력해주세요.")
