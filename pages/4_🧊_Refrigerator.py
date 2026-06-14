import streamlit as st

def main():
    st.set_page_config(page_title="LG Refrigerator Finder", page_icon="🧊", layout="wide")

    # LG.com 스타일 CSS (동일 적용)
    st.markdown("""
    <style>
    .stApp { background-color: #f6f3eb; }
    div.stButton > button { width: 100%; height: 70px; font-size: 16px !important; font-weight: 500; text-align: left; justify-content: flex-start; padding-left: 20px; background-color: #ffffff; border: 2px solid #e5e5e5; border-radius: 8px; color: #333; transition: all 0.3s ease; margin-bottom: 5px; }
    div.stButton > button:hover { border-color: #ea1917; color: #ea1917; box-shadow: 0 4px 12px rgba(234, 25, 23, 0.1); }
    .lg-card { background-color: #ffffff; border-radius: 12px; padding: 24px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); display: flex; flex-direction: column; height: 100%; border: 1px solid #eaeaea; font-family: 'Arial', sans-serif; }
    .lg-tag-row { display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
    .lg-tag { font-size: 11px; font-weight: bold; padding: 4px 8px; border-radius: 4px; }
    .lg-tag-red { background-color: #ea1917; color: white; }
    .lg-tag-outline { border: 1px solid #ea1917; color: #ea1917; background-color: #fffafb; }
    .lg-title { font-size: 16px; font-weight: 600; line-height: 1.4; color: #000; margin-bottom: 4px; height: 44px; overflow: hidden; }
    .lg-model { font-size: 12px; color: #666; margin-bottom: 12px; }
    .lg-rating { color: #fabb05; font-size: 13px; margin-bottom: 16px; text-align: right;}
    .lg-img-box { text-align: center; padding: 10px 0; border-bottom: 1px solid #eee; margin-bottom: 16px; height: 200px; display: flex; align-items: center; justify-content: center; }
    .lg-img-box img { max-width: 100%; max-height: 180px; object-fit: contain; }
    .lg-price-box { margin-top: auto; }
    .lg-save-text { color: #ea1917; font-size: 12px; font-weight: bold; margin-bottom: 4px; }
    .lg-price { font-size: 22px; font-weight: bold; color: #000; }
    .lg-price-old { font-size: 14px; text-decoration: line-through; color: #888; margin-left: 8px; }
    .lg-btn-row { display: flex; gap: 10px; margin-top: 10px; }
    .lg-btn { flex: 1; text-align: center; padding: 12px 0; font-size: 14px; font-weight: bold; border-radius: 6px; cursor: pointer; text-decoration: none; transition: 0.2s; }
    .lg-btn-sec { background-color: white; border: 1px solid #ccc; color: #333; }
    .lg-btn-sec:hover { border-color: #000; }
    .lg-btn-pri { background-color: #e50000; border: 1px solid #e50000; color: white; }
    .lg-btn-pri:hover { background-color: #c40000; }
    </style>
    """, unsafe_allow_html=True)

    # 냉장고 전용 상태 관리 (ref_step, ref_data)
    if 'ref_step' not in st.session_state:
        st.session_state.ref_step = 1
        st.session_state.ref_data = {}

    st.write("<br>", unsafe_allow_html=True)
    st.title("🧊 LG Kühlschrank Finder")
    st.markdown("주방의 품격을 높이는 당신만의 완벽한 LG 냉장고를 찾아보세요.")
    st.divider()

    if st.session_state.ref_step > 1 and st.session_state.ref_step != 4:
        if st.button("⬅️ Zurück (이전)", key="back_btn_ref"):
            st.session_state.ref_step -= 1
            st.rerun()

    col_q, col_empty = st.columns([2, 1])
    
    with col_q:
        if st.session_state.ref_step == 1:
            st.subheader("1. 주로 몇 명이 함께 사용하는 주방인가요?")
            if st.button("👤 1~2인 가구 (공간 효율이 중요해요)"): st.session_state.ref_data['size'] = "소형"; st.session_state.ref_step = 2; st.rerun()
            if st.button("👨‍👩‍👦 3~4인 가구 (균형 잡힌 표준 용량이 필요해요)"): st.session_state.ref_data['size'] = "표준"; st.session_state.ref_step = 2; st.rerun()
            if st.button("👨‍👩‍👧‍👦 대가족 또는 요리 매니아 (최대 용량과 보관 공간이 필수)"): st.session_state.ref_data['size'] = "대형"; st.session_state.ref_step = 2; st.rerun()

        elif st.session_state.ref_step == 2:
            st.subheader("2. 가장 선호하는 냉장고 도어(문) 스타일은?")
            if st.button("🚪 넓게 열고 한눈에 보는 상냉장 하냉동 (French Door / 4도어)"): st.session_state.ref_data['style'] = "4도어"; st.session_state.ref_step = 3; st.rerun()
            if st.button("↕️ 좌우로 나뉘어 정리가 편리한 스타일 (Side-by-Side / 양문형)"): st.session_state.ref_data['style'] = "양문형"; st.session_state.ref_step = 3; st.rerun()
            if st.button("📏 주방 가구에 툭 튀어나오지 않는 일체형 (빌트인/키친핏)"): st.session_state.ref_data['style'] = "빌트인"; st.session_state.ref_step = 3; st.rerun()

        elif st.session_state.ref_step == 3:
            st.subheader("3. 냉장고에 꼭 있었으면 하는 LG만의 마법은?")
            if st.button("✊ 똑똑! 두 번 두드리면 안이 보이는 마법 (InstaView)"): st.session_state.ref_data['feature'] = "인스타뷰"; st.session_state.ref_step = 4; st.rerun()
            if st.button("🎨 기분에 따라 도어 색상을 바꾸는 인테리어 혁명 (MoodUP)"): st.session_state.ref_data['feature'] = "무드업"; st.session_state.ref_step = 4; st.rerun()
            if st.button("🧊 홈파티를 완벽하게 해주는 동그란 얼음 제조기 (Craft Ice)"): st.session_state.ref_data['feature'] = "크래프트아이스"; st.session_state.ref_step = 4; st.rerun()

    if st.session_state.ref_step == 4:
        st.balloons()
        st.markdown("### 🎉 Ihr perfekter LG Kühlschrank (당신을 위한 완벽한 냉장고)")
        st.write("<br>", unsafe_allow_html=True)

        def create_lg_card_html(tags, title, model, rating, save_text, price, old_price, btn1_text, btn2_text, is_primary=False):
            tag_html = "".join([f"<span class='lg-tag lg-tag-{'red' if 'InstaView' in t or 'Neu' in t else 'outline'}'>{t}</span>" for t in tags])
            btn2_class = "lg-btn-pri" if is_primary else ("lg-btn-pri" if "kaufen" in btn2_text else "lg-btn-sec")
            return f"""
            <div class="lg-card">
                <div class="lg-tag-row">{tag_html}</div>
                <div class="lg-title">{title}</div>
                <div style="display:flex; justify-content: space-between;"><div class="lg-model">{model}</div><div class="lg-rating">★★★★★ <span style="color:#666;">({rating})</span></div></div>
                <div class="lg-img-box"><h1 style="font-size: 60px; color:#ccc;">🧊</h1></div>
                <div class="lg-price-box"><div class="lg-save-text">{save_text}</div><div><span class="lg-price">{price}</span> <span class="lg-price-old">{old_price}</span></div></div>
                <div class="lg-btn-row"><a href="#" class="lg-btn lg-btn-sec">{btn1_text}</a><a href="#" class="lg-btn {btn2_class}" style="{'' if is_primary else 'background-color:#e50000; color:white; border:none;'}">{btn2_text}</a></div>
            </div>
            """

        cards = [
            create_lg_card_html(["InstaView", "Bestseller"], "LG InstaView Door-in-Door™ Side-by-Side", "GSXV90MCDE", "580", "Spare 300,00 €", "1.799,00 €", "2.099,00 €", "Weitere Infos", "Jetzt kaufen", is_primary=True),
            create_lg_card_html(["MoodUP", "Premium"], "LG MoodUP™ French Door Kühlschrank", "GM-F900MOOD", "120", "Spare 500,00 €", "3.499,00 €", "3.999,00 €", "Weitere Infos", "Jetzt kaufen"),
            create_lg_card_html(["Craft Ice", "Neu"], "LG Multi-Door mit Craft Ice™ Maker", "GM-X945MC9F", "340", "Spare 400,00 €", "2.299,00 €", "2.699,00 €", "Weitere Infos", "Jetzt kaufen")
        ]

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(cards[0], unsafe_allow_html=True)
        with col2: st.markdown(cards[1], unsafe_allow_html=True)
        with col3: st.markdown(cards[2], unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            if st.button("🔄 Test wiederholen (다시 테스트하기)", use_container_width=True):
                st.session_state.ref_step = 1
                st.session_state.ref_data = {}
                st.rerun()

if __name__ == "__main__":
    main()
