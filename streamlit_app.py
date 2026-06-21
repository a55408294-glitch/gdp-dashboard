import streamlit as st
import re
from collections import Counter

# 1. 디자인 스타일 (가독성 최우선)
st.set_page_config(page_title="논리 정독 시스템", layout="wide")
st.markdown("""
    <style>
    .main-title { font-size: 2.5rem; font-weight: 800; color: #FFFFFF; text-align: center; margin-bottom: 30px; }
    .box { background-color: #1E293B; padding: 20px; border-radius: 10px; border: 1px solid #334155; margin-bottom: 15px; color: #E2E8F0; }
    .header { font-size: 1.3rem; font-weight: bold; color: #60A5FA; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧠 논리 정독 분석기</div>', unsafe_allow_html=True)

# 2. 지문 입력
input_text = st.text_area("공부할 지문을 붙여넣고 아래 버튼을 누르세요:", height=200)

if st.button("⚡ 분석 시작"):
    if not input_text.strip():
        st.warning("지문을 입력해주세요.")
    else:
        # 3. 실시간 분석 로직 (사전 단어 정의 없음)
        sentences = [s.strip() for s in re.split(r'[.!?]', input_text) if len(s.strip()) > 5]
        
        # 키워드 자동 추출
        words = [w for w in re.findall(r'\w{2,}', input_text) if w not in ["이러한", "있는", "하는", "대한"]]
        keys = [pair[0] for pair in Counter(words).most_common(5)]
        
        concept_a = keys[0] if len(keys) > 0 else "전반부 전제"
        concept_b = keys[1] if len(keys) > 1 else "후반부 대안"

        # 4. 화면 렌더링
        st.markdown('<div class="header">🎯 1단계: 핵심 논리 추출</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="box">지문의 핵심은 <b>{concept_a}</b>와 <b>{concept_b}</b>의 관계를 설명하는 것입니다.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="header">📊 2단계: 구조 분석</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        c1.markdown(f'<div class="box"><b>원칙/전제:</b><br>{sentences[0]}</div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="box"><b>전환/대안:</b><br>{next((s for s in sentences if "그러나" in s or "반면" in s), sentences[-2])}</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="header">💡 3단계: 정독 가이드</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="box"><b>귀결:</b> {sentences[-1]}<br><br><b>공부 팁:</b> <b>{concept_a}</b>를 중심으로 지문이 어떻게 전개되는지 흐름을 타면서, <b>{concept_b}</b>가 원칙을 어떻게 보완하는지 파악하세요.</div>', unsafe_allow_html=True)
