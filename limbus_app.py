import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Limbus Company Info",
    page_icon="⏰",
    layout="wide"
)

# 캐릭터별 데이터 정의 (상징 색상, 이미지, 관계, 노래 등)
CHARACTER_DATA = {
    "기본 로비": {
        "color": "#D4AF37", # 황금색/로비 톤
        "bg_color": "#121212",
        "description": "버스를 선택하여 수감자의 정보를 확인하세요.",
        "relations": [],
        "songs": [],
        "image": "",
        "logo": ""
    },
    "히스클리프": {
        "color": "#1C355E", # 네이비/푸른계열
        "bg_color": "#0d1b2a",
        "title": "제5수감자 히스클리프",
        "description": "폭주하기 쉬운 다혈질이지만, 그 이면에 깊은 상처와 집착을 품고 있는 수감자.",
        "relations": [
            ("캐서린", "애증이 얽힌 연인이자 모든 사건의 핵심"),
            ("뫼르소", "임무 수행 중 자주 부딪히거나 대조되는 인물"),
            ("오티스", "거친 언행으로 인해 자주 마찰을 빚는 동료")
        ],
        "songs": [
            ("Through Patches of Violet", "히스클리프 전투 OST"),
            ("사라지네 (Vocal. 히스클리프)", "보컬 곡")
        ],
        "image": "https://via.placeholder.com/300x400/1C355E/FFFFFF?text=Heathcliff",
        "logo": "https://via.placeholder.com/100x100/1C355E/FFFFFF?text=Logo"
    },
    "단테": {
        "color": "#E5A93B", # 시계 황금빛/노란색
        "bg_color": "#1a150b",
        "title": "관리자 단테",
        "description": "머리에 커다란 시계를 인 림버스 컴퍼니의 관리자. 수감자들의 부활을 관장한다.",
        "relations": [
            ("베르길리우스", "길잡이자 실질적인 지시를 내리는 안내자"),
            ("카론", "메피스토펠레스를 운전하는 괴짜 드라이버"),
            ("수감자들", "관리해야 할 12명의 통제 불능 수감자들")
        ],
        "songs": [
            ("Limbus Company Main Theme", "메인 오프닝 곡")
        ],
        "image": "https://via.placeholder.com/300x400/E5A93B/000000?text=Dante",
        "logo": "https://via.placeholder.com/100x100/E5A93B/000000?text=Logo"
    }
}

# 세션 스테이트 초기화
if "selected_char" not in st.session_state:
    st.session_state["selected_char"] = "기본 로비"

# 사이드바: 캐릭터 선택 메뉴
st.sidebar.title("⏰ 림버스 컴퍼니 버스 터미널")
st.sidebar.markdown("---")

char_list = list(CHARACTER_DATA.keys())
selected = st.sidebar.radio("수감자를 선택하세요", char_list)

if selected != st.session_state["selected_char"]:
    st.session_state["selected_char"] = selected
    st.rerun()

# 현재 선택된 캐릭터 데이터 로드
current_data = CHARACTER_DATA[st.session_state["selected_char"]]
theme_color = current_data["color"]
bg_color = current_data["bg_color"]

# 동적 배경색 및 글씨 색상 적용을 위한 CSS 주입
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
    }}
    h1, h2, h3, p, span, label {{
        color: {theme_color} !important;
    }}
    .stRadio label {{
        color: #FFFFFF !important;
    }}
    .custom-box {{
        border: 2px solid {theme_color};
        padding: 20px;
        border-radius: 10px;
        background-color: rgba(0, 0, 0, 0.4);
    }}
    </style>
""", unsafe_allow_html=True)

# 메인 화면 구성
if st.session_state["selected_char"] == "기본 로비":
    st.title("LIMBUS COMPANY - LOBBY")
    st.markdown("환영합니다, 관리자님. 왼쪽 사이드바에서 수감자를 선택하여 상세 기록을 열람하십시오.")
    st.image("https://via.placeholder.com/800x400/121212/D4AF37?text=Limbus+Company+Bus+Lobby", use_column_width=True)
else:
    # 캐릭터 페이지
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if current_data["logo"]:
            st.image(current_data["logo"], width=100)
        st.title(current_data["title"])
        if current_data["image"]:
            st.image(current_data["image"], use_column_width=True)
            
    with col2:
        st.markdown(f"### 📌 캐릭터 소개")
        st.markdown(f"<p style='font-size: 18px;'>{current_data['description']}</p>", unsafe_allow_html=True)
        
        st.markdown("### 🤝 주변 인물 및 관계도")
        for rel_name, rel_desc in current_data["relations"]:
            st.markdown(f"- **{rel_name}**: {rel_desc}")
            
        st.markdown("### 🎵 관련 테마 및 보컬 곡")
        for song_title, song_desc in current_data["songs"]:
            st.markdown(f"- 🎶 **{song_title}** ({song_desc})")
