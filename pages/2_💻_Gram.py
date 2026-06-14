import streamlit as st

def main():
    st.set_page_config(page_title="LG Gram Product Finder", page_icon="💻", layout="wide")

    # LG.com 스타일 CSS 적용 (모니터 버전과 동일)
    st.markdown("""
    <style>
    .stApp { background-color: #f6f3eb; }
    div.stButton > button {
        width: 100%; height: 70px; font-size: 16px !important; font-weight: 500;
        text-align: left; justify-content: flex-start; padding-left: 20px;
        background-color: #ffffff; border: 2px solid #e5e5e5; border-radius: 8px;
        color: #333; transition: all 0.3s ease; margin-bottom: 5px;
    }
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
    .lg-energy { font-size: 12px; font-weight: bold; color: #fff; background: #e3000f; padding: 2px 6px; border-radius: 2px; display: inline-block;}
    .lg-price-box { margin-top: auto; }
    .lg-save-text { color: #ea1917; font-size: 12px; font-weight: bold; margin-bottom: 4px; }
    .lg-price { font-size: 22px; font-weight: bold; color: #000; }
    .lg-price-old { font-size: 14px; text-decoration: line-through; color: #888; margin-left: 8px; }
    .lg-delivery { font-size: 12px; font-weight: bold; color: #d86c00; background: #fff4e6; padding: 6px 12px; border-radius: 4px; display: inline-block; margin: 12px 0; }
    .lg-btn-row { display: flex; gap: 10px; margin-top: 10px; }
    .lg-btn { flex: 1; text-align: center; padding: 12px 0; font-size: 14px; font-weight: bold; border-radius: 6px; cursor: pointer; text-decoration: none; transition: 0.2s; }
    .lg-btn-sec { background-color: white; border: 1px solid #ccc; color: #333; }
    .lg-btn-sec:hover { border-color: #000; }
    .lg-btn-pri { background-color: #e50000; border: 1px solid #e50000; color: white; }
    .lg-btn-pri:hover { background-color: #c40000; }
    </style>
    """, unsafe_allow_html=True)

    if 'step' not in st.session_state:
        st.session_state.step = 1
        st.session_state.data = {}

    st.write("<br>", unsafe_allow_html=True)
    st.title("💻 LG Gram Product Finder")
    st.markdown("가벼움 그 이상, 당신의 일상에 완벽히 맞는 LG 그램을 찾아보세요.")
    st.divider()

    # 뒤로가기 버튼
    if st.session_state.step > 1 and st.session_state.step != 4:
        if st.button("⬅️ Zurück (이전)", key="back_btn"):
            st.session_state.step -= 1
            st.rerun()

    col_q, col_empty = st.columns([2, 1])
    
    with col_q:
        # Step 1: 페르소나
        if st.session_state.step == 1:
            st.subheader("1. 당신의 가방 속에 들어갈 이 노트북, 주로 어떤 역할을 하나요?")
            if st.button("📝 문서 작성, 웹서핑, 대학 과제 등 가벼운 일상 (Standard)"): st.session_state.data['persona'] = "일상"; st.session_state.step = 2; st.rerun()
            if st.button("🎬 영상 편집, 3D 디자인, 코딩 등 무거운 작업 (Pro/Creator)"): st.session_state.data['persona'] = "프로"; st.session_state.step = 2; st.rerun()
            if st.button("🎨 화면을 접어 자유롭게 스케치하고 필기 (Artist/2-in-1)"): st.session_state.data['persona'] = "투인원"; st.session_state.step = 4; st.rerun() # 2-in-1은 사이즈/디스플레이가 정해져 있어 Step 4로 하이패스

        # Step 2: 사이즈
        elif st.session_state.step == 2:
            st.subheader("2. 매일 들고 다니는 무게는 똑같이 가볍습니다. 화면 크기는 어느 정도가 좋을까요?")
            if st.button("🎒 에코백에도 쏙 들어가는 극강의 휴대성 (14~15.6인치)"): st.session_state.data['size'] = "14/15"; st.session_state.step = 3; st.rerun()
            if st.button("⚖️ 휴대성과 작업 공간의 완벽한 밸런스 (16인치)"): st.session_state.data['size'] = "16"; st.session_state.step = 3; st.rerun()
            if st.button("🖥️ 데스크탑이 필요 없는 광활한 작업 공간 (17인치)"): st.session_state.data['size'] = "17"; st.session_state.step = 3; st.rerun()

        # Step 3: 디스플레이/특징
        elif st.session_state.step == 3:
            st.subheader("3. 마지막으로, 당신의 눈을 가장 즐겁게 할 디스플레이 마법은?")
            if st.button("☀️ 밝은 카페나 야외에서도 빛 반사 없는 편안함 (Anti-glare IPS)"): st.session_state.data['display'] = "IPS"; st.session_state.step = 4; st.rerun()
            if st.button("🌌 넷플릭스나 사진 편집을 위한 완벽한 블랙 (OLED)"): st.session_state.data['display'] = "OLED"; st.session_state.step = 4; st.rerun()
            if st.button("⚡ 화면 스크롤마저 부드러운 압도적인 주사율 (144Hz / VRR)"): st.session_state.data['display'] = "144Hz"; st.session_state.step = 4; st.rerun()

    # Step 4: 결과 화면
    if st.session_state.step == 4:
        st.balloons()
        st.markdown("### 🎉 Ihr perfekter LG Gram (당신을 위한 완벽한 LG 그램)")
        st.write("고객님의 답변을 분석하여 가장 잘 맞는 그램 라인업을 추천합니다.")
        st.write("<br>", unsafe_allow_html=True)

        def create_lg_card_html(tags, title, model, rating, save_text, price, old_price, btn1_text, btn2_text, img_url, is_primary=False):
            tag_html = "".join([f"<span class='lg-tag lg-tag-{'red' if 'WM' in t or 'Neu' in t else 'outline'}'>{t}</span>" for t in tags])
            btn2_class = "lg-btn-pri" if is_primary else ("lg-btn-pri" if "kaufen" in btn2_text else "lg-btn-sec")
            
            return f"""
            <div class="lg-card">
                <div class="lg-tag-row">{tag_html}</div>
                <div class="lg-title">{title}</div>
                <div style="display:flex; justify-content: space-between;">
                    <div class="lg-model">{model} <span><input type="checkbox"></span></div>
                    <div class="lg-rating">★★★★★ <span style="color:#666;">({rating})</span></div>
                </div>
                <div class="lg-img-box"><img src="{img_url}" alt="{model}"></div>
                <div style="margin-bottom: 10px;">
                    <span style="font-size:12px; color:#666;">Intel® Core™ Ultra Processor</span>
                </div>
                <div class="lg-price-box">
                    <div class="lg-save-text">{save_text}</div>
                    <div><span class="lg-price">{price}</span> <span class="lg-price-old">{old_price}</span></div>
                    <div style="font-size: 11px; color: #888;">€74.96 / mtl. bis zu 24 Raten für 0%</div>
                </div>
                <div class="lg-delivery">🚚 Free Delivery</div>
                <div class="lg-btn-row">
                    <a href="#" class="lg-btn lg-btn-sec">{btn1_text}</a>
                    <a href="#" class="lg-btn {btn2_class}" style="{'' if is_primary else 'background-color:#e50000; color:white; border:none;'}">{btn2_text}</a>
                </div>
                <div style="text-align: center; margin-top: 15px; font-size: 12px; color: #666;"><input type="checkbox"> Vergleichen</div>
            </div>
            """

        persona = st.session_state.data.get('persona', '')
        
        # 데모용 이미지 URL (LG.com 독일 기반 대표 이미지 매핑)
        img_pro_16 = "https://www.lg.com/content/dam/channel/wcms/de/images/laptops/16z90sp-g.ad78g/gallery/16Z90SP-G-Large-01.jpg/jcr:content/renditions/thum-350x350.jpeg"
        img_gram_17 = "https://www.lg.com/content/dam/channel/wcms/de/images/laptops/17z90r-g.aa79g/gallery/17Z90R-G-Large-01.jpg/jcr:content/renditions/thum-350x350.jpeg"
        img_2in1 = "https://www.lg.com/content/dam/channel/wcms/de/images/laptops/16t90r-g.aa76g/gallery/16T90R-G-Large-01.jpg/jcr:content/renditions/thum-350x350.jpeg"

        cards = []
        if persona == "투인원":
            cards = [
                create_lg_card_html(["Empfehlungen"], "LG gram 14 2-in-1 (14인치 WUXGA 터치)", "14T90R-G", "85", "Spare 200,00 €", "1.499,00 €", "1.699,00 €", "Weitere Infos", "Jetzt kaufen", img_2in1),
                create_lg_card_html(["Neu", "Bestseller"], "LG gram 16 2-in-1 (16인치 WQXGA 터치 & 펜)", "16T90R-G", "120", "Spare 300,00 €", "1.699,00 €", "1.999,00 €", "Weitere Infos", "Jetzt kaufen", img_2in1, is_primary=True),
                create_lg_card_html(["OLED"], "LG gram Style 16 (오로라 화이트, 히든 터치패드)", "16Z90RS-G", "45", "Spare 150,00 €", "1.749,00 €", "1.899,00 €", "Weitere Infos", "Jetzt kaufen", img_gram_17)
            ]
        elif persona == "프로":
            cards = [
                create_lg_card_html(["Creator"], "LG gram Pro 16 (Intel Core Ultra 7, 144Hz)", "16Z90SP-G", "60", "Spare 250,00 €", "1.849,00 €", "2.099,00 €", "Weitere Infos", "Jetzt kaufen", img_pro_16, is_primary=True),
                create_lg_card_html(["RTX 3050", "Gaming"], "LG gram Pro 17 (NVIDIA 외장 그래픽 탑재)", "17Z90SP-G", "38", "Spare 300,00 €", "2.199,00 €", "2.499,00 €", "Weitere Infos", "Jetzt kaufen", img_gram_17),
                create_lg_card_html(["Neu"], "LG gram 16 (Intel Core Ultra 5, 고해상도)", "16Z90S-G", "95", "Spare 100,00 €", "1.599,00 €", "1.699,00 €", "Weitere Infos", "Jetzt kaufen", img_pro_16)
            ]
        else:
            cards = [
                create_lg_card_html(["Ultra Light"], "LG gram 14 (999g 초경량, 배터리 최장)", "14Z90S-G", "150", "Spare 100,00 €", "1.299,00 €", "1.399,00 €", "Weitere Infos", "Jetzt kaufen", img_pro_16),
                create_lg_card_html(["Bestseller", "IPS"], "LG gram 16 (16:10 대화면, 1.19kg)", "16Z90S-G", "320", "Spare 200,00 €", "1.499,00 €", "1.699,00 €", "Weitere Infos", "Jetzt kaufen", img_pro_16, is_primary=True),
                create_lg_card_html(["Desktop-Ersatz"], "LG gram 17 (17인치 대화면, 숫자 키패드 포함)", "17Z90S-G", "210", "Spare 250,00 €", "1.649,00 €", "1.899,00 €", "Weitere Infos", "Jetzt kaufen", img_gram_17)
            ]

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(cards[0], unsafe_allow_html=True)
        with col2: st.markdown(cards[1], unsafe_allow_html=True)
        with col3: st.markdown(cards[2], unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            if st.button("🔄 Test wiederholen (다시 테스트하기)", use_container_width=True):
                st.session_state.step = 1
                st.session_state.data = {}
                st.rerun()

if __name__ == "__main__":
    main()
