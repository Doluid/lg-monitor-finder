import streamlit as st

def main():
    st.set_page_config(page_title="LG Washing Machine Finder", page_icon="🧺", layout="wide")

    # LG.com 스타일 CSS 적용
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
    .lg-energy { font-size: 12px; font-weight: bold; color: #fff; background: #009e49; padding: 2px 6px; border-radius: 2px; display: inline-block;}
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

    if 'wm_step' not in st.session_state:
        st.session_state.wm_step = 1
        st.session_state.wm_data = {}

    st.write("<br>", unsafe_allow_html=True)
    st.title("🧺 LG Waschmaschinen Finder")
    st.markdown("에너지 절약부터 완벽한 옷감 케어까지, 당신의 세탁 라이프를 바꿀 LG 세탁기를 찾아보세요.")
    st.divider()

    if st.session_state.wm_step > 1 and st.session_state.wm_step != 4:
        if st.button("⬅️ Zurück (이전)", key="back_btn_wm"):
            st.session_state.wm_step -= 1
            st.rerun()

    col_q, col_empty = st.columns([2, 1])
    
    with col_q:
        if st.session_state.wm_step == 1:
            st.subheader("1. 주로 세탁을 함께 하는 가구원 수는 몇 명인가요?")
            if st.button("👤 1~2인 가구 (적은 양을 자주 세탁해요 / 7-8kg)"): st.session_state.wm_data['capacity'] = "소형"; st.session_state.wm_step = 2; st.rerun()
            if st.button("👨‍👩‍👦 3~4인 가구 (일반적인 표준 용량 / 9-10kg)"): st.session_state.wm_data['capacity'] = "표준"; st.session_state.wm_step = 2; st.rerun()
            if st.button("👨‍👩‍👧‍👦 대가족 또는 이불 빨래 잦음 (최대 용량 / 11kg 이상)"): st.session_state.wm_data['capacity'] = "대형"; st.session_state.wm_step = 2; st.rerun()

        elif st.session_state.wm_step == 2:
            st.subheader("2. 어떤 형태의 세탁기를 찾고 계신가요?")
            if st.button("🧺 세탁에만 집중하는 클래식 세탁기 (Frontlader)"): st.session_state.wm_data['type'] = "세탁기"; st.session_state.wm_step = 3; st.rerun()
            if st.button("☀️ 세탁과 건조를 한 번에 끝내는 세탁건조기 (Waschtrockner)"): st.session_state.wm_data['type'] = "세탁건조기"; st.session_state.wm_step = 3; st.rerun()
            if st.button("📏 공간이 좁아 쏙 들어가는 슬림형 디자인 (Slim-Design)"): st.session_state.wm_data['type'] = "슬림형"; st.session_state.wm_step = 3; st.rerun()

        elif st.session_state.wm_step == 3:
            st.subheader("3. 절대 포기할 수 없는 LG만의 핵심 기술은 무엇인가요?")
            if st.button("🧠 무게와 옷감 재질을 스스로 파악해 보호하는 지능형 세탁 (AI DD™)"): st.session_state.wm_data['feature'] = "AI_DD"; st.session_state.wm_step = 4; st.rerun()
            if st.button("⏱️ 39분 만에 빠르고 깨끗하게 세탁 완료 (TurboWash™ 360°)"): st.session_state.wm_data['feature'] = "TurboWash"; st.session_state.wm_step = 4; st.rerun()
            if st.button("💨 스팀으로 집먼지 진드기와 알레르기 유발 물질 제거 (Steam™)"): st.session_state.wm_data['feature'] = "Steam"; st.session_state.wm_step = 4; st.rerun()

    if st.session_state.wm_step == 4:
        st.balloons()
        st.markdown("### 🎉 Ihre perfekte LG Waschmaschine (당신을 위한 완벽한 세탁기)")
        st.write("<br>", unsafe_allow_html=True)

        def create_lg_card_html(tags, title, model, rating, save_text, price, old_price, btn1_text, btn2_text, energy_class="A", is_primary=False):
            tag_html = "".join([f"<span class='lg-tag lg-tag-{'red' if 'Neu' in t or 'Bestseller' in t else 'outline'}'>{t}</span>" for t in tags])
            btn2_class = "lg-btn-pri" if is_primary else ("lg-btn-pri" if "kaufen" in btn2_text else "lg-btn-sec")
            return f"""
            <div class="lg-card">
                <div class="lg-tag-row">{tag_html}</div>
                <div class="lg-title">{title}</div>
                <div style="display:flex; justify-content: space-between;"><div class="lg-model">{model}</div><div class="lg-rating">★★★★★ <span style="color:#666;">({rating})</span></div></div>
                <div class="lg-img-box"><h1 style="font-size: 60px; color:#ccc;">🧺</h1></div>
                <div style="margin-bottom: 10px;">
                    <span class="lg-energy">{energy_class}</span> <span style="font-size:12px; color:#666;">Produktdatenblatt</span>
                </div>
                <div class="lg-price-box"><div class="lg-save-text">{save_text}</div><div><span class="lg-price">{price}</span> <span class="lg-price-old">{old_price}</span></div></div>
                <div class="lg-btn-row"><a href="#" class="lg-btn lg-btn-sec">{btn1_text}</a><a href="#" class="lg-btn {btn2_class}" style="{'' if is_primary else 'background-color:#e50000; color:white; border:none;'}">{btn2_text}</a></div>
            </div>
            """

        wm_type = st.session_state.wm_data.get('type', '')
        
        if wm_type == "세탁건조기":
            cards = [
                create_lg_card_html(["Waschtrockner", "AI DD"], "LG Waschtrockner (9kg Waschen / 6kg Trocknen)", "V7WD96H1", "120", "Spare 150,00 €", "799,00 €", "949,00 €", "Weitere Infos", "Jetzt kaufen", "E", is_primary=True),
                create_lg_card_html(["Premium", "TurboWash"], "LG SIGNATURE Waschtrockner (12kg / 7kg)", "LWS27W", "45", "Spare 300,00 €", "1.599,00 €", "1.899,00 €", "Weitere Infos", "Jetzt kaufen", "A"),
                create_lg_card_html(["Steam™", "Kompakt"], "LG Waschtrockner Serie 5 (8kg / 5kg)", "V5WD85H1", "88", "Spare 100,00 €", "649,00 €", "749,00 €", "Weitere Infos", "Jetzt kaufen", "E")
            ]
        elif wm_type == "슬림형":
            cards = [
                create_lg_card_html(["Slim Design", "Steam"], "LG Slim Waschmaschine (7kg, 47cm Tiefe)", "F2WV4S7S1E", "210", "Spare 80,00 €", "499,00 €", "579,00 €", "Weitere Infos", "Jetzt kaufen", "A", is_primary=True),
                create_lg_card_html(["Slim", "AI DD"], "LG Slim Waschmaschine Serie 5 (8.5kg)", "F4WV508S1E", "150", "Spare 100,00 €", "549,00 €", "649,00 €", "Weitere Infos", "Jetzt kaufen", "A"),
                create_lg_card_html(["Kompakt", "Direct Drive"], "LG Slim Waschmaschine (6.5kg)", "F2WV3S6S3E", "95", "Spare 50,00 €", "429,00 €", "479,00 €", "Weitere Infos", "Jetzt kaufen", "B")
            ]
        else:
            cards = [
                create_lg_card_html(["Bestseller", "A -10%"], "LG Waschmaschine Serie 7 (10kg) mit TurboWash™", "F4V710WTSE", "340", "Spare 200,00 €", "699,00 €", "899,00 €", "Weitere Infos", "Jetzt kaufen", "A", is_primary=True),
                create_lg_card_html(["Große Kapazität", "Premium"], "LG Waschmaschine Serie 9 (11kg) mit AI DD™", "F6V9B9W", "180", "Spare 250,00 €", "849,00 €", "1.099,00 €", "Weitere Infos", "Jetzt kaufen", "A"),
                create_lg_card_html(["Eco", "Steam"], "LG Waschmaschine Serie 5 (8kg) mit Dampf", "F4V508WSE", "420", "Spare 120,00 €", "479,00 €", "599,00 €", "Weitere Infos", "Jetzt kaufen", "A")
            ]

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(cards[0], unsafe_allow_html=True)
        with col2: st.markdown(cards[1], unsafe_allow_html=True)
        with col3: st.markdown(cards[2], unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            if st.button("🔄 Test wiederholen (다시 테스트하기)", use_container_width=True):
                st.session_state.wm_step = 1
                st.session_state.wm_data = {}
                st.rerun()

if __name__ == "__main__":
    main()
