import streamlit as st

def main():
    st.set_page_config(page_title="LG OLED TV Finder", page_icon="📺", layout="wide")

    # LG.com 스타일 CSS 
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

    # TV 전용 상태 관리 (tv_step, tv_data)
    if 'tv_step' not in st.session_state:
        st.session_state.tv_step = 1
        st.session_state.tv_data = {}

    st.write("<br>", unsafe_allow_html=True)
    st.title("📺 LG OLED TV Finder")
    st.markdown("차원이 다른 블랙, 당신의 거실을 완성할 완벽한 OLED TV를 찾아보세요.")
    st.divider()

    if st.session_state.tv_step > 1 and st.session_state.tv_step != 4:
        if st.button("⬅️ Zurück (이전)", key="back_btn_tv"):
            st.session_state.tv_step -= 1
            st.rerun()

    col_q, col_empty = st.columns([2, 1])
    
    with col_q:
        if st.session_state.tv_step == 1:
            st.subheader("1. TV를 켰을 때, 가장 기대하는 순간은 언제인가요?")
            if st.button("🎬 영화관을 그대로 옮겨놓은 듯한 압도적인 시네마 몰입감"): st.session_state.tv_data['purpose'] = "영화"; st.session_state.tv_step = 2; st.rerun()
            if st.button("⚽ 잔상 없이 빠르고 생생한 스포츠 경기 직관의 감동"): st.session_state.tv_data['purpose'] = "스포츠"; st.session_state.tv_step = 2; st.rerun()
            if st.button("🎮 차세대 콘솔(PS5)의 그래픽을 100% 끌어내는 게이밍"): st.session_state.tv_data['purpose'] = "게임"; st.session_state.tv_step = 2; st.rerun()

        elif st.session_state.tv_step == 2:
            st.subheader("2. TV가 설치될 공간의 크기는 어느 정도인가요?")
            if st.button("🛏️ 안방이나 서브룸에 적합한 사이즈 (42~55인치)"): st.session_state.tv_data['size'] = "중소형"; st.session_state.tv_step = 3; st.rerun()
            if st.button("🛋️ 일반적인 거실에 딱 맞는 표준 대화면 (65~77인치)"): st.session_state.tv_data['size'] = "대형"; st.session_state.tv_step = 3; st.rerun()
            if st.button("🏰 홈씨어터를 완성하는 초대형 프리미엄 스크린 (83~97인치)"): st.session_state.tv_data['size'] = "초대형"; st.session_state.tv_step = 3; st.rerun()

        elif st.session_state.tv_step == 3:
            st.subheader("3. 선호하는 인테리어 및 설치 방식은 무엇인가요?")
            if st.button("🖼️ 벽에 밀착되어 갤러리 액자처럼 보이는 디자인 (Wall-mount)"): st.session_state.tv_data['style'] = "갤러리"; st.session_state.tv_step = 4; st.rerun()
            if st.button("🔌 복잡한 선 없이 깔끔하게 공간을 구성 (Zero Connect 무선)"): st.session_state.tv_data['style'] = "무선"; st.session_state.tv_step = 4; st.rerun()
            if st.button("📺 가장 클래식하고 안정적인 스탠드형 설치 (Stand)"): st.session_state.tv_data['style'] = "스탠드"; st.session_state.tv_step = 4; st.rerun()

    if st.session_state.tv_step == 4:
        st.balloons()
        st.markdown("### 🎉 Ihr perfekter LG OLED TV (당신을 위한 완벽한 OLED TV)")
        st.write("<br>", unsafe_allow_html=True)

        def create_lg_card_html(tags, title, model, rating, save_text, price, old_price, btn1_text, btn2_text, is_primary=False):
            tag_html = "".join([f"<span class='lg-tag lg-tag-{'red' if 'Neu' in t or 'OLED' in t else 'outline'}'>{t}</span>" for t in tags])
            btn2_class = "lg-btn-pri" if is_primary else ("lg-btn-pri" if "kaufen" in btn2_text else "lg-btn-sec")
            return f"""
            <div class="lg-card">
                <div class="lg-tag-row">{tag_html}</div>
                <div class="lg-title">{title}</div>
                <div style="display:flex; justify-content: space-between;"><div class="lg-model">{model}</div><div class="lg-rating">★★★★★ <span style="color:#666;">({rating})</span></div></div>
                <div class="lg-img-box"><h1 style="font-size: 60px; color:#ccc;">📺</h1></div>
                <div class="lg-price-box"><div class="lg-save-text">{save_text}</div><div><span class="lg-price">{price}</span> <span class="lg-price-old">{old_price}</span></div></div>
                <div class="lg-btn-row"><a href="#" class="lg-btn lg-btn-sec">{btn1_text}</a><a href="#" class="lg-btn {btn2_class}" style="{'' if is_primary else 'background-color:#e50000; color:white; border:none;'}">{btn2_text}</a></div>
            </div>
            """

        # 임시 추천 로직 (실제 이미지 URL 매핑 시 교체 필요)
        cards = [
            create_lg_card_html(["OLED evo", "Bestseller"], "LG OLED evo C4 (게이밍 & 올어라운드)", "OLED65C47LA", "450", "Spare 400,00 €", "2.199,00 €", "2.599,00 €", "Weitere Infos", "Jetzt kaufen", is_primary=True),
            create_lg_card_html(["Gallery Design", "Premium"], "LG OLED evo G4 (초밀착 갤러리 핏)", "OLED77G48LW", "210", "Spare 600,00 €", "3.899,00 €", "4.499,00 €", "Weitere Infos", "Jetzt kaufen"),
            create_lg_card_html(["Zero Connect", "Neu"], "LG SIGNATURE OLED M (선 없는 무선 TV)", "OLED83M39LA", "45", "Spare 1.000,00 €", "6.499,00 €", "7.499,00 €", "Weitere Infos", "Jetzt kaufen")
        ]

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(cards[0], unsafe_allow_html=True)
        with col2: st.markdown(cards[1], unsafe_allow_html=True)
        with col3: st.markdown(cards[2], unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            if st.button("🔄 Test wiederholen (다시 테스트하기)", use_container_width=True):
                st.session_state.tv_step = 1
                st.session_state.tv_data = {}
                st.rerun()

if __name__ == "__main__":
    main()
