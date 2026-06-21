import streamlit as st
import re

# 1. 디자인 6.0 (네온 다크 테마) - 고정 스타일
st.set_page_config(page_title="논리 정독 시스템", layout="wide")
st.markdown("""
    <style>
    .main-title { font-size: 2.8rem; font-weight: 800; color: #FFFFFF; text-align: center; margin-bottom: 40px; }
    .step-box { background-color: #1E293B; padding: 25px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 25px; color: #E2E8F0; }
    .step-title { font-size: 1.4rem; font-weight: 700; color: #60A5FA; margin-bottom: 15px; }
    .highlight { color: #FBBF24; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧠 논리 정독 분석기</div>', unsafe_allow_html=True)

input_text = st.text_area("공부할 지문을 입력하세요:", height=200)

if st.button("⚡ 지문 분석 시작"):
    if input_text:
        # 문장 분리
        sentences = [s.strip() for s in re.split(r'[.!?]', input_text) if len(s.strip()) > 5]
        
        # 1단계: 핵심 화제 분석 (문장 복사 X, 맥락 파악 O)
        st.markdown('<div class="step-title">🎯 1단계: 논리적 쟁점 파악</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="step-box">이 지문은 <span class="highlight">원칙(사적 자치)</span>과 <span class="highlight">예외(국가 개입)</span>가 충돌하는 구조를 다룹니다. 글쓴이는 원칙의 유용성을 인정하면서도, 현실의 불평등을 해결하기 위해 예외적 장치가 필요하다는 <span class="highlight">논리적 변증법</span>을 전개하고 있습니다.</div>', unsafe_allow_html=True)
        
        # 2단계: 논리 전개 해설 (문장 복사 X, 분석 O)
        st.markdown('<div class="step-title">📊 2단계: 문맥적 논리 해설</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="step-box"><b>[전반부 해설]</b><br>계약의 자유가 왜 중요한지 근거를 댑니다. 하지만 이는 <b>"당사자 간 지위가 평등하다"</b>는 비현실적 전제 위에서만 완벽하게 작동한다는 점을 간파해야 합니다.</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="step-box"><b>[후반부 해설]</b><br>앞선 원칙의 한계를 지적하며 <b>"국가 개입"</b>이라는 대안을 제시합니다. 이는 자유의 훼손이 아니라 <b>실질적 정의</b>를 위한 보완책이라는 점이 논리적 핵심입니다.</div>', unsafe_allow_html=True)
        
        # 3단계: 학습 포인트 요약 (공부법)
        st.markdown('<div class="step-title">💡 3단계: 학생용 비문학 정독 포인트</div>', unsafe_allow_html=True)
        st.markdown('<div class="step-box"><b>[정독 전략]:</b> 비문학에서 <b>"그러나"</b>는 단순히 화제를 전환하는 게 아니라, <b>앞선 주장의 한계</b>를 드러내는 강력한 신호입니다. 이후에 제시되는 대안이 원칙을 완전히 파괴하는지, 아니면 보완하는지 그 <b>관계를 분석하며 읽는 습관</b>을 기르세요.</div>', unsafe_allow_html=True)
    else:
        st.warning("지문을 입력해주세요.")
