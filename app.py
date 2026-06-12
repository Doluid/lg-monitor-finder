import streamlit as st

st.set_page_config(page_title="LG Product Finder Portal", page_icon="LG", layout="centered")

st.title("LG Electronics Product Finder 🇩🇪")
st.markdown("### 환영합니다! 어떤 제품을 찾고 계신가요?")
st.divider()

st.write("좌측 사이드바(Sidebar)의 메뉴를 클릭하여 자신에게 딱 맞는 제품을 찾아보세요.")

col1, col2 = st.columns(2)
with col1:
    st.info("🖥️ **Monitor Finder**\n\n당신의 책상 위를 완성할 완벽한 디스플레이를 찾습니다.")
with col2:
    st.success("💻 **Gram Finder**\n\n가벼움 그 이상, 당신의 일상과 함께할 랩탑을 찾습니다.")

st.write("<br><br><br>", unsafe_allow_html=True)
st.caption("© 2026 LG Electronics Prototype. Built with Streamlit.")
