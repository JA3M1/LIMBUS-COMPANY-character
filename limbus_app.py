import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Limbus Company Info", page_icon="⏰", layout="wide")

# 캐릭터별 데이터 정의
CHARACTER_DATA = {
    "기본 로비": {
        "color": "#D4AF37",
        "bg_color": "#121212",
        "description": "버스를 선택하여 수감자의 정보를 확인하세요.",
        "image": "https://dummyimage.com/800x400/121212/D4AF37&text=Limbus+Company+Lobby",
        "is_lobby": True
    },
    "히스클리프": {
        "color": "#1C355E",
        "bg_color": "#0d1b2a",
        "title": "제5수감자 히스클리프",
        "gender": "남성",
        "birthday": "미상",
        "quote": '"어이, 시계대가리. 이딴 데서 시간 낭비할 바엔 콱 쥐어 패고 끝내자고."',
        "stagger": "흐트러짐 구간 1~2개 (인격별 상이)",
        "skills": [
            "기본 1스킬: 맹수다운 타격 (타격/분노)",
            "기본 2스킬: 후려치기 (타격/질투)",
            "기본 3스킬: 짓이기기 (타격/우울)"
        ],
        "description": "폭주하기 쉬운 다혈질이지만, 그 이면에 깊은 상처와 집착을 품고 있는 수감자.",
        "relations": [
            ("단테", "시계대가리라고 부르며 막 대하지만, 은근히 지시를 따름"),
            ("이스마엘", "버스 내에서 툭하면 의견 충돌로 싸우는 앙숙 관계"),
            ("캐서린", "모든 행동의 이유이자 애증이 얽힌 연인"),
            ("넬리", "워더링하이츠 시절부터 알고 지낸 인물"),
            ("뫼르소", "임무 수행 중 성향 차이로 자주 대조되는 인물")
        ],
        "songs": [
            {"title": "Through Patches of Violet", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, # 실제 유튜브 링크로 교체하세요
            {"title": "사라지네 (Vocal. 히스클리프)", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
        ],
        "image": "https://dummyimage.com/300x400/1C355E/FFFFFF&text=Heathcliff",
        "logo": "https://dummyimage.com/100x100/1C355E/FFFFFF&text=Logo",
        "is_lobby": False
    },
    "파우스트": {
        "color": "#FFB1B4",
        "bg_color": "#2a1516",
        "title": "제2수감자 파우스트",
        "gender": "여성",
        "birthday": "미상",
        "quote": '"파우스트는 모든 것을 알고 있어요."',
        "stagger": "흐트러짐 구간 1~2개 (인격별 상이)",
        "skills": [
            "기본 1스킬: 아래로 베기 (참격/오만)",
            "기본 2스킬: 올려 베기 (참격/나태)",
            "기본 3스킬: 수직 내려찍기 (타격/우울)"
        ],
        "description": "도시 최고의 천재라 자부하며, 메피스토펠레스의 엔진을 설계한 수감자.",
        "relations": [
            ("단테", "관리자의 역할을 설명해주지만, 종종 오만한 태도를 보임"),
            ("베르길리우스", "서로의 속내를 숨긴 채 협력하는 비즈니스 관계"),
            ("카론", "자신이 만든 버스를 운전하는 길잡이")
        ],
        "songs": [
            {"title": "파우스트 테마곡", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
        ],
        "image": "https://dummyimage.com/300x400/FFB1B4/000000&text=Faust",
        "logo": "https://dummyimage.com/100x100/FFB1B4/000000&text=Logo",
        "is_lobby": False
    },
    "이스마엘": {
        "color": "#FF7E00",
        "bg_color": "#211000",
        "title": "제8수감자 이스마엘",
        "gender": "여성",
        "birthday": "미상",
        "quote": '"관리자님, 제발 생각이라는 걸 좀 하고 지시를 내리시겠어요?"',
        "stagger": "흐트러짐 구간 1~2개 (인격별 상이)",
        "skills": [
            "기본 1스킬: 타격 (타격/우울)",
            "기본 2스킬: 방패 강타 (타격/나태)",
            "기본 3스킬: 제압 (타격/분노)"
        ],
        "description": "합리적이고 이성적이지만, 과거의 복수심(에이해브)에 사로잡혀 있던 수감자.",
        "relations": [
            ("단테", "관리자의 무능함을 자주 지적하지만 끝내 의지함"),
            ("히스클리프", "이성적인 자신과 본능적인 히스클리프 사이의 끝없는 마찰"),
            ("에이해브", "맹목적인 증오의 대상이자 과거 선장")
        ],
        "songs": [
            {"title": "Compass", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
        ],
        "image": "https://dummyimage.com/300x400/FF7E00/000000&text=Ishmael",
        "logo": "https://dummyimage.com/100x100/FF7E00/000000&text=Logo",
        "is_lobby": False
    }
}

# 세션 상태 초기화
if "selected_char" not in st.session_state:
    st.session_state["selected_char"] = "기본 로비"

# 사이드바 구성
st.sidebar.title("⏰ 버스 터미널")
st.sidebar.markdown("---")
char_list = list(CHARACTER_DATA.keys())
selected = st.sidebar.radio("수감자 / 로비 선택", char_list)

if selected != st.session_state["selected_char"]:
    st.session_state["selected_char"] = selected
    st.rerun()

current_data = CHARACTER_DATA[st.session_state["selected_char"]]
theme_color = current_data["color"]
bg_color = current_data["bg_color"]

# CSS 스타일 주입 (배경색 및 폰트 색상 동적 변경)
st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg_color}; }}
    h1, h2, h3, p, span, label, li {{ color: {theme_color} !important; }}
    .stRadio label {{ color: #FFFFFF !important; }}
    hr {{ border-color: {theme_color}; }}
    </style>
""", unsafe_allow_html=True)

# 메인 화면 렌더링
if current_data["is_lobby"]:
    st.title("LIMBUS COMPANY - LOBBY")
    st.markdown(current_data["description"])
    st.image(current_data["image"], use_container_width=True)
else:
    # 캐릭터 상세 페이지
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        if current_data["logo"]:
            st.image(current_data["logo"], width=80)
        st.title(current_data["title"])
        st.markdown(f"*{current_data['quote']}*")
        st.image(current_data["image"], use_container_width=True)
        
        st.markdown("### 📋 기본 정보")
        st.markdown(f"- **성별**: {current_data['gender']}")
        st.markdown(f"- **생일**: {current_data['birthday']}")
        st.markdown(f"- **흐트러짐**: {current_data['stagger']}")
            
    with col2:
        st.markdown(f"### 📌 캐릭터 소개")
        st.markdown(current_data['description'])
        
        st.markdown("### ⚔️ 기본 인격 스킬")
        for skill in current_data["skills"]:
            st.markdown(f"- {skill}")
            
        st.markdown("### 🤝 인물 관계도")
        for rel_name, rel_desc in current_data["relations"]:
            st.markdown(f"- **{rel_name}**: {rel_desc}")
            
        st.markdown("### 🎵 관련 테마 및 보컬 곡")
        for song in current_data["songs"]:
            st.markdown(f"**{song['title']}**")
            st.video(song["url"]) # 유튜브 영상 임베드
