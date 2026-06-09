import streamlit as st


def main():
    # 1. 페이지 기본 설정
    st.set_page_config(page_title="LG Monitor Product Finder", page_icon="🖥️", layout="wide")

    # 2. LG.com 스타일의 고급 CSS 적용
    st.markdown("""
    <style>
    .stApp { background-color: #f6f3eb; }

    div.stButton > button {
        width: 100%; height: 70px; font-size: 16px !important; font-weight: 500;
        text-align: left; justify-content: flex-start; padding-left: 20px;
        background-color: #ffffff; border: 2px solid #e5e5e5; border-radius: 8px;
        color: #333; transition: all 0.3s ease; margin-bottom: 5px;
    }
    div.stButton > button:hover {
        border-color: #ea1917; color: #ea1917;
        box-shadow: 0 4px 12px rgba(234, 25, 23, 0.1);
    }

    /* === LG.com 제품 카드 CSS === */
    .lg-card {
        background-color: #ffffff; border-radius: 12px; padding: 24px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); display: flex; flex-direction: column;
        height: 100%; border: 1px solid #eaeaea; font-family: 'Arial', sans-serif;
    }
    .lg-tag-row { display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
    .lg-tag { font-size: 11px; font-weight: bold; padding: 4px 8px; border-radius: 4px; }
    .lg-tag-red { background-color: #ea1917; color: white; }
    .lg-tag-outline { border: 1px solid #ea1917; color: #ea1917; background-color: #fffafb; }
    .lg-title { font-size: 16px; font-weight: 600; line-height: 1.4; color: #000; margin-bottom: 4px; height: 44px; overflow: hidden; }
    .lg-model { font-size: 12px; color: #666; margin-bottom: 12px; }
    .lg-rating { color: #fabb05; font-size: 13px; margin-bottom: 16px; text-align: right;}

    /* 이미지 박스 스타일 - 이미지가 중앙에 꽉 차지 않게 예쁘게 들어가도록 조정 */
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

    # 3. 상태 관리
    if 'step' not in st.session_state:
        st.session_state.step = 1
        st.session_state.data = {}

    st.write("<br>", unsafe_allow_html=True)
    st.title("🖥️ LG Monitor Product Finder")
    st.markdown("당신에게 딱 맞는 LG 모니터를 찾아보세요. (독일 스토어 UI 벤치마킹)")
    st.divider()

    # 이전 단계 버튼
    if st.session_state.step > 1 and st.session_state.step != 4:
        if st.button("⬅️ Zurück (이전)", key="back_btn"):
            if st.session_state.step == 1.1:
                st.session_state.step = 1
            elif st.session_state.step == 2:
                st.session_state.step = 1.1 if "게임" in st.session_state.data.get('purpose', '') else 1
            elif st.session_state.step == 3:
                st.session_state.step = 2
            st.rerun()

    # ==============================
    # Step 1 ~ 3 질문 영역
    # ==============================
    col_q, col_empty = st.columns([2, 1])

    with col_q:
        if st.session_state.step == 1:
            st.subheader("1. 모니터 앞에 앉았을 때, 가장 설레는 순간은?")
            if st.button("🎮 짜릿한 게임 플레이 (Gaming)"): st.session_state.data[
                'purpose'] = "게임"; st.session_state.step = 1.1; st.rerun()
            if st.button("🎨 정밀한 사진/영상 작업 (Pro-Work)"): st.session_state.data[
                'purpose'] = "작업"; st.session_state.step = 2; st.rerun()
            if st.button("📝 전천후 홈오피스와 멀티태스킹 (Home Office)"): st.session_state.data[
                'purpose'] = "오피스"; st.session_state.step = 2; st.rerun()

        elif st.session_state.step == 1.1:
            st.subheader("1-1. 최고의 몰입을 선사하는 게임 스타일은?")
            if st.button("🔫 0.1초 반응이 생명인 경쟁형 FPS (예: 발로란트)"): st.session_state.data[
                'game_style'] = "FPS"; st.session_state.step = 2; st.rerun()
            if st.button("🌍 현실보다 더 진짜 같은 오픈월드 대작"): st.session_state.data[
                'game_style'] = "오픈월드"; st.session_state.step = 2; st.rerun()

        elif st.session_state.step == 2:
            st.subheader("2. 책상 위, 모니터를 위한 공간은 어느 정도인가요?")
            if st.button("🖥️ 24~27인치 (컴팩트 사이즈)"): st.session_state.data[
                'size'] = "27"; st.session_state.step = 3; st.rerun()
            if st.button("📺 32~39인치 (큼직한 대화면)"): st.session_state.data[
                'size'] = "32"; st.session_state.step = 3; st.rerun()
            if st.button("↔️ 40인치 이상 / 울트라와이드"): st.session_state.data[
                'size'] = "40+"; st.session_state.step = 3; st.rerun()

        elif st.session_state.step == 3:
            st.subheader("3. 일상을 완벽하게 만들어줄 '단 하나의 마법'은?")
            if st.button("🔋 깔끔한 충전과 연결 (USB-C / Thunderbolt)"): st.session_state.data[
                'feature'] = "Type-C"; st.session_state.step = 4; st.rerun()
            if st.button("🦾 내 자세에 맞춰 움직이는 자유 (Ergo)"): st.session_state.data[
                'feature'] = "에르고"; st.session_state.step = 4; st.rerun()
            if st.button("🛞 공간 제약 없이 (거실/부엌) 이동하면서 (StandbyMe)"): st.session_state.data[
                'feature'] = "스탠바이미"; st.session_state.step = 4; st.rerun()

    # ==============================
    # Step 4: 결과 화면 (온전한 URL 이미지 매핑)
    # ==============================
    if st.session_state.step == 4:
        st.balloons()
        st.markdown("### 🎉 Ihre perfekten LG Monitore (당신을 위한 완벽한 모니터)")
        st.write("고객님의 응답을 분석하여 가장 잘 맞는 3가지 모델을 추천합니다.")
        st.write("<br>", unsafe_allow_html=True)

        def create_lg_card_html(tags, title, model, rating, save_text, price, old_price, btn1_text, btn2_text, img_url,
                                is_primary=False):
            tag_html = "".join(
                [f"<span class='lg-tag lg-tag-{'red' if 'WM' in t or 'Vorbestellung' in t else 'outline'}'>{t}</span>"
                 for t in tags])
            btn2_class = "lg-btn-pri" if is_primary else ("lg-btn-pri" if "kaufen" in btn2_text else "lg-btn-sec")

            return f"""
            <div class="lg-card">
                <div class="lg-tag-row">{tag_html}</div>
                <div class="lg-title">{title}</div>
                <div style="display:flex; justify-content: space-between;">
                    <div class="lg-model">{model} <span><input type="checkbox"></span></div>
                    <div class="lg-rating">★★★★★ <span style="color:#666;">({rating})</span></div>
                </div>
                <div class="lg-img-box">
                    <img src="{img_url}" alt="{model}">
                </div>
                <div style="margin-bottom: 10px;">
                    <span class="lg-energy">G</span> <span style="font-size:12px; color:#666;">Produktblatt</span>
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
                <div style="text-align: center; margin-top: 15px; font-size: 12px; color: #666;">
                    <input type="checkbox"> Vergleichen
                </div>
            </div>
            """

        purpose = st.session_state.data.get('purpose', '')

        cards = []
        if purpose == "게임":
            cards = [
                # 52G930B-B
                create_lg_card_html(
                    ["2% mit PayPal"], "52 Zoll UltraGear evo G9, Weltweit größter 5K2K 240 Hz Gaming...", "52G930B-B",
                    "7", "Spare 0,00 €", "1.799,00 €", "1.799,00 €", "Weitere<br>Informationen",
                    "Info wenn<br>verfügbar",
                    "https://www.lg.com/content/dam/channel/wcms/de/_it/fcs/52g930b-b/LG-IT_PRJ_Award-Gallery-Images-52G930B-B_2026-03_01_450x450.jpg/jcr:content/renditions/thum-350x350.jpeg"
                ),
                # 39GX950B-B
                create_lg_card_html(
                    ["Vorbestellung", "5 Jahre Garantie"],
                    "39-Zoll-UltraGear evo GX9, der weltweit erste 39-Zoll-5K2K-OLED...", "39GX950B-B", "3",
                    "Spare 0,01 €", "1.798,99 €", "1.799,00 €", "Weitere<br>Informationen", "Vorbestellung",
                    "https://www.lg.com/content/dam/channel/wcms/de/_it/galleries/39gx950b-b/gallery-cards-de/01_39GX950B.jpg/jcr:content/renditions/thum-350x350.jpeg",
                    is_primary=True
                ),
                # 32GS95UE
                create_lg_card_html(
                    ["50€ WM-Bonus", "2% mit PayPal"], "LG UltraGear™ 32 Zoll 4K OLED 240Hz Gaming Monitor", "32GS95UE",
                    "45", "Spare 200,00 €", "1.299,00 €", "1.499,00 €", "Weitere<br>Informationen", "Jetzt kaufen",
                    "https://www.lg.com/content/dam/channel/wcms/de/images/monitore/32gs95ux-b/gallery/ultragear-32gs95ue-basic-large.jpg/jcr:content/renditions/thum-350x350.jpeg"
                )
            ]
        else:  # 작업이나 오피스 등
            cards = [
                # 32U990A-S
                create_lg_card_html(
                    ["Empfehlungen", "2% mit PayPal"], "LG UltraFine™ evo 32 Zoll 6K Nano IPS Black mit Thunderbolt™ 5",
                    "32U990A-S", "80", "Spare 300,00 €", "1.699,00 €", "1.999,00 €", "Weitere<br>Informationen",
                    "Jetzt kaufen",
                    "https://www.lg.com/content/dam/channel/wcms/de/32u990a-s/LG-IT_PRJ_Award-Gallery-Images-32U990A-S_20260504_01_450%20x%20450.jpg/jcr:content/renditions/thum-350x350.jpeg",
                    is_primary=True
                ),
                # 32UN880-B
                create_lg_card_html(
                    ["Neu", "Ergo Stand"], "LG 32 Zoll 4K UHD Ergo Monitor mit USB-C", "32UN880-B", "120",
                    "Spare 150,00 €", "549,00 €", "699,00 €", "Weitere<br>Informationen", "Jetzt kaufen",
                    "https://www.lg.com/content/dam/channel/wcms/de/images/32un880k-b/gallery/ultrafine-uhd-4k-5k-32un880k-2024-gallery-basic-large.jpg/jcr:content/renditions/thum-350x350.jpeg"
                ),
                # 27ART10AKPL (스탠바이미)
                create_lg_card_html(
                    ["Lifestyle", "Smart"], "LG StanbyME 27 Zoll FHD IPS Touch Screen", "27ART10AKPL", "34",
                    "Spare 100,00 €", "999,00 €", "1.099,00 €", "Weitere<br>Informationen", "Jetzt kaufen",
                    "https://www.lg.com/content/dam/channel/wcms/de/2025_ms_lg-com/tv/stanbyme-2/27lx6t/gp1/gallery/basic/450-basic.jpg/jcr:content/renditions/thum-350x350.jpeg"
                )
            ]

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(cards[0], unsafe_allow_html=True)
        with col2:
            st.markdown(cards[1], unsafe_allow_html=True)
        with col3:
            st.markdown(cards[2], unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)

        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            if st.button("🔄 Test wiederholen (다시 테스트하기)", use_container_width=True):
                st.session_state.step = 1
                st.session_state.data = {}
                st.rerun()


if __name__ == "__main__":
    main()
