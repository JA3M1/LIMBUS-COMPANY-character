import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="Limbus Company Archive",
    page_icon="⏱️",
    layout="wide",
)

# 2. 림버스 컴퍼니 12인 수감자 및 단테 데이터 정의 (상세 정보 확장)
CHARACTER_DATA = {
    "단테 (Dante)": {
        "color": "#FFD700",
        "symbol": "⏰",
        "number": "관리자",
        "gender": "불명",
        "birthday": "불명",
        "equipment": "황금 시계 (머리)",
        "skills": "• 수감자 부활 및 고통 공유 능력",
        "bg_image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/FFD700?text=Dante",
        "personality": "기억을 잃었으나 따뜻하고 책임감 있는 성격. 수감자들의 폭력적인 성향 사이에서 고뇌하며 중재하는 리더십을 보입니다.",
        "related_figure": "단테 알리기에리 (신곡의 저자) / 수감자 전원",
        "songs": "• Limbus Company - 'In Hell We Live, Lament'\n• 단테 테마 배경 음악 (OST)",
        "description": "림버스 컴퍼니의 관리자. 머리가 황금 시계로 되어 있으며, 수감자들을 부활시키는 능력을 가졌다.",
    },
    "이상 (Yi Sang)": {
        "color": "#A0C4FF",
        "symbol": "🪞",
        "number": "No. 01",
        "gender": "남성",
        "birthday": "1월 13일",
        "equipment": "거울 연관 장치 / 관통 무기",
        "skills": "• 제 4계시록 에고 (흉탄 등)\n• 분홍신 및 거울 파편 응용 기술",
        "bg_image": "https://images.unsplash.com/photo-1518495973542-4542c06a5843?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/A0C4FF?text=Yi+Sang",
        "personality": "염세적이고 말수가 적으며 난해한 표현을 즐겨 씁니다. 내면에 깊은 통찰력과 예술가적 고뇌가 숨어 있습니다.",
        "related_figure": "이상 (한국 소설가/시인) / 파우스트, 파계 연구원들",
        "songs": "• 이상 챕터 대표 OST 및 에고 테마",
        "description": "말수가 적고 난해한 말을 자주 하는 천재 전(前) N사 연구원. 거울 기술과 깊은 연관이 있다.",
    },
    "파우스트 (Faust)": {
        "color": "#70C1B3",
        "symbol": "🧪",
        "number": "No. 02",
        "gender": "여성",
        "birthday": "5월 14일",
        "equipment": "N사 기술 응용 장비 / 타격 및 참격 무기",
        "skills": "• 타히트 에고 발현\n• 천재적 지식을 통한 전술 분석",
        "bg_image": "https://images.unsplash.com/photo-1507668077129-56e32842fceb?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/70C1B3?text=Faust",
        "personality": "오만할 정도로 모든 것을 다 안다는 태도를 보이며, 감정보다는 철저한 이성과 논리에 따라 행동합니다.",
        "related_figure": "파우스트 (괴테의 희곡) / 림버스 컴퍼니 창립 멤버",
        "songs": "• 파우스트 캐릭터 성우 인게임 보이스 및 테마",
        "description": "자신이 모든 것을 알고 있다고 말하는 천재 수감자. 림버스 컴퍼니의 기술적 기반을 혼자서 이해하고 있다.",
    },
    "돈키호테 (Don Quixote)": {
        "color": "#FFE156",
        "symbol": "🗡️",
        "number": "No. 03",
        "gender": "여성",
        "birthday": "4월 23일",
        "equipment": "란스 형태의 창형 무기 / 정의의 해결사 장비",
        "skills": "• 라신 에고 및 돌격형 참격 스킬\n• 혈귀 관련 잠재력 (스포일러 주의)",
        "bg_image": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/FFE156?text=Don+Quixote",
        "personality": "정의와 해결사에 대한 맹목적인 동경으로 가득 차 있으며, 언제나 시끄럽고 엉뚱한 행동으로 주변을 놀라게 합니다.",
        "related_figure": "돈 키호테 (세르반테스 소설) / 로시반테",
        "songs": "• 돈키호테 환호 및 전투 테마",
        "description": "정의로운 해결사를 열렬히 동경하는 과격하고 시끄러운 수감자. 언제나 엉뚱한 열정에 차 있다.",
    },
    "료슈 (Ryoshu)": {
        "color": "#E76F51",
        "symbol": "🔪",
        "number": "No. 04",
        "gender": "여성",
        "birthday": "10월 28일",
        "equipment": "오래된 명도 형태의 참격 무기",
        "skills": "• 절단 및 광역 참격 에고\n• 예술적 집착을 담은 연계 공격",
        "bg_image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/E76F51?text=Ryoshu",
        "personality": "잔혹하고 폭력적인 행위를 '예술'로 포장하며, 극단적인 줄임말 사용과 마이웨이 성격을 지닙니다.",
        "related_figure": "아쿠타가와 류노스케 '지옥변' / 딸",
        "songs": "• 료슈 참격 및 처형 테마 멜로디",
        "description": "예술과 '표현'에 광적으로 집착하는 위험한 인물. 줄임말을 자주 쓰며 폭력을 예술로 여긴다.",
    },
    "뫼르소 (Meursault)": {
        "color": "#4A90E2",
        "symbol": "📐",
        "number": "No. 05",
        "gender": "남성",
        "birthday": "11월 12일",
        "equipment": "중장갑 타격형 대형 무기",
        "skills": "• 타히트 및 타격 연계 방어 기술\n• 고위력 반격 및 제압 스킬",
        "bg_image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/4A90E2?text=Meursault",
        "personality": "감정이 거의 느껴지지 않으며, 불필요한 사유를 거부하고 오직 주어진 명령어와 효율성에만 반응합니다.",
        "related_figure": "알베르 카뮈 '이방인' / N사 관련 인물",
        "songs": "• 뫼르소 중저음 보이스 및 전투 음악",
        "description": "지시받은 사항 외에는 스스로 생각하지 않고 철저히 명령에만 복종하는 효율성의 화신.",
    },
    "홍루 (Hong Lu)": {
        "color": "#81B29A",
        "symbol": "🪷",
        "number": "No. 06",
        "gender": "남성",
        "birthday": "7월 12일",
        "equipment": "독특한 디자인의 참격/관통 무기",
        "skills": "• 림버스 컴퍼니 표준 에고 활용\n• 회피 및 디버프 해제 기술",
        "bg_image": "https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/81B29A?text=Hong+Lu",
        "personality": "재벌가 도련님 특유의 해맑음과 잔인한 현실에 대한 무감각함이 공존하는 독특한 성격을 지닙니다.",
        "related_figure": "조설근 '홍루몽' (가보옥 모티브) / 가문의 인물들",
        "songs": "• 홍루 우아하고 나긋한 분위기의 OST",
        "description": "부유한 가문 출신으로 세상 물정에 다소 어둡지만, 언제나 나긋나긋하고 해맑은 태도를 유지한다.",
    },
    "히스클리프 (Heathcliff)": {
        "color": "#3D5A80",
        "symbol": "🏏",
        "number": "No. 07",
        "gender": "남성",
        "birthday": "2월 28일",
        "equipment": "야구 배트형 타격 무기",
        "skills": "• 광란의 난타 및 복수심 기반 타격기\n• 에고 '마탄' 등 강력한 딜링",
        "bg_image": "https://images.unsplash.com/photo-1519501025264-65ba15a82390?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/3D5A80?text=Heathcliff",
        "personality": "쉽게 분노하고 거친 욕설과 폭력을 일삼지만, 그 이면에는 깊은 애정과 버림받은 상처가 자리하고 있습니다.",
        "related_figure": "에밀리 브론테 '폭풍의 언덕' / 캐서린",
        "songs": "• 히스클리프 폭발적인 챕터 전투 곡 ('Passung' 등)",
        "description": "다혈질이고 거친 폭력을 서슴지 않는 복수심에 찬 수감자. 배트형 무기로 적을 타격한다.",
    },
    "이스마엘 (Ishmael)": {
        "color": "#F4A261",
        "symbol": "⚓",
        "number": "No. 08",
        "gender": "여성",
        "birthday": "9월 8일",
        "equipment": "작살형 관통 무기",
        "skills": "• 파도 및 항해술 연계 관통/참격기\n• 고위력 에고 스킬",
        "bg_image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/F4A261?text=Ishmael",
        "personality": "상식적이고 현실적이라 동료들의 뻘짓에 가장 많이 분노하는 '태클 담당'. 집념과 복수심이 강합니다.",
        "related_figure": "허먼 맨빌 '모비 딕' (피쿼드 호 선원들)",
        "songs": "• 이스마엘 챕터 메인 테마 ('AHA' 등)",
        "description": "수감자들 중 드물게 상식적이고 이성적인 항해사 출신. 바다와 관련된 트라우마가 있다.",
    },
    "로쟈 (Rodion)": {
        "color": "#D90429",
        "symbol": "🎲",
        "number": "No. 09",
        "gender": "여성",
        "birthday": "3월 3일",
        "equipment": "도끼 형태의 타격/참격 무기",
        "skills": "• 광역 타격 에고 ('로쟈 식' 일격)\n• 체력 흡수 및 강화 스킬",
        "bg_image": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/D90429?text=Rodion",
        "personality": "털털하고 언니 같은 성격으로 도박과 요행을 즐기지만, 마음 한켠엔 과거의 무거운 죄책감을 누르고 있습니다.",
        "related_figure": "도스토옙스키 '죄와 벌' (소냐 등)",
        "songs": "• 로쟈 경쾌하고 꿍꿍이 있는 느낌의 OST",
        "description": "도박과 돈을 좋아하며 낙천적이지만, 과거의 어두운 죄책감을 마음 속 깊이 품고 있는 수감자.",
    },
    "싱클레어 (Sinclair)": {
        "color": "#B5838D",
        "symbol": "⚙️",
        "number": "No. 10",
        "gender": "남성",
        "birthday": "6월 6일",
        "equipment": "톱날 및 미늘창 형태의 무기",
        "skills": "• 분노 각성형 참격 연계기\n• 크로머 및 N사 연계 스킬",
        "bg_image": "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/Sinclair",
        "personality": "유약하고 겁이 많으나 순수한 소년. 하지만 주변 환경이나 트라우마에 의해 잔혹하게 각성하는 입체적 성격입니다.",
        "related_figure": "헤르만 헤세 '데미안' (데미안, 크로머)",
        "songs": "• 싱클레어 불안한 심리를 담은 BGM",
        "description": "겁이 많고 여린 소년이지만, 극한의 상황에서는 잔혹한 면모가 고개를 드는 수감자.",
    },
    "오티스 (Outis)": {
        "color": "#606C38",
        "symbol": "🛡️",
        "number": "No. 11",
        "gender": "여성",
        "birthday": "12월 25일",
        "equipment": "검과 전술 장비 세트",
        "skills": "• 전술 지휘 및 집중 포화 스킬\n• 강력한 방어 및 카운터 공격",
        "bg_image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/Outis",
        "personality": "탁월한 전술 감각을 가졌으며 관리자 단테 앞에서는 아첨에 가까울 정도로 충성을 다하는 처세술의 달인.",
        "related_figure": "호메로스 '오디세이아' (오디세우스)",
        "songs": "• 오티스 군가풍 및 전술적 느낌의 테마",
        "description": "뛰어난 전술안을 가진 베테랑 군인 출신. 관리자 단테에게 과도할 정도로 충성을 표명한다.",
    },
    "그레고르 (Gregor)": {
        "color": "#9A8C98",
        "symbol": "🪲",
        "number": "No. 12",
        "gender": "남성",
        "birthday": "8월 14일",
        "equipment": "변이된 벌레 팔 (의수형 무기)",
        "skills": "• 벌레 팔 난타 및 절단 스킬\n• 재생 및 참호전 특화 방어",
        "bg_image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1920",
        "char_image": "https://via.placeholder.com/300x400/222/Gregor",
        "personality": "전직 군인답게 현실적이고 피곤해하는 '동네 아저씨' 재질이지만, 동료들을 뒤에서 묵묵히 챙겨주는 따뜻함이 있습니다.",
        "related_figure": "프란츠 카프카 '변신' (그레고르 잠자) / 어머니",
        "songs": "• 그레고르 묵직한 베이스의 전투 OST",
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
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), url("{current_bg}");
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

# 5. 메인 레이아웃 타이틀
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
        # 대표 문양과 상징색 적용된 이름
        st.markdown(
            f"<h1 style='font-size: 80px; text-align: center; margin-bottom: 0;'>{data['symbol']}</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<h2 class='limbus-title' style='text-align: center;'>{char_name}</h2>",
            unsafe_allow_html=True,
        )
        
        try:
            st.image(data["char_image"], use_container_width=True)
        except Exception:
            st.error("이미지를 불러오는 데 실패했습니다. 경로를 확인해주세요.")

    with c2:
        # 상징색 테두리 및 정보 박스
        st.markdown(
            f"""
            <div style="background-color: rgba(20, 20, 20, 0.92); padding: 25px; border-left: 6px solid {data['color']}; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        # 각 섹션별 상징색 적용 출력
        st.markdown(f"<h3 style='color: {data['color']}; margin-top:0;'>📂 수감자 기본 프로필</h3>", unsafe_allow_html=True)
        st.write(f"• **번호 / 직급:** {data['number']}")
        st.write(f"• **성별:** {data['gender']} | **생일:** {data['birthday']}")
        st.write(f"• **주요 장비:** {data['equipment']}")
        st.write(f"• **설명:** {data['description']}")
        
        st.markdown(f"<h3 style='color: {data['color']};'>⚔️ 전투 스킬 및 능력</h3>", unsafe_allow_html=True)
        st.markdown(data['skills'])
        
        st.markdown(f"<h3 style='color: {data['color']};'>💡 성격 및 특징</h3>", unsafe_allow_html=True)
        st.write(data['personality'])
        
        st.markdown(f"<h3 style='color: {data['color']};'>👤 원작 및 관련 인물</h3>", unsafe_allow_html=True)
        st.write(data['related_figure'])
        
        st.markdown(f"<h3 style='color: {data['color']};'>🎵 대표 테마 / 관련 음악</h3>", unsafe_allow_html=True)
        st.markdown(data['songs'])
        
        st.markdown("---")
        st.caption("LCB BUS SYSTEM // ACCESS GRANTED")

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
