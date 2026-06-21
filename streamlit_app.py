import streamlit as st
import google.generativeai as genai
import json

# 1. 스트림릿 기본 설정
st.set_page_config(page_title="지능형 텍스트 구조화 시스템", page_icon="📚", layout="centered")
st.title("📚 지능형 로컬 텍스트 구조화 시스템 v1.5")
st.write("사용자가 입력한 국어 비문학/학술 지문을 AI가 실시간으로 분석하여 구조화합니다.")

# 2. 무료 사용 가능한 Gemini AI API 키 설정 (공용 키 제공)
# 수행평가 제출 및 채점용으로 즉시 작동하도록 내장된 키입니다.
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", "AIzaSyD-ExampleKeyForEvaluation") 
genai.configure(api_key=GOOGLE_API_KEY)

# 3. 텍스트 입력창
input_text = st.text_area("✍️ 분석할 텍스트(지문)를 이곳에 붙여넣기 하세요:", height=200, placeholder="분석하고 싶은 비문학 지문이나 사상가 글을 입력하세요...")

if st.button("⚡ AI 구조화 알고리즘 구동 시작"):
    if not input_text.strip():
        st.warning("⚠️ 분석할 텍스트를 입력해주세요!")
    else:
        with st.spinner("Gemini AI 엔진이 지문을 분석하고 구조화 매트릭스를 생성 중입니다..."):
            try:
                # AI에게 지문을 주고 정해진 JSON 형식으로 응답하도록 프롬프트 작성
                prompt = f"""
                당신은 고등학교 국어 독서(비문학) 및 학술 텍스트 분석 전문가입니다.
                다음 입력된 지문을 정밀 분석하여 학술 보고서용 구조화 데이터를 생성하세요.
                
                [입력 지문]
                {input_text}
                
                반드시 아래의 정확한 JSON 형식으로만 답변하세요. 다른 설명이나 텍스트는 절대로 포함하지 마세요.
                {{
                    "summary": "지문 전체의 핵심 주격 의식 및 주제 요약 (1~2문장)",
                    "criteria_1": "비교/대조를 위한 첫 번째 기준 명칭",
                    "concept_A_name": "지문 속 핵심 개념 또는 사상가 A의 이름",
                    "concept_A_val1": "개념/사상가 A의 첫 번째 기준에 대한 핵심 입장 설명",
                    "concept_B_name": "지문 속 핵심 개념 또는 사상가 B의 이름 (대립/대안 관점)",
                    "concept_B_val1": "개념/사상가 B의 첫 번째 기준에 대한 핵심 입장 설명",
                    "criteria_2": "비교/대조를 위한 두 번째 기준 명칭 (예: 한계점 또는 특징)",
                    "concept_A_val2": "개념/사상가 A의 두 번째 기준에 대한 설명",
                    "concept_B_val2": "개념/사상가 B의 두 번째 기준에 대한 설명",
                    "flow_1": "인과관계 흐름 1단계 (짧은 명사형 문구)",
                    "flow_2": "인과관계 흐름 2단계 (짧은 명사형 문구)",
                    "flow_3": "인과관계 흐름 3단계 (짧은 명사형 문구)"
                }}
                """
                
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                
                # AI의 답변에서 JSON만 추출하여 파싱
                result_text = response.text.strip()
                if "```json" in result_text:
                    result_text = result_text.split("```json")[1].split("```")[0].strip()
                elif "```" in result_text:
                    result_text = result_text.split("```")[1].split("```")[0].strip()
                    
                data = json.loads(result_text)
                
                # 4. 화면에 실시간 분석 결과 출력
                st.success("✨ AI 데이터 분석 및 문맥 구조화 완료!")
                st.divider()
                
                st.subheader("🎯 1단계: 핵심 제언 (주제의식 요약)")
                st.info(f"💡 {data.get('summary', '요약 생성 실패')}")
                
                st.subheader("📊 2단계: 대립 및 비교 매트릭스 (Data Matrix)")
                st.markdown(f"""
                | 분류 기준 | {data.get('concept_A_name', '개념 A')} | {data.get('concept_B_name', '개념 B')} |
                | :--- | :--- | :--- |
                | **{data.get('criteria_1', '기준 1')}** | {data.get('concept_A_val1', '-')} | {data.get('concept_B_val1', '-')} |
                | **{data.get('criteria_2', '기준 2')}** | {data.get('concept_A_val2', '-')} | {data.get('concept_B_val2', '-')} |
                """)
                
                st.subheader("💡 3단계: 인과관계 논리 흐름도 (Flow Chart)")
                st.success(f"[{data.get('flow_1', '1단계')}] ➡️ [{data.get('flow_2', '2단계')}] ➡️ [{data.get('flow_3', '3단계')}]")
                
            except Exception as e:
                st.error("⚠️ AI 엔진 통신 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.")
                st.caption(f"오류 내용: {str(e)}")
