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

selected = st.sidebar.selectbox("목차", ("체질량지수 계산기", "갭마인더", "국가별 통계"))

if selected == "체질량지수 계산기" : 
    st.title("체질량지수 계산기")

    st.info("체질량지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다.")

    height = st.number_input("키(cm)", value=160, step=1)
    st.write("당신의 신장은: ", height)

    weight = st.number_input("몸무게(kg)", value=60, step=1)
    st.write("당신의 몸무게는: ", weight)

    if st.button("계산", type="primary", disabled=False) :
        bmi = weight / ((height/100)**2) if weight != 0 and height != 0 else 0
        st.write(f"당신의 체질량지수는 {bmi:.2f}입니다.")
        bmi_range(bmi)
        
    st.image('5334759.jpg', caption="건강한 삶")

if selected == '갭마인더' :
    st.title("갭마인더")




if selected == '국가별 통계' :
    st.title("국가별 통계")