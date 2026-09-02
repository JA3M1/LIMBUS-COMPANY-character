import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Limbus Company Info", page_icon="⏰", layout="wide")

# 캐릭터별 데이터 정의 (12명 수감자 + 기본 로비)
CHARACTER_DATA = {
    "기본 로비": {
        "color": "#D4AF37",
        "bg_color": "#121212",
        "description": "버스를 선택하여 수감자의 정보를 확인하세요.",
        "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=800&auto=format&fit=crop",
        "is_lobby": True
    },
    "이상": {
        "color": "#4A90E2",
        "bg_color": "#0d1626",
        "title": "제1수감자 이상",
        "gender": "남성",
        "birthday": "미상",
        "quote": '"알 수 없는 일이지. 어째서 날아가야만 하는 것인가."',
        "stagger": "흐트러짐 구간 2개",
        "skills": [
            "기본 1스킬: 응시 (참격/오만)",
            "기본 2스킬: 타격 (타격/우울)",
            "기본 3스킬: 가르기 (참격/색욕)"
        ],
        "description": "말수가 적고 항상 공허한 눈을 하고 있는 천재이자 시인.",
        "relations": [
            ("파우스트", "서로의 지적 수준을 은근히 존중하는 관계"),
            ("단테", "자신의 말을 묘하게 이해해 주는 시계대가리")
        ],
        "songs": [
            {"title": "이상 테마곡 - Effloresced", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
        "is_lobby": False
    },
    "파우스트": {
        "color": "#FFB1B4",
        "bg_color": "#2a1516",
        "title": "제2수감자 파우스트",
        "gender": "여성",
        "birthday": "미상",
        "quote": '"파우스트는 모든 것을 알고 있어요."',
        "stagger": "흐트러짐 구간 1~2개",
        "skills": [
            "기본 1스킬: 아래로 베기 (참격/오만)",
            "기본 2스킬: 올려 베기 (참격/나태)",
            "기본 3스킬: 수직 내려찍기 (타격/우울)"
        ],
        "description": "도시 최고의 천재라 자부하며, 메피스토펠레스의 엔진을 설계한 수감자.",
        "relations": [
            ("단테", "관리자의 역할을 설명해주지만, 종종 오만한 태도를 보임"),
            ("베르길리우스", "서로의 속내를 숨긴 채 협력하는 관계")
        ],
        "songs": [
            {"title": "파우스트 테마 관련 OST", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
        "is_lobby": False
    },
    "돈키호테": {
        "color": "#FFD700",
        "bg_color": "#26220d",
        "title": "제3수감자 돈키호테",
        "gender": "여성",
        "birthday": "미상",
        "quote": '"정의의 사도가 나가신다! 모두 길을 비켜라!"',
        "stagger": "흐트러짐 구간 3개",
        "skills": [
            "기본 1스킬: 찌르기 (관통/오만)",
            "기본 2스킬: 정의의 일격 (관통/질투)",
            "기본 3s킬: 돌진 (관통/분노)"
        ],
        "description": "지상 최고의 해결사인 '포졸'과 '색마'를 동경하며 정의를르 부르짖는 열혈 수감자.",
        "relations": [
            ("로쟈", "함께 장난을 치거나 어울리는 유쾌한 조합"),
            ("단테", "자신의 영웅이자 관리자님")
        ],
        "songs": [
            {"title": "돈키호테 관련 곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1563089145-599997674d42?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
        "is_lobby": False
    },
    "료슈": {
        "color": "#C0392B",
        "bg_color": "#2a0d0d",
        "title": "제4수감자 료슈",
        "gender": "여성",
        "birthday": "미상",
        "quote": '"……예술적이군."',
        "stagger": "흐트러짐 구간 1개",
        "skills": [
            "기본 1스킬: 섬단 (참격/질투)",
            "기본 2스킬: 베기 (참격/분노)",
            "기본 3스킬: 난무 (참격/오만)"
        ],
        "description": "손에 항상 담배를 들고 다니며, 잔인하고 폭력적인 행위를 예술로 비유하는 수감자.",
        "relations": [
            ("싱클레어", "은근히 료슈를 무서워하면서도 엮이는 수감자")
        ],
        "songs": [
            {"title": "료슈 관련 곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
        "is_lobby": False
    },
    "히스클리프": {
        "color": "#1C355E",
        "bg_color": "#0d1b2a",
        "title": "제5수감자 히스클리프",
        "gender": "남성",
        "birthday": "미상",
        "quote": '"어이, 시계대가리. 이딴 데서 시간 낭비할 바엔 콱 쥐어 패고 끝내자고."',
        "stagger": "흐트러짐 구간 1~2개",
        "skills": [
            "기본 1스킬: 맹수다운 타격 (타격/분노)",
            "기본 2스킬: 후려치기 (타격/질투)",
            "기본 3스킬: 짓이기기 (타격/우울)"
        ],
        "description": "폭주하기 쉬운 다혈질이지만, 그 이면에 깊은 상처와 집착을 품고 있는 수감자.",
        "relations": [
            ("이스마엘", "버스 내에서 툭하면 의견 충돌로 싸우는 앙숙 관계"),
            ("캐서린", "모든 행동의 이유이자 애증이 얽힌 연인")
        ],
        "songs": [
            {"title": "Through Patches of Violet (Mili)", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"},
            {"title": "사라지네 (Vocal. 히스클리프)", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
        "is_lobby": False
    },
    "뫼르소": {
        "color": "#2980B9",
        "bg_color": "#0f2027",
        "title": "제6수감자 뫼르소",
        "gender": "남성",
        "birthday": "미상",
        "quote": '"지시는 하달되었고, 수행할 뿐이다."',
        "stagger": "흐트러짐 구간 2개",
        "skills": [
            "기본 1스킬: 강타 (타격/우울)",
            "기본 2스킬: 제압 (타격/나태)",
            "기본 3스킬: 단죄 (타격/오만)"
        ],
        "description": "명령에 절대적으로 복종하며 감정이 거의 드러나지 않는 철저한 합리주의자.",
        "relations": [
            ("히스클리프", "정반대의 성향으로 자주 부딪힘")
        ],
        "songs": [
            {"title": "뫼르소 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
        "is_lobby": False
    },
    "홍루": {
        "color": "#E67E22",
        "bg_color": "#26170d",
        "title": "제7수감자 홍루",
        "gender": "남성",
        "birthday": "미상",
        "quote": '"어머, 저기에 재미있는 구경거리가 있네요~"',
        "stagger": "흐트러짐 구간 2개",
        "skills": [
            "기본 1스킬: 타격 (타격/색욕)",
            "기본 2스킬: 연격 (타격/나태)",
            "기본 3스킬: 후려치기 (타격/질투)"
        ],
        "description": "부유한 저택에서 자라 세상 물정에 다소 어둡지만, 천진난만한 성격의 수감자.",
        "relations": [
            ("싱클레어", "순진한 면모로 공감대를 형성")
        ],
        "songs": [
            {"title": "홍루 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
        "is_lobby": False
    },
    "이스마엘": {
        "color": "#FF7E00",
        "bg_color": "#211000",
        "title": "제8수감자 이스마엘",
        "gender": "여성",
        "birthday": "미상",
        "quote": '"관리자님, 제발 생각이라는 걸 좀 하고 지시를 내리시겠어요?"',
        "stagger": "흐트러짐 구간 1~2개",
        "skills": [
            "기본 1스킬: 타격 (타격/우울)",
            "기본 2스킬: 방패 강타 (타격/나태)",
            "기본 3스킬: 제압 (타격/분노)"
        ],
        "description": "합리적이고 이성적이지만, 과거의 복수심(에이해브)에 사로잡혀 있던 수감자.",
        "relations": [
            ("히스클리프", "이성적인 자신과 본능적인 히스클리프 사이의 끝없는 마찰"),
            ("에이해브", "맹목적인 증오의 대상")
        ],
        "songs": [
            {"title": "Compass (Mili)", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
        "is_lobby": False
    },
    "오티스": {
        "color": "#27AE60",
        "bg_color": "#0d2616",
        "title": "제9수감자 오티스",
        "gender": "여성",
        "birthday": "미상",
        "quote": '"오직 관리자님만을 위해 이 한 몸 바치겠습니다!"',
        "stagger": "흐트러짐 구간 2개",
        "skills": [
            "기본 1스킬: 찌르기 (관통/오만)",
            "기본 2스킬: 사격 (관통/색욕)",
            "기본 3s킬: 집중 포화 (관통/분노)"
        ],
        "description": "군인 출신으로 관리자(단테)에게 극단적일 정도로 충성하는 베테랑.",
        "relations": [
            ("그레고르", "군대식 농담이나 갈등을 자주 빚음")
        ],
        "songs": [
            {"title": "오티스 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
        "is_lobby": False
    },
    "로쟈": {
        "color": "#9B59B6",
        "bg_color": "#1f0d26",
        "title": "제10수감자 로쟈",
        "gender": "여성",
        "birthday": "미상",
        "quote": '"에이, 복잡한 건 나중에 생각하고 일단 즐기자고!"',
        "stagger": "흐트러짐 구간 2~3개",
        "skills": [
            "기본 1스킬: 타격 (타격/질투)",
            "기본 2스킬: 후려치기 (타격/색욕)",
            "기본 3스킬: 난타 (타격/나태)"
        ],
        "description": "여유롭고 낙천적인 성격이지만, 깊은 내면에는 과거의 무거운 선택에 대한 죄책감이 숨어있는 수감자.",
        "relations": [
            ("돈키호테", "장난을 치며 잘 받아주는 언니 같은 관계")
        ],
        "songs": [
            {"title": "로쟈 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
        "is_lobby": False
    },
    "싱클레어": {
        "color": "#F39C12",
        "bg_color": "#261f0d",
        "title": "제11수감자 싱클레어",
        "gender": "남성",
        "birthday": "미상",
        "quote": '"제발… 더 이상 저를 몰아세우지 말아 주세요."',
        "stagger": "흐트러짐 구간 3개",
        "skills": [
            "기본 1스킬: 찌르기 (관통/분노)",
            "기본 2스킬: 가르기 (참격/색욕)",
            "기본 3스킬: 절단 (참격/오만)"
        ],
        "description": "순수하고 여린 소년이지만, 극한의 상황에서 잠재된 광기와 폭력성을 드러내는 수감자.",
        "relations": [
            ("크로마르", "과거 트라우마의 원흉이자 악연")
        ],
        "songs": [
            {"title": "싱클레어 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
        "is_lobby": False
    },
    "그레고르": {
        "color": "#7F8C8D",
        "bg_color": "#1a1c1d",
        "title": "제12수감자 그레고르",
        "gender": "남성",
        "birthday": "미상",
        "quote": '"이 벌레 같은 팔짝... 익숙해질 때도 됐잖아?"',
        "stagger": "흐트러짐 구간 2개",
        "skills": [
            "기본 1스킬: 베기 (참격/나태)",
            "기본 2스킬: 절단 (참격/분노)",
            "기본 3스킬: 폭격 (타격/우울)"
        ],
        "description": "과거 연기전쟁의 용병 출신으로, 벌레로 변이된 오른팔을 지니고 있는 베테랑 수감자.",
        "relations": [
            ("오티스", "군대 경험을 공유하지만 서로 툴툴거림")
        ],
        "songs": [
            {"title": "그레고르 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}
        ],
        "image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=400&auto=format&fit=crop",
        "logo": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=100&auto=format&fit=crop",
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
            st.video(song["url"])
