import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import myfunc as my

st.session_state.id = "진유택"
st.write(f'{st.session_state.id}님 안녕하세요')

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
        my.bmi_range(bmi)
        
    st.image('5334759.jpg', caption="건강한 삶")

if selected == '갭마인더' :
    st.title("갭마인더")

    data = pd.read_csv("gapminder.csv")

    year = st.slider("년도", 1952, 2007, 1970, step=5)
    
    
    data = data[data['year'] == year]

    st.write(data)

    fig, ax = plt.subplots()
    
    country = data['continent']

    colors=[]
    for x in country :
        if x == 'Africa' :
            colors.append("royalblue")
        elif x == 'Americas' :
            colors.append('green')
        elif x == 'Asia' :
            colors.append('tomato')
        elif x == 'Europe' :
            colors.append('orange')
        else :
            colors.append('purple')
        

    ax.scatter(data['gdpPercap'], data['lifeExp'], s=data['pop']*0.000002, color=colors)

    st.pyplot(fig)


if selected == '국가별 통계' :
    st.title("국가별 통계")

    df = pd.read_csv('gapminder.csv')

    list = df['country'].unique()

    options = st.multiselect(
    "국가를 선택하십시오.",
    list,
    ["Korea, Rep."])

    fig, ax = plt.subplots()
    for country in options :
        data = df[df['country']==country]
        ax.plot(data['year'], data['gdpPercap'])
    ax.legend()
    ax.set_title('gdpPercap')

    st.pyplot(fig)

    fig1, ax1 = plt.subplots()

    for country in options :
        data = df[df['country']==country]
        ax1.plot(data['year'], data['lifeExp'])
    ax1.legend()
    ax1.set_title('lifeExp')

    st.pyplot(fig1)

    