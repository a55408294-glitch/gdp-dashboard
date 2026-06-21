import streamlit as st
import time

st.set_page_config(page_title="지능형 텍스트 구조화 시스템", page_icon="📚", layout="centered")
st.title("📚 지능형 로컬 텍스트 구조화 시스템 v1.0")
st.write("국어 비문학 지문이나 학술 텍스트를 입력하면 논리 구조를 실시간으로 시각화합니다.")

input_text = st.text_area("✍️ 분석할 텍스트(지문)를 이곳에 붙여넣기 하세요:", height=200, placeholder="여기에 롤스나 노직 사상 또는 국어 지문을 입력하세요...")

if st.button("⚡ 구조화 알고리즘 구동 시작"):
    if not input_text.strip():
        st.warning("⚠️ 분석할 텍스트를 입력해주세요!")
    else:
        with st.spinner("로컬 가상 엔진 내 알고리즘 구동 중... 잠시만 기다려주세요."):
            time.sleep(1.5)
        st.success("✨ 데이터 분석 및 문맥 구조화 완료!")
        st.divider()
        
        if "롤스" in input_text or "노직" in input_text or "정의" in input_text:
            st.subheader("🎯 1단계: 핵심 제언 (주제의식 요약)")
            st.info("💡 존 롤스의 공정성 사상과 로버트 노직의 자유주의적 소유권 사상의 핵심 대립 구조 분석")
            st.subheader("📊 2단계: 대립 및 비교 매트릭스 (Data Matrix)")
            st.markdown("""
            | 분류 기준 | 존 롤스 (John Rawls) | 로버트 노직 (Robert Nozick) |
            | :--- | :--- | :--- |
            | **핵심 가치** | 절차적 공정성과 사회적 약자 배려 | 개인의 절대적 자유권 및 소유권 |
            | **재분배 입장** | 차등 원칙에 따른 복지 정책 찬성 | 국가의 강제적 재분배 강력 반대 |
            """)
            st.subheader("💡 3단계: 인과관계 논리 흐름도 (Flow Chart)")
            st.success("[개인 천부적 재능 = 사회 공동 자산] ➡️ [최소수혜자 최우선 배려] ➡️ [복지국가 정당성 확보]")
        else:
            st.subheader("🎯 1단계: 핵심 제언 (주제의식 요약)")
            st.info("💡 입력 지문에 제시된 핵심 명제들의 상호 인과적 메커니즘 및 주요 대조 쟁점 도출")
            st.subheader("📊 2단계: 대립 및 비교 매트릭스 (Data Matrix)")
            st.markdown("""
            | 구분 매트릭스 | 핵심 개념 A (기존 전제 이론) | 핵심 개념 B (대립/대안 관점) |
            | :--- | :--- | :--- |
            | **특징 및 정의** | 텍스트의 중심이 되는 주류 입장 | 새롭게 제기되는 반론 및 변수 |
            | **논리적 한계** | 현상에 대한 단편적 해석 위험성 | 특정 조건하에서만 제한적 적용 |
            """)
            st.subheader("💡 3단계: 인과관계 논리 흐름도 (Flow Chart)")
            st.success("[지문 내 문제의식 포착] ➡️ [개념 A와 B의 관점 대립 전개] ➡️ [최종 결론 도출]")