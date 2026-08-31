import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="Limbus Company Archive",
    page_icon="⏱️",
    layout="wide",
)

# 2. 림버스 컴퍼니 12인 수감자 및 단테 데이터 정의
CHARACTER_DATA = {
    "단테 (Dante)": {
        "color": "#FFD700",
        "symbol": "⏰",
        "bg_image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/FFD700?text=Dante",
        "description": "림버스 컴퍼니의 관리자. 머리가 황금 시계로 되어 있으며, 수감자들을 부활시키는 능력을 가졌다.",
    },
    "이상 (Yi Sang)": {
        "color": "#A0C4FF",
        "symbol": "🪞",
        "bg_image": "https://images.unsplash.com/photo-1518495973542-4542c06a5843?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/A0C4FF?text=Yi+Sang",
        "description": "말수가 적고 난해한 말을 자주 하는 천재 전(前) N사 연구원. 거울 기술과 깊은 연관이 있다.",
    },
    "파우스트 (Faust)": {
        "color": "#70C1B3",
        "symbol": "🧪",
        "bg_image": "https://images.unsplash.com/photo-1507668077129-56e32842fceb?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/70C1B3?text=Faust",
        "description": "자신이 모든 것을 알고 있다고 말하는 천재 수감자. 림버스 컴퍼니의 기술적 기반을 혼자서 이해하고 있다.",
    },
    "돈키호테 (Don Quixote)": {
        "color": "#FFE156",
        "symbol": "🗡️",
        "bg_image": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/FFE156?text=Don+Quixote",
        "description": "정의로운 해결사를 열렬히 동경하는 과격하고 시끄러운 수감자. 언제나 엉뚱한 열정에 차 있다.",
    },
    "료슈 (Ryoshu)": {
        "color": "#E76F51",
        "symbol": "🔪",
        "bg_image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/E76F51?text=Ryoshu",
        "description": "예술과 '표현'에 광적으로 집착하는 위험한 인물. 줄임말을 자주 쓰며 폭력을 예술로 여긴다.",
    },
    "뫼르소 (Meursault)": {
        "color": "#4A90E2",
        "symbol": "📐",
        "bg_image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/4A90E2?text=Meursault",
        "description": "지시받은 사항 외에는 스스로 생각하지 않고 철저히 명령에만 복종하는 효율성의 화신.",
    },
    "홍루 (Hong Lu)": {
        "color": "#81B29A",
        "symbol": "🪷",
        "bg_image": "https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/81B29A?text=Hong+Lu",
        "description": "부유한 가문 출신으로 세상 물정에 다소 어둡지만, 언제나 나긋나긋하고 해맑은 태도를 유지한다.",
    },
    "히스클리프 (Heathcliff)": {
        "color": "#3D5A80",
        "symbol": "🏏",
        "bg_image": "https://images.unsplash.com/photo-1519501025264-65ba15a82390?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/3D5A80?text=Heathcliff",
        "description": "다혈질이고 거친 폭력을 서슴지 않는 복수심에 찬 수감자. 배트형 무기로 적을 타격한다.",
    },
    "이스마엘 (Ishmael)": {
        "color": "#F4A261",
        "symbol": "⚓",
        "bg_image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/F4A261?text=Ishmael",
        "description": "수감자들 중 드물게 상식적이고 이성적인 항해사 출신. 바다와 관련된 트라우마가 있다.",
    },
    "로쟈 (Rodion)": {
        "color": "#D90429",
        "symbol": "🎲",
        "bg_image": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/D90429?text=Rodion",
        "description": "도박과 돈을 좋아하며 낙천적이지만, 과거의 어두운 죄책감을 마음 속 깊이 품고 있는 수감자.",
    },
    "싱클레어 (Sinclair)": {
        "color": "#B5838D",
        "symbol": "⚙️",
        "bg_image": "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/B5838D?text=Sinclair",
        "description": "겁이 많고 여린 소년이지만, 극한의 상황에서는 잔혹한 면모가 고개를 드는 수감자.",
    },
    "오티스 (Outis)": {
        "color": "#606C38",
        "symbol": "🛡️",
        "bg_image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/606C38?text=Outis",
        "description": "뛰어난 전술안을 가진 베테랑 군인 출신. 관리자 단테에게 과도할 정도로 충성을 표명한다.",
    },
    "그레고르 (Gregor)": {
        "color": "#9A8C98",
        "symbol": "🪲",
        "bg_image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/9A8C98?text=Gregor",
        "description": "왼팔이 거대한 벌레의 형태로 변이된 전직 군인. 피로에 쩐 아저씨 같은 성격이지만 속은 깊다.",
    },
}

# 3. 세션 상태 관리
if "selected_char" not in st.session_state:
    st.session_state.selected_char = "None"

# 4. 동적 배경 및 UI 스타일 적용 (CSS)
current_bg = "https://images.unsplash.com/photo-1511447333015-45b65e60f6d5?q=80&w=1920"
selected_color = "#FFFFFF"

if st.session_state.selected_char != "None":
    current_bg = CHARACTER_DATA[st.session_state.selected_char]["bg_image"]
    selected_color = CHARACTER_DATA[st.session_state.selected_char]["color"]

st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), url("{current_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    .limbus-title {{
        color: {selected_color};
        font-family: 'Helvetica', sans-serif;
        font-weight: 800;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.9);
    }}
    
    .stSelectbox label {{
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
    "<p style='text-align: center; color: #A0A0A0;'>관리자님, 안내할 수감자를 선택해 주십시오.</p>",
    unsafe_allow_html=True,
)
st.write("---")

# 6. 캐릭터 선택 셀렉트박스
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    char_list = ["None"] + list(CHARACTER_DATA.keys())
    user_input = st.selectbox(
        "수감자 선택", char_list, help="조회할 수감자를 선택하세요."
    )

    if user_input != st.session_state.selected_char:
        st.session_state.selected_char = user_input
        st.rerun()

# 7. 캐릭터 선택 후 상세 화면 출력
if st.session_state.selected_char != "None":
    char_name = st.session_state.selected_char
    data = CHARACTER_DATA[char_name]

    st.write("")
    st.write("")

    c1, c2 = st.columns([1, 2])

    with c1:
        # 대표 문양과 색상 적용된 이름
        st.markdown(
            f"<h1 style='font-size: 80px; text-align: center; margin-bottom: 0;'>{data['symbol']}</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<h2 class='limbus-title' style='text-align: center;'>{char_name}</h2>",
            unsafe_allow_html=True,
        )
        
        # [수정 포인트] 최신 Streamlit 문법(use_container_width) 적용 및 예외 처리
        try:
            st.image(data["char_image"], use_container_width=True)
        except Exception:
            st.error("이미지를 불러오는 데 실패했습니다. 경로를 확인해주세요.")

    with c2:
        st.markdown(
            f"""
            <div style="background-color: rgba(20, 20, 20, 0.88); padding: 35px; border-left: 6px solid {data['color']}; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
                <h3 style="color: {data['color']}; margin-top: 0; font-weight: 700;">수감자 상세 기록</h3>
                <p style="color: #E0E0E0; font-size: 19px; line-height: 1.7;">{data['description']}</p>
                <hr style="border-color: #444; margin: 25px 0;">
                <p style="color: #888; font-size: 14px; font-family: monospace;">LCB BUS SYSTEM // ACCESS GRANTED</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    col_btn1, col_btn2, col_btn3 = st.columns([2, 1, 2])
    with col_btn2:
        if st.button("로비로 돌아가기", use_container_width=True):
            st.session_state.selected_char = "None"
            st.rerun()

else:
    # 기본 로비 화면 연출
    st.markdown(
        """
        <div style="text-align: center; margin-top: 80px; color: #888;">
            <h3 style="font-family: monospace; color: #ccc;">[ LCB 버스 탑승 대기 중 ... ]</h3>
            <p>상단의 메뉴에서 수감자를 호출하여 상세 기록을 열람하십시오.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
