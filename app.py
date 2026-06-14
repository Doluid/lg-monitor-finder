import streamlit as st

st.set_page_config(page_title="LG Product Finder Portal", page_icon="LG", layout="wide")

# 대형 클릭 카드를 만들기 위한 커스텀 CSS
st.markdown("""
<style>
.stApp { background-color: #f6f3eb; }
/* 버튼을 거대한 카드 형태로 만듭니다 */
div.stButton > button {
    width: 100%;
    height: 160px;
    font-size: 18px !important;
    font-weight: 600;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #ffffff;
    border: 2px solid #e5e5e5;
    border-radius: 12px;
    color: #333;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    white-space: pre-wrap; /* 줄바꿈 허용 */
}
/* 마우스를 올렸을 때 애니메이션 효과 */
div.stButton > button:hover {
    border-color: #ea1917;
    color: #ea1917;
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(234, 25, 23, 0.15);
}
</style>
""", unsafe_allow_html=True)

st.title("LG Electronics Product Finder 🇩🇪")
st.markdown("### 환영합니다! 어떤 제품을 찾고 계신가요?")
st.divider()

st.write("아래의 원하시는 제품군 카드를 **클릭**하시면 해당 파인더로 바로 이동합니다.")
st.write("<br>", unsafe_allow_html=True)

# 첫 번째 줄: 모니터, 노트북, TV
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🖥️ Monitor Finder\n\n완벽한 디스플레이 찾기"):
        st.switch_page("pages/1_🖥️_Monitor.py")
with col2:
    if st.button("💻 Gram Finder\n\n나의 일상과 함께할 랩탑 찾기"):
        st.switch_page("pages/2_💻_Gram.py")
with col3:
    if st.button("📺 OLED TV Finder\n\n거실을 완성할 완벽한 TV 찾기"):
        st.switch_page("pages/3_📺_OLED_TV.py")

st.write("<br>", unsafe_allow_html=True)

# 두 번째 줄: 냉장고, 세탁기
col4, col5, col6 = st.columns(3)
with col4:
    if st.button("🧊 Kühlschrank Finder\n\n주방의 품격을 높일 냉장고 찾기"):
        st.switch_page("pages/4_🧊_Refrigerator.py")
with col5:
    if st.button("🧺 Waschmaschinen Finder\n\n세탁 라이프를 바꿀 세탁기 찾기"):
        st.switch_page("pages/5_🧺_Washing_Machine.py")
with col6:
    st.empty() # 여백 유지

st.write("<br><br><br><br>", unsafe_allow_html=True)
st.caption("© 2026 LG Electronics Prototype. Built with Streamlit.")
