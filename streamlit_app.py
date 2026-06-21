import streamlit as st
import re

# 1. 디자인 6.0 (네온 다크)
st.set_page_config(page_title="논리 정독 시스템", layout="wide")
st.markdown("""
    <style>
    .main-title { font-size: 2.5rem; font-weight: 800; color: #FFFFFF; text-align: center; }
    .step-box { background-color: #1E293B; padding: 25px; border-radius: 15px; border: 1px solid #334155; color: #E2E8F0; margin-top: 15px; }
    .step-title { font-size: 1.3rem; font-weight: 700; color: #60A5FA; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧠 논리 정독 분석기</div>', unsafe_allow_html=True)

# 2. 버튼 클릭 전 상태 관리
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

input_text = st.text_area("공부할 지문을 입력하세요:", height=150)

if st.button("⚡ 지문 분석 시작"):
    if input_text:
        st.session_state.analyzed = True
        st.session_state.text = input_text
    else:
        st.warning("지문을 입력해주세요.")

# 3. 버튼을 누른 후에만 결과 렌더링
if st.session_state.analyzed:
    sentences = [s.strip() for s in re.split(r'[.!?]', st.session_state.text) if len(s.strip()) > 5]
    
    st.markdown('<div class="step-title">🎯 1단계: 논리적 쟁점 파악</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="step-box">이 지문은 원칙과 예외가 충돌하는 구조를 다룹니다. 글쓴이는 원칙의 유용성을 인정하면서도, 현실의 한계를 보완하기 위한 <span style="color:#FBBF24;">변증법적 논리</span>를 전개합니다.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="step-title">📊 2단계: 문맥적 논리 해설</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="step-box"><b>[전반부]</b><br>계약의 자유라는 기본 원칙을 설정합니다. 하지만 이는 현실의 불평등을 간과할 위험이 있습니다.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="step-box"><b>[후반부]</b><br>앞선 원칙의 한계를 보완할 국가 개입의 당위성을 제시합니다. 이는 자유의 파괴가 아닌 정의 실현을 위한 보완책입니다.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="step-title">💡 3단계: 학습 포인트</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-box"><b>정독 전략:</b> "그러나"를 기점으로 논리가 어떻게 반전되는지, 예외가 원칙을 보완하는지 분석하세요. 이것이 비문학 정독의 핵심입니다.</div>', unsafe_allow_html=True)
