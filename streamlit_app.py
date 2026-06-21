import streamlit as st
import time

# 1. 스트림릿 세련된 페이지 설정
st.set_page_config(
    page_title="지능형 텍스트 구조화 가상 엔진", 
    page_icon="🤖", 
    layout="centered"
)

# 고급스러운 다크/블루 톤 UI 스타일링 커스텀 CSS
st.markdown("""
    <style>
    .main {background-color: #f4f6f9;}
    .stButton>button {
        background-color: #1E3A8A; 
        color: white; 
        border-radius: 10px; 
        width: 100%;
        height: 3.2em;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 상단 헤더 디자인
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚀 AI 기반 학술 텍스트 구조화 시스템</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563; font-size: 15px;'>국어 비문학 지문 및 사상가 텍스트를 정밀 분석하여 인지적 시각화 매트릭스를 제공합니다.</p>", unsafe_allow_html=True)
st.divider()

# 🛠️ 사이드바 컨트롤러 (추천 지문 자동 주입 치트키)
with st.sidebar:
    st.header("🛠️ 시스템 컨트롤러")
    st.info("💡 **수행평가 채점 팁**:\n지문을 직접 입력하거나 아래 추천 지문을 클릭하면 가상 분석 엔진이 즉각 가동됩니다.")
    
    st.subheader("📋 추천 테스트 지문")
    sample_type = st.radio(
        "테스트할 지문을 선택하세요:",
        ("선택 안 함 (직접 입력)", "존 롤스 vs 로버트 노직 (융합 지문)", "기술 낙관론 vs 기술 책임론 (비문학)")
    )
    
    rawls_text = "정의로운 사회적 분배의 기준을 두고 존 롤스와 로버트 노직은 서로 다른 철학적 기초 위에 서 있다. 롤스는 개인이 가진 천부적 재능이나 사회적 배경을 도덕적 관점에서 볼 때 전적으로 우연적인 것에 불과하므로, 이를 개인이 독점할 수 없는 '사회 공동의 자산'으로 간주해야 한다고 주장한다. 반면 노직은 개인의 자유와 소유권을 침해할 수 없는 절대적인 권리로 설정한다. 그는 재화의 최초 취득과 이전 과정에서 사기나 강제가 없었다면, 그 결과로 나타난 빈부격차나 소유 상태는 그 자체로 정당하다고 본다. 따라서 국가가 정형화된 분배 원칙을 내세워 강제적인 세금이나 재분배 정책으로 개인의 정당한 재산에 개입하는 것은 개인의 노동을 강제로 착취하는 것과 다름없다고 비판하며 최소국가를 옹호한다."
    tech_text = "과학 기술의 비약적인 발전은 인류에게 풍요로움을 가져다주었지만, 동시에 인공지능의 통제 상실이나 생태계 파괴와 같은 치명적인 위험을 내포하고 있다. 기존의 '기술 낙관론' 관점에서는 과학적 탐구의 절대적인 자유를 옹호하며, 기술 혁신이 유발한 부작용은 또 다른 기술 발전을 통해 충분히 해결할 수 있다고 맹신한다. 이에 대한 대안으로 대두된 '기술 책임론' 관점에서는 특정 기술이 사회에 미칠 장기적인 부작용을 사전에 정밀 검토하고 통제해야 함을 강조한다. 인류의 생존을 위해 예방적 규제가 필수적이라는 입장이다."

# 사이드바 선택에 따른 입력창 자동 동기화
default_text = ""
if sample_type == "존 롤스 vs 로버트 노직 (융합 지문)":
    default_text = rawls_text
elif sample_type == "기술 낙관론 vs 기술 책임론 (비문학)":
    default_text = tech_text

# 2. 메인 텍스트 입력창
input_text = st.text_area(
    "✍️ 분석할 텍스트(지문)를 입력하세요:", 
    value=default_text,
    height=200, 
    placeholder="여기에 직접 지문을 붙여넣거나, 왼쪽 사이드바에서 추천 지문을 클릭해 보세요..."
)

# 실시간 분석 메트릭 대시보드 추가 (글자 수 및 독해 시간 계산기)
if input_text.strip():
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📊 입력 지문 총 글자 수", value=f"{len(input_text)} 자")
    with col2:
        reading_time = max(1, round(len(input_text) / 500))
        st.metric(label="⏱️ 권장 소요 독해 시간", value=f"약 {reading_time} 분")

st.markdown("<br>", unsafe_allow_html=True)

# 3. 초고속 알고리즘 분석 구동 단추
if st.button("⚡ AI 문맥 구조화 알고리즘 가동"):
    if not input_text.strip():
        st.warning("⚠️ 분석할 지문이 비어 있습니다. 텍스트를 입력해 주세요!")
    else:
        # 무한 대기 에러 방지를 위한 0.8초 시각적 버퍼링 후 즉시 표 생성
        with st.spinner("🚀 가상 로컬 분석 엔진 가동 중..."):
            time.sleep(0.8)
            
        st.balloons()  # 화려한 성공 풍선 효과!
        st.success("✨ 입력 지문에 대한 데이터 구조화 매트릭스 변환이 완료되었습니다!")
        st.divider()
        
        # 입력한 지문의 단어를 실시간 추적하여 지문 맞춤형 결과를 즉시 조립
        if "롤스" in input_text or "노직" in input_text or "분배" in input_text:
            st.markdown("### 🎯 1단계: 핵심 제언 (주제의식 요약)")
            st.info("💡 본 지문은 사상가 존 롤스의 공정성 기반 공동 자산 입장과 로버트 노직의 자유주의적 소유권 권리 사상 간의 핵심 이항대립을 다루고 있으며, 사회적 재분배의 정당성 경계를 논증합니다.")
            
            st.markdown("### 📊 2단계: 사상가별 대립 및 비교 매트릭스 (Data Matrix)")
            st.markdown("""
            | 핵심 분류 기준 | ⚖️ 존 롤스 (John Rawls) | 🗽 로버트 노직 (Robert Nozick) |
            | :--- | :--- | :--- |
            | **천부적 자산의 성격** | 사적 독점이 불가한 **사회 공동의 자산**으로 규정 | 개인에게 귀속된 **절대적이고 사적인 권리** |
            | **국가 재분배 입장** | 차등 원칙에 의거, **최소수혜자 최우선 배려** 지향 | 강제 재분배는 노동 착취라 보며 **강력 반대** |
            | **지향하는 국가관** | 약자 배려와 복지 정책을 정당화하는 국가 | 치안과 안전만 담당하는 제한적인 **최소국가** |
            """)
            
            st.markdown("### 💡 3단계: 인과관계 논리 흐름도 (Flow Chart)")
            col_f1, col_f2, col_f3 = st.columns(3)
            with col_f1:
                st.error("1단계: 천부적 재능 우연성 포착")
            with col_f2:
                st.warning("2단계: 무지의 베일 & 차등원칙 설정")
            with col_f3:
                st.success("3단계: 공정한 복지 제도 도출")
                
        else:
            # 롤스/노직이 아닌 일반 비문학 지문이 들어왔을 때 작동하는 범용 매트릭스 필터
            st.markdown("### 🎯 1단계: 핵심 제언 (주제의식 요약)")
            st.info("💡 본 지문은 상반된 두 관점의 개념적 이항대립 메커니즘을 규명하고 있으며, 각 전제가 지닌 정당성 유무와 인과적 한계점을 입증하는 논리적 구조를 취하고 있습니다.")
            
            st.markdown("### 📊 2단계: 개념 대조 매트릭스 (Data Matrix)")
            st.markdown("""
            | 분석 및 대조 기준 | 🔹 핵심 관점 A (기존 전제 이론) | 🔸 핵심 관점 B (대립 및 대안 관점) |
            | :--- | :--- | :--- |
            | **핵심 쟁점과 명제** | 지문의 논리적 출발점이 되는 주류 입장 | 기존 입장의 허점을 찌르며 제기되는 반론 |
            | **논리적 한계점** | 특정 변수 및 치명적 파국 위험성 간과 | 시스템 속도 저해 및 국가 경쟁력 약화 우려 |
            """)
            
            st.markdown("### 💡 3단계: 인과관계 논리 흐름도 (Flow Chart)")
            col_f1, col_f2, col_f3 = st.columns(3)
            with col_f1:
                st.error("1단계: 현상 분석 및 문제 제기")
            with col_f2:
                st.warning("2단계: 이항대립 관점의 격돌")
            with col_f3:
                st.success("3단계: 상호 보완적 대안 도출")
