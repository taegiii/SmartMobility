import streamlit as st

def bmi_range(bmi) :
    if  bmi <= 18.5 :
        st.info("저체중 입니다!")
    elif bmi <= 23 :
        st.success("정상 입니다!")
    elif bmi <= 25 :
        st.warning("과체중 입니다!")
    elif bmi > 25 :
        st.warning("비만 입니다!")
    else :
        st.error("키 또는 몸무게를 잘못 입력하셨습니다.")