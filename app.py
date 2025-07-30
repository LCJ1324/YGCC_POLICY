import streamlit as st
import time


def login_page():
    st.set_page_config(page_title="로그인", layout="centered")
    st.title("청년 주거지원 통합 서비스")

    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")
    _, col1, col2 = st.columns([0.76, 0.12, 0.14])
    if col1.button("로그인", use_container_width=True):
        if username == "test" and password == "1234":
            st.session_state.login = True
            st.session_state.page = "main"
            st.success("이계몽님 환영합니다.")
            time.sleep(1)
            st.rerun()
        else:
            st.error("아이디 또는 비밀번호가 잘못되었습니다.")
    col2.button("회원가입", use_container_width=True)


def main_page():
    st.set_page_config(page_title="메인 페이지", layout="centered")
    st.title("청년 주거지원 통합 서비스")
    st.subheader("출발을 위한 안정된 거처 🏠")
    st.write("**청년의 첫 출근을 주거로 응원합니다**")

    col1, col2 = st.columns(2)
    with col1:
        st.image("주거비.png", use_container_width=True)
        if st.button("주거비 지원 신청", use_container_width=True):
            st.session_state.page = "housing"
            st.rerun()

    with col2:
        st.image("주거연계.png", use_container_width=True)
        if st.button("단기 주거 연계", use_container_width=True):
            st.session_state.page = "short_term"
            st.rerun()

    col3, col4 = st.columns(2)
    with col3:
        if st.button("마이페이지", use_container_width=True):
            st.session_state.page = "mypage"
            st.rerun()
    with col4:
        if st.button("로그아웃", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()


def housing_page():
    st.set_page_config(page_title="주거비 지원 신청", layout="wide")
    st.title("주거비 지원 신청")
    st.subheader("월세의 2/3 지원 (최대 50만원)")
    tab1, tab2, tab3 = st.tabs(["지원 대상", "지원 조건", "지원 방식"])
    with tab1:
        st.write("**지원 대상**")
        st.markdown(
            "**만 19세 이상 34세 이하 청년** 중 새로운 근무지를 위해 주거지를 이전한 자"
        )
    with tab2:
        st.write("**지원 조건**")
        st.write("1개월 이상 근무한 청년")
        st.write("동일 기업 또는 동일 기간 내 중복 지원 불가")
        st.text("최대 3회 수혜")

    with tab3:
        st.write("**지원 방식**")
        st.text("모든 제출서류 검토 완료 후 개인 계좌로 직접 입금(본인 명의 계좌)")

    st.divider()

    with st.expander("**서류 업로드**"):
        col1, col2, col3, col4 = st.columns(4)
        col1.file_uploader("주민등록등본")
        col2.file_uploader("임대차계약서")
        col3.file_uploader("고용계약서")
        col4.file_uploader("급여 명세서")
    if st.button("뒤로"):
        st.session_state.page = "main"
        st.rerun()


def short_term_page():
    st.set_page_config(page_title="단기 주거 연계", layout="wide")
    st.title("단기 주거 연계")
    st.subheader("근무기간 1~6개월 청년 대상")
    tab1, tab2, tab3, tab4 = st.tabs(
        ["지원 대상", "지원 조건", "우선 선발 기준", "지원방법"]
    )
    with tab1:
        st.write("**지원 대상**")
        st.markdown(
            "**만 19세 이상 34세 이하 청년** 중"
            "\n"
            " 1. 인턴, 수습, 단기 계약직, 시범 채용 등 1~6개월 이내 근무 형태로 채용된 자"
            "\n"
            " 2. 곧 근무 예정이며, 기존 거주지에서 출퇴근이 어렵거나 불가능한 자"
        )
    with tab2:
        st.write("**지원 조건**")
        st.write("단기 근무계약(1~6개월)이 체결되어 있고, 실제 입주가 필요한 자")

    with tab3:
        st.write("**우선 선발 기준**")
        st.write(" 1순위 : 출퇴근 거리 순")
        st.write(" 2순위 : 경제적 취약계층")
        st.write(" 3순위 : 계약 기간이 짧은 순")

    with tab4:
        st.write("**지원방법**")
        st.text("근무지 주소 및 희망 거주 지역 입력")
        st.text("제출 서류 기반으로 선발된 인원에게 지원 확정")
        st.text("배정 주택은 지역별 위탁기관이 계약 및 관리")
        st.text(
            "임대료 일부 감면 또는 보증금 무이자 대출 등의 부가적 지원은 협약 기관 조건에 따라 적용"
        )
        st.text("매달 신청 가능")

    st.divider()

    col_location, col_select, col_money = st.columns(3)
    col_location.text_input(
        "근무지 주소", placeholder="예시) 서울특별시 강남구 테헤란로 123, 10층 1001호"
    )
    col_select.selectbox(
        "희망 지역",
        [
            "서울특별시",
            "부산광역시",
            "대구광역시",
            "인천광역시",
            "광주광역시",
            "대전광역시",
            "울산광역시",
            "세종특별자치시",
            "경기도",
            "강원특별자치도",
            "충청북도",
            "충청남도",
            "전북특별자치도",
            "전라남도",
            "경상북도",
            "경상남도",
            "제주특별자치도",
        ],
    )
    col_money.number_input("예산(만원)", 10, 200)

    with st.expander("**서류 업로드**"):
        col1, col2 = st.columns(2)
        col1.file_uploader("주민등록등본")
        col2.file_uploader("고용계약서")

    if st.button("뒤로"):
        st.session_state.page = "main"
        st.rerun()


def mypage():
    st.set_page_config(page_title="마이페이지", layout="centered")
    st.title("마이페이지")
    st.subheader("나의 신청내역")
    import pandas as pd

    df = pd.DataFrame(
        {
            "신청종류": ["주거비 지원", "단기 주거 연계"],
            "상태": ["심사중", "배정 완료"],
            "알림": ["서류 보완 요청", "배정 확정"],
        }
    )
    st.dataframe(df)
    st.divider()
    st.warning("⚠️ 주거비 지원 제출 서류 미비")
    if st.button("뒤로"):
        st.session_state.page = "main"
        st.rerun()


if "page" not in st.session_state:
    st.session_state.page = "login"

if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "main":
    main_page()
elif st.session_state.page == "housing":
    housing_page()
elif st.session_state.page == "short_term":
    short_term_page()
elif st.session_state.page == "mypage":
    mypage()
