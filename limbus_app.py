import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Limbus Company Info", page_icon="⏰", layout="wide")

# 캐릭터별 데이터 (상징색, 스토리 배경 이미지, 프로필/전투/스토리후/로고 이미지)
CHARACTER_DATA = {
    "기본 로비": {
        "color": "#FFD700", # 황금색
        "bg_image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1920&auto=format&fit=crop",
        "description": "버스를 선택하여 수감자의 정보를 확인하세요.",
        "is_lobby": True
    },
    "단테": {
        "color": "#b01c37", # 요청하신 단테 상징색 적용
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/b/b4/Lab_Background.png",
        "title": "관리자 단테",
        "gender": "미상",
        "birthday": "미상",
        "quote": '"틱... 톡... (수감자들을 부활시키며)"',
        "stagger": "불사신 (수감자들의 고통을 대신 느낌)",
        "skills": [
            "기본 능력: 수감자 부활 (황금가지의 힘)",
            "패시브: 수감자와의 감정 공감 및 고통 공유",
            "특수 능력: 시간 되감기 및 지휘"
        ],
        "description": "머리 대신 거대한 황금빛 시계를 달고 있는 림버스 컴퍼니의 제1관리자. 수감자들을 부활시킬 수 있는 유일한 존재이지만, 기억을 잃은 상태이다.",
        "relations": [
            ("베르길리우스", "버스의 총지휘관이자 단테를 이끄는 안내자"),
            ("카론", "메피스토펠레스를 운전하는 말없는 동반자"),
            ("수감자들", "단테를 '시계대가리'라 부르며 때로는 불평하고 때로는 의지하는 부하들")
        ],
        "songs": [{"title": "Limbus Company Main Theme", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/a/a2/Dante_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/a/a2/Dante_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/a/a2/Dante_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/a/a2/Dante_Icon.png",
        "is_lobby": False
    },
    "이상": {
        "color": "#4A90E2",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/e/ee/Canto_IV_Background.png",
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
        "description": "말수가 적고 항상 공허한 눈을 하고 있는 천재이자 시인. 구(舊) L사에서 일했던 과거가 있다.",
        "relations": [
            ("파우스트", "서로의 지적 수준과 과거를 은근히 존중하는 관계"),
            ("단테", "자신의 말을 묘하게 이해해 주는 시계대가리"),
            ("구보", "과거 이상을 괴로움과 영감으로 몰아넣었던 인물"),
            ("동백", "과거 이상이 품었던 이상향과 예술의 상징")
        ],
        "songs": [{"title": "이상 테마곡 - Effloresced", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/7/73/Yi_Sang_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/0/07/Yi_Sang_ID.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/7/73/Yi_Sang_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/7/73/Yi_Sang_Icon.png",
        "is_lobby": False
    },
    "파우스트": {
        "color": "#FFB1B4",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/b/b4/Lab_Background.png",
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
            ("베르길리우스", "서로의 속내를 숨긴 채 협력하는 비즈니스 관계")
        ],
        "songs": [{"title": "파우스트 관련 테마 OST", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/8/82/Faust_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/8/82/Faust_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/8/82/Faust_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/8/82/Faust_Icon.png",
        "is_lobby": False
    },
    "돈키호테": {
        "color": "#FFD700",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/7/70/Canto_VII_Background.png",
        "title": "제3수감자 돈키호테",
        "gender": "여성",
        "birthday": "미상",
        "quote": '"정의의 사도가 나가신다! 모두 길을 비켜라!"',
        "stagger": "흐트러짐 구간 3개",
        "skills": [
            "기본 1스킬: 찌르기 (관통/오만)",
            "기본 2스킬: 정의의 일격 (관통/질투)",
            "기본 3스킬: 돌진 (관통/분노)"
        ],
        "description": "지상 최고의 해결사를 동경하며 정의를 부르짖는 열혈 수감자.",
        "relations": [
            ("로쟈", "함께 장난을 치거나 어울리는 유쾌한 언니 동생 관계"),
            ("단테", "자신의 영웅이자 관리자님")
        ],
        "songs": [{"title": "돈키호테 관련 곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/2/29/Don_Quixote_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/2/29/Don_Quixote_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/2/29/Don_Quixote_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/2/29/Don_Quixote_Icon.png",
        "is_lobby": False
    },
    "료슈": {
        "color": "#C0392B",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/2/2b/Alleyway_Background.png",
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
        "songs": [{"title": "료슈 관련 곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/3/3b/Ryōshū_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/3/3b/Ryōshū_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/3/3b/Ryōshū_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/3/3b/Ryōshū_Icon.png",
        "is_lobby": False
    },
    "히스클리프": {
        "color": "#4682B4",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/5/52/Canto_VI_Background.png",
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
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/6/67/Heathcliff_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/6/67/Heathcliff_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/6/67/Heathcliff_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/6/67/Heathcliff_Icon.png",
        "is_lobby": False
    },
    "뫼르소": {
        "color": "#2980B9",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/b/b4/Lab_Background.png",
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
        "songs": [{"title": "뫼르소 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/e/ef/Meursault_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/e/ef/Meursault_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/e/ef/Meursault_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/e/ef/Meursault_Icon.png",
        "is_lobby": False
    },
    "홍루": {
        "color": "#E67E22",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/2/2b/Alleyway_Background.png",
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
        "songs": [{"title": "홍루 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/1/10/Hong_Lu_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/1/10/Hong_Lu_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/1/10/Hong_Lu_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/1/10/Hong_Lu_Icon.png",
        "is_lobby": False
    },
    "이스마엘": {
        "color": "#FF7E00",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/9/93/Canto_V_Background.png",
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
            ("에이해브", "맹목적인 증오의 대상이자 과거 선장")
        ],
        "songs": [{"title": "Compass (Mili)", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/7/7b/Ishmael_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/7/7b/Ishmael_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/7/7b/Ishmael_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/7/7b/Ishmael_Icon.png",
        "is_lobby": False
    },
    "오티스": {
        "color": "#27AE60",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/b/b4/Lab_Background.png",
        "title": "제9수감자 오티스",
        "gender": "여성",
        "birthday": "미상",
        "quote": '"오직 관리자님만을 위해 이 한 몸 바치겠습니다!"',
        "stagger": "흐트러짐 구간 2개",
        "skills": [
            "기본 1스킬: 찌르기 (관통/오만)",
            "기본 2스킬: 사격 (관통/색욕)",
            "기본 3스킬: 집중 포화 (관통/분노)"
        ],
        "description": "군인 출신으로 관리자(단테)에게 극단적일 정도로 충성하는 베테랑.",
        "relations": [
            ("그레고르", "군대식 농담이나 과거 전쟁 트라우마로 갈등을 빚음")
        ],
        "songs": [{"title": "오티스 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/f/f6/Outis_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/f/f6/Outis_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/f/f6/Outis_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/f/f6/Outis_Icon.png",
        "is_lobby": False
    },
    "로쟈": {
        "color": "#9B59B6",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/2/2b/Alleyway_Background.png",
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
            ("돈키호테", "장난을 치며 잘 받아주는 친근한 언니 동생 관계")
        ],
        "songs": [{"title": "로쟈 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/c/c5/Rodion_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/c/c5/Rodion_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/c/c5/Rodion_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/c/c5/Rodion_Icon.png",
        "is_lobby": False
    },
    "싱클레어": {
        "color": "#F39C12",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/4/4e/Canto_III_Background.png",
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
            ("크로마르", "과거 트라우마의 원흉이자 벗어날 수 없는 악연"),
            ("데미안", "싱클레어에게 조언을 건네며 이끄는 미스터리한 인물")
        ],
        "songs": [{"title": "싱클레어 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/a/ab/Sinclair_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/a/ab/Sinclair_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/a/ab/Sinclair_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/a/ab/Sinclair_Icon.png",
        "is_lobby": False
    },
    "그레고르": {
        "color": "#7F8C8D",
        "bg_image": "https://static.wikia.nocookie.net/limbuscompany/images/b/b4/Lab_Background.png",
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
            ("오티스", "군대식 농담이나 서로 툴툴거리는 앙숙")
        ],
        "songs": [{"title": "그레고르 테마곡", "url": "https://www.youtube.com/watch?v=V80o6Z7SgqE"}],
        "image": "https://static.wikia.nocookie.net/limbuscompany/images/f/f6/Gregor_Icon.png",
        "combat_image": "https://static.wikia.nocookie.net/limbuscompany/images/f/f6/Gregor_Icon.png",
        "post_story_image": "https://static.wikia.nocookie.net/limbuscompany/images/f/f6/Gregor_Icon.png",
        "logo": "https://static.wikia.nocookie.net/limbuscompany/images/f/f6/Gregor_Icon.png",
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
selected = st.sidebar.radio("관리자 / 수감자 / 로비 선택", char_list)

if selected != st.session_state["selected_char"]:
    st.session_state["selected_char"] = selected
    st.rerun()

current_data = CHARACTER_DATA[st.session_state["selected_char"]]
theme_color = current_data["color"]
bg_image_url = current_data["bg_image"]

# CSS 스타일 주입 (캐릭터별 배경 이미지 + 상징 컬러 글씨 + 가독성을 위한 반투명 패널 레이아웃)
st.markdown(f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), url("{bg_image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 텍스트 상징색 적용 */
    h1, h2, h3, p, span, label, li {{
        color: {theme_color} !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }}
    
    .stRadio label {{
        color: #FFFFFF !important;
    }}
    
    hr {{
        border-color: {theme_color};
    }}
    
    /* 가독성을 높이기 위한 컨테이너 박스 꾸미기 */
    div.block-container {{
        background-color: rgba(15, 15, 15, 0.85);
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid {theme_color};
        box-shadow: 0 4px 20px rgba(0,0,0,0.7);
    }}
    </style>
""", unsafe_allow_html=True)

# 메인 화면 렌더링
if current_data["is_lobby"]:
    st.title("LIMBUS COMPANY - LOBBY")
    st.markdown(current_data["description"])
    st.info("💡 좌측 사이드바에서 관리자(단테)나 수감자를 선택하면 해당 인물의 스토리 배경과 상징 컬러 테마로 전환됩니다.")
else:
    # 캐릭터 상세 페이지 레이아웃
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        # 로고 표시
        if current_data.get("logo"):
            st.image(current_data["logo"], width=80)
            
        st.title(current_data["title"])
        st.markdown(f"*{current_data['quote']}*")
        
        # 탭을 활용해 '기본 모습', '전투 중 모습', '스토리 후 변화' 분할 표시
        img_tab1, img_tab2, img_tab3 = st.tabs(["기본 모습", "전투 중 모습", "스토리 후 변화"])
        
        with img_tab1:
            st.image(current_data["image"], use_container_width=True)
        with img_tab2:
            st.image(current_data["combat_image"], use_container_width=True)
        with img_tab3:
            st.image(current_data["post_story_image"], use_container_width=True)
        
        st.markdown("### 📋 기본 정보")
        st.markdown(f"- **성별**: {current_data['gender']}")
        st.markdown(f"- **생일**: {current_data['birthday']}")
        st.markdown(f"- **흐트러짐**: {current_data['stagger']}")
            
    with col2:
        st.markdown(f"### 📌 캐릭터 소개")
        st.markdown(current_data['description'])
        
        st.markdown("### ⚔️ 기본 능력 및 스킬")
        for skill in current_data["skills"]:
            st.markdown(f"- {skill}")
            
        st.markdown("### 🤝 인간관계 및 주변 인물")
        for rel_name, rel_desc in current_data["relations"]:
            st.markdown(f"- **{rel_name}**: {rel_desc}")
            
        st.markdown("### 🎵 관련 테마 및 보컬 곡")
        for song in current_data["songs"]:
            st.markdown(f"**{song['title']}**")
            st.video(song["url"])
