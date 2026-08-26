import streamlit as st

# 1. 페이지 설정 (와이드 모드)
st.set_page_config(
    page_title="Limbus Company Archive",
    page_icon="⏱️",
    layout="wide",
)

# 2. 캐릭터 데이터 정의 (예시: 단테, 단테 뫼르소, 히스클리프 등)
# 실제 구현하실 때는 이미지 링크나 로컬 이미지 경로, 색상코드를 채워넣으세요.
CHARACTER_DATA = {
    "단테 (Dante)": {
        "color": "#FFD700",  # 대표 황금시계 색상
        "symbol": "⏰",
        "bg_image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1920",  # 예시 배경
        "char_image": "https://via.placeholder.com/300x400/333/fff?text=Dante",
        "description": "림버스 컴퍼니의 관리자. 머리가 시계로 되어 있으며, 수감자들을 부활시킬 수 있는 능력이 있다.",
    },
    "히스클리프 (Heathcliff)": {
        "color": "#1E90FF",  # 파란색 계열
        "symbol": "🏏",
        "bg_image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/111/fff?text=Heathcliff",
        "description": "폭력적이고 다혈질적인 성격의 수감자. 복수심에 불타며 배트형 무기를 주로 사용한다.",
    },
    "파우스트 (Faust)": {
        "color": "#00FA9A",  # 초록색 계열
        "symbol": "🧪",
        "bg_image": "https://images.unsplash.com/photo-1507668077129-56e32842fceb?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/fff?text=Faust",
        "description": "모든 것을 알고 있다고 주장하는 천재 수감자. 림버스 컴퍼니의 기술 대부분을 혼자 이해하고 있다.",
    },
}

# 3. 세션 상태를 이용한 현재 선택된 캐릭터 관리
if "selected_char" not in st.session_state:
    st.session_state.selected_char = "None"

# 4. 동적 배경 및 UI 스타일 적용 (CSS)
current_bg = (
    "https://images.unsplash.com/photo-1511447333015-45b65e60f6d5?q=80&w=1920"
)  # 기본 로비 분위기 (어두운 철제/콘크리트 느낌)
selected_color = "#FFFFFF"

if st.session_state.selected_char != "None":
    current_bg = CHARACTER_DATA[st.session_state.selected_char]["bg_image"]
    selected_color = CHARACTER_DATA[st.session_state.selected_char]["color"]

# CSS를 통한 배경 및 전역 스타일 커스텀
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), url("{current_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 림버스풍 텍스트 스타일 */
    .limbus-title {{
        color: {selected_color};
        font-family: 'Helvetica', sans-serif;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }}
    
    .stTextInput label {{
        color: #E0E0E0 !important;
        font-weight: bold;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# 5. 메인 레이아웃
st.markdown(
    "<h1 class='limbus-title' style='text-align: center;'>LIMBUS COMPANY ARCHIVE</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #A0A0A0;'>관리자님, 안내할 수감자를 선택하거나 입력해 주십시오.</p>",
    unsafe_allow_html=True,
)
st.write("---")

# 6. 사이드바 또는 상단 입력창 구성
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # 셀렉트박스나 텍스트 입력으로 캐릭터 선택
    char_list = ["None"] + list(CHARACTER_DATA.keys())
    user_input = st.selectbox(
        "수감자 검색 및 선택",
        char_list,
        help="원하는 캐릭터를 선택하세요.",
    )

    if user_input != "None":
        st.session_state.selected_char = user_input
        st.rerun()  # 상태 변경 시 화면 즉시 새로고침

# 7. 캐릭터 선택 후 상세 화면 출력
if st.session_state.selected_char != "None":
    char_name = st.session_state.selected_char
    data = CHARACTER_DATA[char_name]

    st.write("")
    st.write("")

    # 레이아웃 나누기 (문양 및 이름 / 캐릭터 사진 및 정보)
    c1, c2 = st.columns([1, 2])

    with c1:
        # 대표 문양과 색상 적용된 이름
        st.markdown(
            f"<h1 style='font-size: 80px; text-align: center;'>{data['symbol']}</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<h2 class='limbus-title' style='text-align: center;'>{char_name}</h2>",
            unsafe_allow_html=True,
        )
        st.image(data["char_image"], use_column_width=True)

    with c2:
        st.markdown(
            f"""
            <div style="background-color: rgba(20, 20, 20, 0.85); padding: 30px; border-left: 5px solid {data['color']}; border-radius: 5px;">
                <h3 style="color: {data['color']}; margin-top: 0;">수감자 상세 기록</h3>
                <p style="color: #E0E0E0; font-size: 18px; line-height: 1.6;">{data['description']}</p>
                <hr style="border-color: #444;">
                <p style="color: #888; font-size: 14px;">지하 4층 로비 시스템 연동 완료 // 보안 등급: 3급</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # 초기화 버튼
    if st.button("로비로 돌아가기"):
        st.session_state.selected_char = "None"
        st.rerun()

else:
    # 기본 로비 화면 연출
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px; color: #888;">
            <h3>[ LCB 버스 탑승 대기 중 ... ]</h3>
            <p>상단의 메뉴에서 수감자를 호출해 주세요.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
