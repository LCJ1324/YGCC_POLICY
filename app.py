import streamlit as st
import time

def login_page() :
    st.set_page_config(page_title="로그인", layout="centered")

    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")
    if st.button("로그인"):
        if username == "test" and password == "1234":
            st.session_state.login = True
            st.session_state.page = 'main'
            st.success("이계몽님 환영합니다.")
            time.sleep(2)
            st.rerun()
        else:
            st.error("아이디 또는 비밀번호가 잘못되었습니다.")

def main_page():
    st.set_page_config(page_title="메인 페이지", layout="centered")
    st.title("메인 페이지")
    st.subheader("서비스를 선택하세요.")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("주거비 지원"):
            st.session_state.page = "housing"
            st.rerun()
    with col2:
        if st.button("단기 주거 매칭"):
            st.session_state.page = "short_term"
            st.rerun()
    with col3:
        if st.button("마이페이지"):
            st.session_state.page = "mypage"
            st.rerun()
    with col4:
        if st.button("로그아웃"):
            st.session_state.page = "login"
            st.rerun()

def housing_page():
    st.set_page_config(page_title="주거비 지원 신청", layout="centered")
    st.title("주거비 지원 신청")
    st.write("월세의 2/3 지원 (최대 50만원)")
    st.file_uploader("주민등록등본")
    st.file_uploader("임대차계약서")
    st.file_uploader("월세 입금내역")
    if st.button("뒤로"):
        st.session_state.page = "main"
        st.rerun()

def short_term_page():
    st.set_page_config(page_title="단기 주거 매칭", layout="centered")
    st.title("단기 주거 매칭")
    st.write("근무기간 1~6개월 청년 대상")
    st.selectbox("희망 지역", ["서울", "경기", "부산"])
    st.number_input("예산(만원)", 10, 200)
    if st.button("뒤로"):
        st.session_state.page = "main"
        st.rerun()

def mypage():
    st.set_page_config(page_title="마이페이지", layout="centered")
    st.title("마이페이지")
    st.write("나의 신청내역 / 상태 / 알림")
    import pandas as pd
    df = pd.DataFrame({
        "신청종류": ["주거비 지원", "단기 주거 매칭"],
        "상태": ["심사중", "배정 완료"],
        "알림": ["서류 보완 요청", "배정 확정"]
    })
    st.dataframe(df)
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