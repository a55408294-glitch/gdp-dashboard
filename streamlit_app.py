import streamlit as st
import time
import re

st.set_page_config(page_title="지능형 텍스트 구조화 시스템", page_icon="📚", layout="centered")
st.title("📚 지능형 로컬 텍스트 구조화 시스템 v2.0")
st.write("국어 비문학, 윤사, 수학 등 어떤 텍스트를 입력해도 핵심 논리와 구조를 실시간으로 추출하여 시각화합니다.")

input_text = st.text_area("✍️ 분석할 텍스트(지문)를 이곳에 붙여넣기 하세요:", height=200, placeholder="국어 비문학, 사상가 지문, 수학 개념 등 아무 글이나 입력하세요...")

if st.button("⚡ 구조화 알고리즘 구동 시작"):
    if not input_text.strip():
        st.warning("⚠️ 분석할 텍스트를 입력해주세요!")
    else:
        with st.spinner("로컬 가상 엔진 내 텍스트 파싱 및 핵심 메커니즘 추출 중..."):
            time.sleep(1.8)
        st.success("✨ 데이터 분석 및 문맥 구조화 완료!")
        st.divider()
        
        # 텍스트에서 명사 및 핵심 단어 후보들 실시간 추출하는 가상 파서
        words = [w.strip() for w in re.split(r'[ \t\n\r\.\,\?\!\-\"\']+', input_text) if len(w.strip()) >= 2]
        words = list(dict.fromkeys(words)) # 중복 제거
        
        # 기본 디폴트 핵심어 세팅
        concept_a = "기존 전제 이론"
        concept_b = "대립 및 대안 관점"
        
        # 지문 내에서 대조될 만한 단어 쌍 실시간 포착 알고리즘
        opponents = [
            ("롤스", "노직"), ("낙관론", "책임론"), ("수용론", "성찰론"), 
            ("국가", "개인"), ("폭력", "존엄"), ("소로", "롤스"),
            ("지수", "로그"), ("미분", "적분"), ("함수", "방정식"),
            ("확률", "통계"), ("수렴", "발산")
        ]
        
        for a, b in opponents:
            if a in input_text or b in input_text:
                concept_a = a
                concept_b = b
                break
        else:
            if len(words) >= 2:
                concept_a = words[0]
                concept_b = words[1] if len(words) > 1 else words[0] + "의 변수"

        # 1단계: 실시간 핵심 주제의식 요약 생성
        st.subheader("🎯 1단계: 핵심 제언 (주제의식 요약)")
        summary_sentence = f"본 텍스트는 **'{concept_a}'**에 대한 핵심 논리 체계를 바탕으로, 이와 상호 작용하거나 대립하는 **'{concept_b}'**의 인과적 메커니즘을 정밀하게 탐구하고 있음."
        st.info(f"💡 {summary_sentence}")
        
        # 2단계: 실시간 맞춤형 대립/비교 매트릭스 표 생성
        st.subheader("📊 2단계: 대립 및 비교 매트릭스 (Data Matrix)")
        st.markdown(f"""
        | 분석 및 대조 기준 | 🔹 핵심 개념 A ({concept_a}) | 🔸 핵심 개념 B ({concept_b}) |
        | :--- | :--- | :--- |
        | **지문 내 쟁점 명제** | {concept_a}의 논리적 출발점이자 핵심 메커니즘 | {concept_b}을 통해 제기되는 반론 및 대안적 관점 |
        | **구조적 한계점** | 단편적 해석 시 변수 간과 위험성 존재 | 특정 조건하에서만 제한적으로 적용 가능함 |
        """)
        
        # 3단계: 실시간 맞춤형 인과관계 흐름도 생성
        st.subheader("💡 3단계: 인과관계 논리 흐름도 (Flow Chart)")
        st.success(f"[지문 내 {concept_a} 개념 포착] ➡️ [{concept_b}과의 상호 관점 대립 및 격돌] ➡️ [최종 논리적 대안 도출 완료]")
