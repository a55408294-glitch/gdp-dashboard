import streamlit as st
import re

st.set_page_config(page_title="논리 정독 분석기", layout="wide")

# UI 스타일은 그대로 유지
st.markdown("""
    <style>
    .main-title { font-size: 2.5rem; font-weight: 800; color: #FFFFFF; text-align: center; }
    .panel { background-color: #0F172A; padding: 25px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 20px; }
    .title-box { font-size: 1.2rem; font-weight: 700; color: #60A5FA; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧠 실시간 지문 논리 정독 시스템</div>', unsafe_allow_html=True)
input_text = st.text_area("공부할 지문을 입력하세요:", height=200)

if st.button("⚡ 지문 실시간 분석 시작"):
    if not input_text.strip():
        st.warning("분석할 지문을 입력해주세요.")
    else:
        # 1. 지문 파싱: 문장 단위로 쪼개기
        sentences = [s.strip() for s in re.split(r'[.!?]', input_text) if len(s.strip()) > 5]
        
        # 2. 핵심 알고리즘: '그러나', '반면' 등 대립 접속사 찾기 (없으면 중간 분할)
        pivot = len(sentences) // 2
        for i, sent in enumerate(sentences):
            if any(w in sent for w in ["그러나", "반면", "하지만", "그럼에도"]):
                pivot = i
                break
        
        # 3. 데이터 추출 (하드코딩된 단어 없이 문장 슬라이싱)
        part_a = sentences[:pivot]
        part_b = sentences[pivot:]
        
        # [영역 1] 분석 결과 렌더링
        st.markdown('<div class="title-box">🎯 1단계: 논리 구조 파악</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel">이 지문은 <b>{sentences[0][:20]}...</b> 으로 시작하여, <b>{sentences[pivot][:20]}...</b> 시점을 전환점으로 삼고 있습니다.</div>', unsafe_allow_html=True)
        
        # [영역 2] 비교 매트릭스
        st.markdown('<div class="title-box">📊 2단계: 핵심 대립 관계</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<div class="panel"><b>기존 원칙:</b><br>{" ".join(part_a[:2])[:100]}...</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="panel"><b>대안적 관점:</b><br>{" ".join(part_b[:2])[:100]}...</div>', unsafe_allow_html=True)
            
        # [영역 3] 학생용 독해 전략 (마지막 문장 분석)
        st.markdown('<div class="title-box">💡 3단계: 정독 전략 및 요약</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel"><b>핵심 귀결:</b> {sentences[-1]}<br><br><b>전략:</b> 위 지문은 <b>{sentences[0][:15]}</b>의 한계를 지적하고 <b>{sentences[-2][:15]}</b>로 나아가는 변증법적 구조입니다. 전환점을 중심으로 문맥을 파악하세요.</div>', unsafe_allow_html=True)
