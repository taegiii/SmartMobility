import streamlit as st

st.write('# Hi, Welcome My App!')

st.write('반갑습니다. 저의 웹에 오신것을 환영합니다.')

if st.button("Say Hello") :
    st.write("Why hello there")
else :
    st.write("Goodbye")

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

st.write("You selected:", option)

txt = st.text_area(
    "자기를 소개해보세요",
)

st.write("입력한 내용은: ", txt)

age = st.slider("나이를 선택하세요!", 0, 100,1)
st.write(f"저의 나이는 {age}입니다.")