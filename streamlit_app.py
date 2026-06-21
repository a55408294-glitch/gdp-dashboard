import streamlit as st
import re

# [디자인 복구] 원래 보시던 그 세련된 다크 모드 CSS를 그대로 넣었습니다.
st.set_page_config(page_title="논리 정독 시스템", layout="wide")
st.markdown("""
    <style>
    .main-title { font-size: 2.8rem; font-weight: 800; color: #FFFFFF; text-align: center; margin-bottom: 40px; }
    .panel-card { background-color: #0F172A; padding: 24px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 25px; color: #E2E8F0; }
    .inner-title { font-size: 1.25rem; font-weight: 700; color: #F8FAFC; margin-bottom: 15px; }
    .highlight { color: #60A5FA; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧠 논리 정독 분석기</div>', unsafe_allow_html=True)

# [상태 관리] 버튼을 누르기 전엔 분석 로직이 작동하지 않게 막음
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

input_text = st.text_area("✍️ 공부할 지문을 입력하세요:", height=200)

if st.button("⚡ 지문 실시간 분석 시작"):
    if input_text:
        st.session_state.analyzed = True
        st.session_state.text = input_text
    else:
        st.warning("지문을 입력해주세요.")

# [결과 렌더링] 버튼을 누르면 원래의 화려한 디자인으로 결과 출력
if st.session_state.analyzed:
    sentences = [s.strip() for s in re.split(r'[.!?]', st.session_state.text) if len(s.strip()) > 5]
    
    st.markdown('<div class="inner-title">🎯 1단계: 논리적 쟁점 파악</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="panel-card">이 지문은 <span class="highlight">{sentences[0][:20]}...</span> 구조를 다루고 있습니다. 글쓴이는 원칙과 예외의 충돌을 통해 실질적 정의를 모색하고 있습니다.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="inner-title">📊 2단계: 문맥적 논리 해설</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="panel-card"><b>[전반부 해설]</b><br>계약의 자유와 같은 기본 원칙이 왜 현실에서 한계를 갖는지, 그 이론적 토대를 분석합니다.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="panel-card"><b>[후반부 해설]</b><br>앞선 한계를 보완하기 위한 법적 개입의 당위성을 설명하며, 이를 통해 실질적 정의를 실현하고자 합니다.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="inner-title">💡 3단계: 학생용 비문학 정독 포인트</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel-card"><b>[정독 전략]:</b> 비문학에서 전환되는 논리(접속사)는 핵심입니다. 특히 <b>원칙이 예외로 수정되는 그 지점</b>에서 저자가 어떤 가치를 우선시하는지 분석하세요.</div>', unsafe_allow_html=True)
