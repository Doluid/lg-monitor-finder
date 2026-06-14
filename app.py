import streamlit as st

st.set_page_config(page_title="LG Product Finder Portal", page_icon="LG", layout="wide")

st.title("LG Electronics Product Finder 🇩🇪")
st.markdown("### 환영합니다! 어떤 제품을 찾고 계신가요?")
st.divider()

st.write("좌측 사이드바(Sidebar)의 메뉴를 클릭하거나, 아래 안내를 확인하여 자신에게 딱 맞는 제품을 찾아보세요.")
st.write("<br>", unsafe_allow_html=True)

# 첫 번째 줄: 모니터, 노트북, TV
col1, col2, col3 = st.columns(3)
with col1:
    st.info("🖥️ **Monitor Finder**\n\n당신의 책상 위를 완성할 완벽한 디스플레이를 찾습니다.")
with col2:
    st.success("💻 **Gram Finder**\n\n가벼움 그 이상, 당신의 일상과 함께할 랩탑을 찾습니다.")
with col3:
    st.warning("📺 **OLED TV Finder**\n\n차원이 다른 블랙, 당신의 거실을 완성할 완벽한 OLED TV를 찾습니다.")

st.write("<br>", unsafe_allow_html=True)

# 두 번째 줄: 냉장고, 세탁기
col4, col5, col6 = st.columns(3)
with col4:
    st.error("🧊 **Kühlschrank Finder**\n\n주방의 품격을 높이는 당신만의 완벽한 LG 냉장고를 찾습니다.")
with col5:
    st.info("🧺 **Waschmaschinen Finder**\n\n에너지 절약부터 완벽한 옷감 케어까지, 세탁 라이프를 바꿀 세탁기를 찾습니다.")
with col6:
    # 5개이므로 마지막 칸은 비워두어 여백의 미를 살립니다.
    st.empty() 

st.write("<br><br><br><br>", unsafe_allow_html=True)
st.caption("© 2026 LG Electronics Prototype. Built with Streamlit.")
