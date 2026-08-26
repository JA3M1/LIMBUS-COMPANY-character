import time
import streamlit as st

# 1. 페이지 설정 (와이드 모드 및 림버스 풍 타이틀)
st.set_page_config(
    page_title="🚌 림버스 컴퍼니 관리자 터미널 ⏱️",
    page_icon="🩸",
    layout="wide",
)

# 2. 림버스 컴퍼니 다크 디스토피아 스타일 CSS (철창, 톱니바퀴, 붉은색/금색 포인트)
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #0f0f12 0%, #1a1b22 100%);
        color: #f3f0df;
    }
    .stButton>button {
        background: linear-gradient(45deg, #8B0000, #B22222);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 8px;
        padding: 15px 30px;
        border: 2px solid #C5A059;
        box-shadow: 0px 0px 15px rgba(139, 0, 0, 0.6);
        transition: 0.3s;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button:hover {
        transform: scale(1.03);
        background: linear-gradient(45deg, #B22222, #FF0000);
        box-shadow: 0px 0px 25px rgba(255, 0, 0, 0.8);
    }
    .limbus-card {
        background-color: #1e1f24;
        border: 2px solid #C5A059;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        margin-bottom: 20px;
    }
    .terminal-text {
        font-family: 'Courier New', Courier, monospace;
        color: #00FF66;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. 림버스 컴퍼니 12인 수감자 + 단테 데이터베이스 (고증 및 이모지 폭탄 💥)
limbus_data = {
    "이상 (Yi Sang)": {
        "num": "No. 1",
        "title": "📜 거울을 보는 자 / 초현실주의 사색가",
        "emoji": "🪞☁️✒️",
        "novel": "이상 <날개>",
        "ego": "파열 / 수면 / 관측자 (E.G.O: 여우비 🌧️ / 바다선택 🌊)",
        "quote": "“가장 눈부신 날개는 가장 무거운 고통 속에서 피어나는 법이오.”",
        "desc": "말수가 적고 항상 허공을 응시하며 난해한 말만 늘어놓는 수감자. 하지만 그의 천재적인 지능과 거울 기술에 대한 통찰은 메피스토펠레스의 핵심 무기입니다.",
        "stats": "통찰력: SSS | 전투력: A | 대화 빈도: 하(下)",
    },
    "파우스트 (Faust)": {
        "num": "No. 2",
        "title": "🧪 모든 것을 아는 천재 과학자",
        "emoji": "🔬🧬📘",
        "novel": "괴테 <파우스트>",
        "ego": "오만 / 분광 / 지식의 파편 (E.G.O: 표상방출기 ⚡)",
        "quote": "“파우스트는 모든 것을 알고 있습니다. 그리고 그 답은 이미 정해져 있지요.”",
        "desc": "자신이 세상에서 가장 지혜롭다고 믿는 오만한 천재. L사 기술의 정수를 다루며, 언제나 단테의 든든한(혹은 기계적인) 조력자가 되어줍니다.",
        "stats": "지능: ∞ | 오만함: MAX | 효율성: SSS",
    },
    "돈키호테 (Don Quixote)": {
        "num": "No. 3",
        "title": "🎠 정의의 영웅을 꿈꾸는 열혈 광신도",
        "emoji": "⚡🛡️🐎",
        "novel": "세르반테스 <돈 키호테>",
        "ego": "질투 / 관통 / 정의의 사도 (E.G.O: 라 마낭차의 핏빛 창 🩸)",
        "quote": "“정의는 승리하며! 우리들은 위대한 림버스 컴퍼니의 수감자이다아아!”",
        "desc": "픽시브와 망상에 가득 차 날뛰는 트러블메이커. Fixer(해결사)를 광적으로 동경하며, 언제나 사고를 치지만 누구보다 뜨거운 심장을 가졌습니다.",
        "stats": "열정: MAX | 사고유발: SSS | 텐션: 음속 돌파",
    },
    "료슈 (Ryoshu)": {
        "num": "No. 4",
        "title": "🗡️ 예술과 도륙을 사랑하는 화가",
        "emoji": "🎨🔥💀",
        "novel": "아쿠타가와 류노스케 <지옥변>",
        "ego": "색욕 / 참격 / 잔혹한 예술 (E.G.O: 적안 🔴 / 4.M.P)",
        "quote": "“H. F. (한 치의 오차도 없는 잔혹한 도륙의 예술). 불만인가?”",
        "desc": "항상 담배를 물고 다니며 눈에 보이는 모든 것을 '예술'이라는 명목 아래 토막 내고 싶어 하는 위험한 여성. 줄임말을 즐겨 씁니다.",
        "stats": "잔혹함: SSS | 예술혼: MAX | 흡연량: 헤비",
    },
    "표도르 / 뫼르소 (Meursault)": {
        "num": "No. 5",
        "title": "📏 감정을 상실한 철벽의 집행관",
        "emoji": "⚖️🗿⚙️",
        "novel": "알베르 카뮈 <이방인>",
        "ego": "우울 / 타격 / 절대적 규율 (E.G.O: 집행 🔨 / 전면다각도 릴레이)",
        "quote": "“관리자님, 명령을 내리십시오. 그 이상은 불필요한 사유입니다.”",
        "desc": "태양빛이 눈부셔서 살인을 저질렀다는 전설을 가진, 감정과 자아가 거의 없는 거구의 사나이. 지시에 오차 없이 복종합니다.",
        "stats": "근력: SSS | 감정표현: 0% | 신뢰도: 100%",
    },
    "홍루 (Hong Lu)": {
        "num": "No. 6",
        "title": "🌸 세상 물정 모르는 귀공자",
        "emoji": "🪷💎🍵",
        "novel": "조설근 <홍루몽>",
        "ego": "색욕 / 참격 / 유유자적 (E.G.O: 홍염살 🔥)",
        "quote": "“어머, 저기에 흐르는 피는 참 예쁜 색이네요~ 신기라라!”",
        "desc": "엄청난 부잣집 도련님이지만 세상 물정에 전혀 관심이 없고, 심각한 상황에서도 천진난만한 소리를 해 동료들을 아연실색하게 만듭니다.",
        "stats": "재력: ∞ | 해맑음: MAX | 눈치: -100",
    },
    "히스클리프 (Heathcliff)": {
        "num": "No. 7",
        "title": "🦇 분노로 가득 찬 폭주기관차",
        "emoji": "🏏💢⛓️",
        "novel": "에밀리 브론테 <폭풍의 언덕>",
        "ego": "분노 / 타격 / 폭풍의 복수 (E.G.O: 구속 🔗 / 시체수의 🥼)",
        "quote": "“이 새끼들 다 죽여버리겠어! 내 성질머리 건들지 마라!”",
        "desc": "입에 거친 욕을 달고 살며 언제나 폭발 직전인 다혈질 수감자. 슬픈 과거와 복수심을 품고 있으며 야구 방망이를 주 무기로 씁니다.",
        "stats": "분노: MAX | 방망이질: SSS | 입담: 거침없음",
    },
    "이스마엘 (Ishmael)": {
        "num": "No. 8",
        "title": "⚓ 바다를 저주하는 노련한 항해사",
        "emoji": "🌊🐋🧭",
        "novel": "허먼 멜빌 <모비 딕>",
        "ego": "탐식 / 관통 / 심해의 공포 (E.G.O: 홍적화 🔴 / 맹목 ⚡)",
        "quote": "“제발 제정신 좀 차려요! 우리 이러다간 정말 다 죽는다고요!”",
        "desc": "광기 어린 수감자들 사이에서 유일하게 정상인 코스프레를 시도하지만, 고래(바다) 이야기만 나오면 눈이 돌변하는 불쌍한 항해사.",
        "stats": "정상인(인척): 상 | 스트레스: 99% | 작살술: SSS",
    },
    "로쟈 (Rodion)": {
        "num": "No. 9",
        "title": "🪓 여유 넘치는 도박사의 미소",
        "emoji": "🎰🧥💸",
        "novel": "도스토예프스키 <죄와 벌>",
        "ego": "탐식 / 타격 / 도박사의 잭팟 (E.G.O: 4번째 일치 🎲)",
        "quote": "“에이, 설마 죽기야 하겠어? 인생은 한 방이야, 관리자 양반!”",
        "desc": "항상 여유롭고 쾌활하게 돈과 도박, 간식을 밝히는 누님 캐릭터. 과거의 무거운 죄책감을 가슴 깊이 숨기고 있습니다.",
        "stats": "도박중독: MAX | 넉살: SSS | 멘탈: 강철",
    },
    "싱클레어 (Sinclair)": {
        "num": "No. 10",
        "title": "⚡ 어둠에 눈뜬 소년의 날갯짓",
        "emoji": "🌱⚔️⚡",
        "novel": "헤르만 헤세 <데미안>",
        "ego": "오만 / 참격 / 크롬러의 그림자 (E.G.O: 피안개 🩸 / 살랑거림)",
        "quote": "“제, 제가 이런 짓을... 아니에요, 난 괴물이 아니야!”",
        "desc": "험난한 도시 생활에 적응하지 못한 소심하고 여린 소년. 하지만 전투가 시작되면 내면의 광기와 크롬러의 잔재가 눈을 뜹니다.",
        "stats": "순수함: 10% | 광기 각성: 90% | 성장 가능성: SSS",
    },
    "오티스 (Outis)": {
        "num": "No. 11",
        "title": "🧭 늙은 군인의 충성스러운 아첨꾼",
        "emoji": "🎖️⚔️📜",
        "novel": "호메로스 <오디세이아>",
        "ego": "우울 / 관통 / 군대의 지휘 (E.G.O: 시체수의 / 여우비)",
        "quote": "“오오, 위대하시고 자애로우신 우리 관리자 단테님이시여! 이 오티스, 목숨을 바치겠습니다!”",
        "desc": "전쟁 베테랑 출신으로 단테에게는 지극정성으로 아첨을 떨지만, 동료 수감자들에게는 피도 눈물도 없는 철혈의 부소대장.",
        "stats": "아첨: MAX | 전술 지휘: SSS | 군기: 엄격",
    },
    "그레고르 (Gregor)": {
        "num": "No. 12",
        "title": "🪳 벌레 팔을 가진 베테랑 용병",
        "emoji": "🪳🚬🪖",
        "novel": "프란츠 카프카 <변신>",
        "ego": "질투 / 타격 / 돌연변이의 분노 (E.G.O: 초롱 🏮 / AEDD)",
        "quote": "“아이고, 내 팔짝이야… 또 지옥 같은 연장 근무인가?”",
        "desc": "오른팔이 거대한 벌레의 집게발로 변이된 전직 연합군 용병. 피곤에 찌들어 있으며 늘 퇴직을 꿈꾸는 맏형 같은 존재입니다.",
        "stats": "피로도: MAX | 연민: 높음 | 벌레팔: 튼튼",
    },
}

# 4. 사이드바 - 관리자 터미널 메뉴
st.sidebar.markdown(
    "# 🚌 Limbus Terminal Menu ⚙️", unsafe_allow_html=True
)
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p class='terminal-text'>[SYSTEM] LCCB OS v2.14 Connected</p>",
    unsafe_allow_html=True,
)
selected_inmate = st.sidebar.selectbox(
    "👇 분석할 수감자를 선택하십시오", list(limbus_data.keys())
)
st.sidebar.markdown("---")
st.sidebar.info("💡 팁: 황금가지 채굴 전용 맞춤형 진단 시스템입니다. 🌟")

# 5. 메인 화면 구성 (림버스 테마)
st.markdown(
    "<h1 style='text-align: center; color: #FF3B30; font-family: Courier New;'>🔴 림버스 컴퍼니 수감자 심층 분석 시스템 ⚙️</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h4 style='text-align: center; color: #C5A059;'>‘단테, 버스를 출발시키겠습니다. 지령을 하단해 주십시오.’ 🚌⏳</h4>",
    unsafe_allow_html=True,
)
st.markdown("---")

# 6. 분석 실행 버튼
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    analyze_button = st.button("✨ 황금가지 공명 및 캐릭터 데이터 로드 🩸")

if analyze_button:
    # 톱니바퀴 회전 및 로딩 연출
    with st.spinner(
        "⚙️ 메피스토펠레스 엔진 가동 중... 수감자 데이터를 동기화하는 중입니다... ⏳"
    ):
        time.sleep(1.2)

    # 림버스풍 폭죽 대신 황금가지 공명 연출 (볼룬스 + 특수 알림)
    st.balloons()

    info = limbus_data[selected_inmate]

    # 결과 카드 출력
    st.markdown(
        f"""
        <div class="limbus-card">
            <h2 style='text-align: center; color: #F3F0DF;'>{info['emoji']} 수감자: <span style='color: #FF3B30;'>{selected_inmate}</span></h2>
            <h3 style='text-align: center; color: #C5A059;'>({info['num']} / {info['title']})</h3>
            <p style='text-align: center; color: #888;'>모티브 원작: <b>{info['novel']}</b></p>
            <hr style='border-color: #C5A059;'>
            <h4 style='color: #FF3B30;'>💬 대표 대사</h4>
            <p style='font-style: italic; color: #FFF; font-size: 20px; background-color: #121316; padding: 15px; border-left: 4px solid #FF3B30;'>{info['quote']}</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # 상세 정보 컬럼 배치
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown(
            f"""
            <div style='background-color: #1e1f24; border: 1px solid #333; padding: 20px; border-radius: 10px; height: 100%;'>
                <h3 style='color: #C5A059;'>🔍 심층 성향 리포트</h3>
                <p>{info['desc']}</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col_right:
        st.markdown(
            f"""
            <div style='background-color: #1e1f24; border: 1px solid #333; padding: 20px; border-radius: 10px; height: 100%;'>
                <h3 style='color: #C5A059;'>⚡ 전투 및 E.G.O 스펙</h3>
                <p><b>E.G.O 및 특성:</b> {info['ego']}</p>
                <hr style='border-color: #333;'>
                <p class='terminal-text'><b>[전투 지표]</b> {info['stats']}</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    # 하단 코칭 메시지
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #8B0000 0%, #330000 100%); padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #FF3B30;'>
            <h3 style='color: #FFF;'>🩸 관리자 지령 완료</h3>
            <p style='color: #F3F0DF; font-size: 16px;'>이 수감자의 뒤틀림을 막고 황금가지를 회수하세요. 지옥 끝까지 버스는 달립니다! 🚌💨</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

else:
    # 초기 안내 화면
    st.markdown(
        """
        <div style='text-align: center; padding: 60px;'>
            <h3>👈 왼쪽 사이드바 터미널에서 분석할 <b>수감자</b>를 선택하고 버튼을 누르십시오.</h3>
            <p style='font-size: 50px;'>🚌⚙️🩸🗝️🕰️</p>
            <p style='color: #C5A059; font-family: Courier New;'>[WAITING FOR MANAGER'S COMMAND...]</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

# 7. 푸터
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666; font-family: Courier New;'>✨ Limbus Company Terminal - All Rights Reserved by Project Moon 🚌</p>",
    unsafe_allow_html=True,
)
