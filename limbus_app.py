import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="림버스 컴퍼니 도감",
    page_icon="🚌",
    layout="wide"
)

# 림버스 컴퍼니 수감자 데이터베이스 (관련 인물, 관계, 대사 추가)
sinners_data = {
    "이상 (Yi Sang)": {
        "number": "No. 1",
        "literature": "이상, 《날개》",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Yi_Sang_signature.svg", # 예시 이미지 (실제 로컬 파일 경로로 교체 가능)
        "description": "림버스 컴퍼니의 1번 수감자. 말수가 적고 난해한 표현을 자주 쓰지만, 뛰어난 지적 능력을 지니고 있습니다.",
        "related_figures": ["파우스트 (지적 교류)", "단테 (관리자)"],
        "relationships": "파우스트와는 주로 거울 기술이나 과학적 지식을 논하는 동료 관계입니다. 다른 수감자들의 기행에 대체로 무관심한 듯하면서도 깊이 관찰합니다.",
        "quotes": [
            "알 수 없는 일이지요. 어째서 날개는 돋아났던 것일까오.",
            "…안개 걷힐 날이 오기는 하는 것일까."
        ],
        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" # 예시 오디오 (캐릭터별 테마곡 링크로 교체)
    },
    "파우스트 (Faust)": {
        "number": "No. 2",
        "literature": "요한 볼프강 폰 괴테, 《파우스트》",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Wikisource-logo.svg",
        "description": "자신이 모든 것을 알고 있다고 주장하는 천재 수감자. 회사의 기밀이나 기술적 사안에 깊게 관여하고 있습니다.",
        "related_figures": ["이상 (학술적 대화)", "베르길리우스 (안내자)"],
        "relationships": "회사의 방침을 대변하며 수감자들 위에서 통제력을 행사하려 합니다. 이상과는 서로의 지식을 인정하는 유일한 파트너입니다.",
        "quotes": [
            "파우스트는 모든 것을 알고 있습니다.",
            "이것이 가장 최선의 선택이에요."
        ],
        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
    },
    "돈키호테 (Don Quixote)": {
        "number": "No. 3",
        "literature": "미겔 데 세르반테스, 《돈 키호테》",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Wikisource-logo.svg",
        "description": "정의로운 해결사를 광적으로 동경하는 분위기 메이커. 언제나 과도하게 들떠 있으며 황당한 정의감을 품고 있습니다.",
        "related_figures": ["로쟈 (주로 함께 엮이는 장난꾸러기 조합)", "로시난테 (애마/구속구)"],
        "relationships": "모든 수감자들에게 형제자매 같은 친근함을 보이지만, 가끔 그 지나친 열정 때문에 주변을 피곤하게 만듭니다.",
        "quotes": [
            "정의의 해결사, 돈키호테 납시오!",
            "라만차의 영웅에게 불가능이란 없느니라!"
        ],
        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
    }
    # 필요에 따라 다른 수감자 데이터(오티스, 히스클리프, 이스마엘 등)를 이 형식으로 추가하세요!
}

# 사이드바 메뉴 설정
st.sidebar.title("🚌 LIMBUS COMPANY")
st.sidebar.markdown("관리자님, 안내할 수감자를 선택해 주세요.")

selected_sinner_name = st.sidebar.selectbox(
    "수감자 선택", 
    list(sinners_data.keys()),
    key="sinner_selectbox" # 위젯 키를 부여하여 상태 꼬임 방지
)

# 선택된 데이터 가져오기
data = sinners_data[selected_sinner_name]

# 메인 화면 구성
st.title(f"림버스 컴퍼니 수감자 파일: {selected_sinner_name}")
st.markdown(f"**{data['number']}** | *모티브 원작: {data['literature']}*")
st.divider()

# 2열 레이아웃 (좌: 이미지 및 기본 정보, 우: 관계 및 대사)
col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("인물 프로필")
    # 이미지 출력 (URL 또는 로컬 경로)
    try:
        st.image(data["image"], caption=selected_sinner_name, use_container_width=True)
    except Exception:
        st.warning("이미지를 불러올 수 없습니다. 경로를 확인해주세요.")
    
    st.markdown(f"**개요:** {data['description']}")
    
    # 음악 재생 (캐릭터별 고유 오디오)
    st.markdown("### 🎵 캐릭터 테마곡")
    st.audio(data["audio_url"], format="audio/mp3")

with col2:
    st.subheader("🤝 관련 인물 및 관계")
    st.markdown(f"**주요 관련 인물:** {', '.join(data['related_figures'])}")
    st.info(data["relationships"])
    
    st.subheader("💬 주요 대사")
    for quote in data["quotes"]:
        st.markdown(f"> *\"{quote}\"*\n")

# 하단 부가 정보
st.divider()
st.caption("Limbus Company Executive Manager Assistance System v1.0")
