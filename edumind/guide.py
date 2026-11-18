"""User Guide component focusing exclusively on the 3 core features of EduMind AI:
1. Giải Bài Tập AI (Học tập thông minh)
2. Chăm Sóc Tinh Thần (Trạm sạc năng lượng)
3. Định Hướng Tương Lai (La bàn sự nghiệp)
"""
from __future__ import annotations

from pathlib import Path
from typing import Callable, Optional
import streamlit as st

from .models import Feature

ASSETS_DIR = Path(__file__).resolve().parent / "assets" / "guide"


def _show_image(img_filename: str, caption: str = ""):
    img_path = ASSETS_DIR / img_filename
    if img_path.is_file():
        st.image(str(img_path), caption=caption, use_container_width=True)


def user_guide_page(navigate_fn: Optional[Callable[[Feature], None]] = None):
    def _go_to(feature: Feature):
        if navigate_fn:
            navigate_fn(feature)
        else:
            st.session_state["_next_nav"] = feature.value
            st.rerun()

    # Custom styling for guide cards and steps
    st.markdown(
        """
        <style>
        .guide-header-hero {
            padding: 1.3rem 1.6rem;
            border-radius: 20px;
            border: 1px solid color-mix(in srgb, var(--em-violet) 25%, transparent);
            background: linear-gradient(135deg, color-mix(in srgb, var(--em-violet) 12%, transparent), color-mix(in srgb, var(--em-blue) 8%, transparent));
            margin-bottom: 1.25rem;
        }
        .guide-hero-title {
            font-size: 1.55rem;
            font-weight: 850;
            letter-spacing: -0.02em;
            margin: 0 0 0.4rem;
        }
        .guide-hero-desc {
            font-size: 0.92rem;
            opacity: 0.84;
            line-height: 1.55;
            margin: 0;
            max-width: 900px;
        }
        .feature-intro-card {
            display: flex;
            align-items: center;
            gap: 1.2rem;
            padding: 1.1rem 1.4rem;
            border-radius: 18px;
            border: 1px solid color-mix(in srgb, currentColor 14%, transparent);
            background: color-mix(in srgb, currentColor 4%, transparent);
            margin-bottom: 1.2rem;
        }
        .feature-intro-badge {
            flex: 0 0 54px;
            height: 54px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.9rem;
            border-radius: 16px;
            background: color-mix(in srgb, currentColor 8%, transparent);
        }
        .feature-intro-text h3 {
            margin: 0 0 0.25rem;
            font-size: 1.25rem;
            font-weight: 800;
        }
        .feature-intro-text p {
            margin: 0;
            font-size: 0.88rem;
            opacity: 0.8;
            line-height: 1.45;
        }
        .guide-step-card {
            border-radius: 14px;
            border: 1px solid color-mix(in srgb, currentColor 12%, transparent);
            background: color-mix(in srgb, currentColor 3%, transparent);
            padding: 0.95rem 1.2rem;
            margin-bottom: 0.8rem;
        }
        .guide-step-num {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 26px;
            height: 26px;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 800;
            color: #fff;
            background: var(--em-violet);
            margin-right: 0.5rem;
        }
        .guide-callout {
            border-left: 3px solid var(--em-violet);
            background: color-mix(in srgb, var(--em-violet) 7%, transparent);
            padding: 0.8rem 1.1rem;
            border-radius: 0 12px 12px 0;
            margin: 0.8rem 0;
            font-size: 0.88rem;
            line-height: 1.5;
        }
        .guide-callout strong {
            color: var(--em-violet);
        }
        .guide-callout.pink {
            border-left-color: var(--em-pink);
            background: color-mix(in srgb, var(--em-pink) 7%, transparent);
        }
        .guide-callout.pink strong {
            color: var(--em-pink);
        }
        .guide-callout.cyan {
            border-left-color: #06b6d4;
            background: color-mix(in srgb, #06b6d4 7%, transparent);
        }
        .guide-callout.cyan strong {
            color: #06b6d4;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Hero Banner
    st.markdown(
        """
        <div class="guide-header-hero">
          <div class="eyebrow" style="color:var(--em-violet); font-size:0.75rem; font-weight:800; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.3rem;">
            EDUMIND AI · CẨM NANG SỬ DỤNG
          </div>
          <h1 class="guide-hero-title">Hướng dẫn sử dụng 3 Chức năng cốt lõi</h1>
          <p class="guide-hero-desc">
            EduMind AI tích hợp trọn vẹn 3 nhu cầu thiết yếu nhất của học sinh: <strong>Gia sư giải bài tập thông minh</strong>, <strong>Không gian chăm sóc tinh thần an toàn</strong>, và <strong>La bàn định hướng tương lai</strong>. Chọn từng mục bên dưới để xem hướng dẫn chi tiết, hình ảnh minh họa và các nút tương tác nhanh.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 3 Main Feature Tabs
    tab_study, tab_wellbeing, tab_career = st.tabs([
        "📚 1. Giải Bài Tập AI",
        "🌱 2. Chăm Sóc Tinh Thần",
        "🧭 3. Định Hướng Tương Lai",
    ])

    # =========================================================================
    # TAB 1: GIẢI BÀI TẬP AI
    # =========================================================================
    with tab_study:
        st.markdown(
            """
            <div class="feature-intro-card">
              <div class="feature-intro-badge">📚</div>
              <div class="feature-intro-text">
                <h3>Chức năng: Giải Bài Tập AI (Học tập thông minh)</h3>
                <p>Đóng vai trò như một gia sư kiên nhẫn: giảng giải cặn kẽ bản chất bài toán, phân tích lỗi sai và hướng dẫn phương pháp làm bài tối ưu.</p>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col_action, col_info = st.columns([1.2, 2.8], vertical_alignment="center")
        with col_action:
            if st.button("👉 Bắt đầu Giải bài tập ngay", type="primary", use_container_width=True, icon=":material/school:"):
                _go_to(Feature.STUDY)
        with col_info:
            st.caption("Chuyển thẳng sang không gian Giải bài tập để nhập câu hỏi hoặc gửi ảnh bài toán.")

        st.markdown("---")

        st.subheader("🖼️ Giao diện thực tế của tính năng")
        _show_image("study_guide_1.png", "Giao diện Giải bài tập AI: Khung trò chuyện, thanh chọn môn học và nút gửi yêu cầu")

        st.markdown("---")

        st.subheader("📋 Quy trình 4 bước sử dụng chi tiết")

        st.markdown(
            """
            <div class="guide-step-card">
              <span class="guide-step-num">1</span><strong>Chọn Chế độ AI phù hợp với nhu cầu:</strong>
              <ul>
                <li><strong>Chế độ Nhanh (Fast Mode):</strong> Phù hợp khi bạn cần kiểm tra nhanh đáp số, tra cứu công thức, định lý hoặc tóm tắt lời giải ngắn gọn.</li>
                <li><strong>Chế độ Tư duy (Thinking Mode):</strong> Phù hợp với bài toán khó, bài tập nâng cao. AI sẽ suy luận từng bước (Step-by-step), giải thích tại sao lại áp dụng công thức đó và chỉ ra các bẫy học sinh hay mắc. <em>(Lưu ý: Chế độ Tư duy yêu cầu đăng nhập tài khoản)</em>.</li>
              </ul>
            </div>

            <div class="guide-step-card">
              <span class="guide-step-num">2</span><strong>Nhập câu hỏi bài tập hoặc tải ảnh:</strong>
              <ul>
                <li><strong>Nhập văn bản:</strong> Gõ trực tiếp đề bài vào khung chat bên dưới. Hệ thống hỗ trợ công thức Toán học chuẩn LaTeX đặt giữa hai dấu <code>$</code> (ví dụ: <code>$x^2 - 4x + 3 = 0$</code>).</li>
                <li><strong>Gợi ý môn học:</strong> Bấm vào các thẻ môn học gợi ý trên thanh công cụ (Toán, Vật lí, Hóa học, Sinh học, Tin học...) để lấy cấu trúc câu hỏi chuẩn.</li>
              </ul>
            </div>

            <div class="guide-step-card">
              <span class="guide-step-num">3</span><strong>Giải bài qua ảnh chụp hoặc Camera (Multimodal):</strong>
              <ul>
                <li>Bấm biểu tượng camera / tải ảnh để đính kèm hình ảnh đề bài từ sách vở, đề thi.</li>
                <li>Hệ thống hỗ trợ định dạng JPG, PNG, tối đa 10 MB và tự động tối ưu hóa kích thước.</li>
                <li><strong>Quota hàng ngày:</strong> Mỗi người dùng được cấp <strong>3 lượt gửi ảnh/ngày</strong> để đảm bảo hiệu năng và tính bảo mật. Hạn mức tự động làm mới vào 00:00 mỗi ngày.</li>
              </ul>
            </div>

            <div class="guide-step-card">
              <span class="guide-step-num">4</span><strong>Tương tác đối thoại 2 chiều và quản lý phiên học:</strong>
              <ul>
                <li>Nếu chưa hiểu bất kỳ bước giải nào, bạn hãy thoải mái hỏi tiếp: <em>"Tại sao từ bước 2 lại suy ra được bước 3?"</em> hoặc <em>"Có cách giải nào bằng phương pháp hình học không?"</em>.</li>
                <li>Lịch sử buổi học được tự động lưu lại ở thanh bên trái (Sidebar). Bạn có thể tìm kiếm, đổi tên phiên học hoặc xoá khi không cần thiết.</li>
              </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="guide-callout">
              <strong>💡 Mẹo học tập thông minh:</strong> Đừng chỉ chép đáp án! Hãy yêu cầu AI: <em>"Đừng giải hết, hãy cho mình gợi ý bước đầu tiên để mình tự giải tiếp"</em>. Đây là cách rèn luyện tư duy tự học hiệu quả nhất cùng EduMind AI.
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.expander("📝 **Bấm xem các câu lệnh (Prompt) mẫu theo từng môn học**"):
            st.markdown(
                """
                - **Toán học:** *"Cho hàm số $y = x^3 - 3x^2 + 2$. Hãy hướng dẫn mình các bước khảo sát sự biến thiên và tìm toạ độ điểm cực trị."*
                - **Vật lí:** *"Một vật có khối lượng 2kg trượt trên mặt phẳng nghiêng 30 độ với hệ số ma sát 0.1. Hãy phân tích các lực tác dụng và tính gia tốc của vật."*
                - **Hóa học:** *"Hướng dẫn mình phương pháp cân bằng phản ứng oxi hoá khử sau bằng phương pháp thăng bằng electron: $Fe_3O_4 + HNO_3 \\rightarrow Fe(NO_3)_3 + NO + H_2O$."*
                - **Tin học:** *"Giải thích nguyên lý hoạt động của thuật toán tìm kiếm nhị phân (Binary Search) bằng Python và cho ví dụ minh hoạ dễ hiểu."*
                """
            )

    # =========================================================================
    # TAB 2: CHĂM SÓC TINH THẦN
    # =========================================================================
    with tab_wellbeing:
        st.markdown(
            """
            <div class="feature-intro-card">
              <div class="feature-intro-badge">🌱</div>
              <div class="feature-intro-text">
                <h3>Chức năng: Chăm Sóc Tinh Thần (Trạm sạc năng lượng)</h3>
                <p>Một khoảng dừng tĩnh lặng, an toàn để học sinh nhìn nhận cảm xúc, giải tỏa áp lực thi cử, peer pressure và nhận những gợi ý phục hồi năng lượng.</p>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col_action_w, col_info_w = st.columns([1.2, 2.8], vertical_alignment="center")
        with col_action_w:
            if st.button("👉 Vào Trạm sạc năng lượng ngay", type="primary", use_container_width=True, icon=":material/spa:"):
                _go_to(Feature.WELLBEING)
        with col_info_w:
            st.caption("Chuyển thẳng sang không gian Chăm sóc tinh thần để check-in cùng linh vật Mindi.")

        st.markdown("---")

        st.subheader("🖼️ Giao diện thực tế của tính năng")
        col_img1, col_img2 = st.columns(2)
        with col_img1:
            _show_image("wellbeing_guide_1.png", "Bước Check-in cảm xúc cùng Mindi")
        with col_img2:
            _show_image("wellbeing_guide_2.png", "Giao diện trò chuyện thấu cảm và gợi ý hành động")

        st.markdown("---")

        st.subheader("📋 Quy trình Check-in 4 bước cùng Mindi")

        st.markdown(
            """
            <div class="guide-step-card">
              <span class="guide-step-num">1</span><strong>Bước 1 · Nhận diện cảm xúc:</strong>
              <p>Chọn cảm xúc gần nhất với bạn lúc này: <em>Khá ổn, Mệt mỏi, Lo lắng, Buồn, Bối rối, Khó gọi tên</em>. Linh vật cú mèo Mindi sẽ ngay lập tức thay đổi ánh mắt và biểu cảm động để đồng hành cùng bạn.</p>
            </div>

            <div class="guide-step-card">
              <span class="guide-step-num">2</span><strong>Bước 2 · Bộc bạch điều đang bận tâm:</strong>
              <p>Ghi ngắn gọn điều đang khiến bạn nặng lòng (ví dụ: bài kiểm tra điểm kém, mâu thuẫn bạn bè, áp lực kỳ vọng gia đình, hoặc mất ngủ). <em>Bạn hoàn toàn có thể để trống nếu lúc này chỉ muốn tìm sự tĩnh lặng</em>.</p>
            </div>

            <div class="guide-step-card">
              <span class="guide-step-num">3</span><strong>Bước 3 · Đánh giá mức độ ảnh hưởng:</strong>
              <p>Thang điểm từ <strong>1 (Nhẹ)</strong> đến <strong>5 (Rất nhiều)</strong> để AI hiểu được mức độ căng thẳng hiện tại của bạn.</p>
            </div>

            <div class="guide-step-card">
              <span class="guide-step-num">4</span><strong>Bước 4 · Chọn mong muốn hỗ trợ:</strong>
              <p>Bạn mong muốn EduMind hỗ trợ như thế nào?
                <br/>• <em>Lắng nghe nhẹ nhàng</em> (không phán xét, chỉ cần một người thấu hiểu).
                <br/>• <em>Bài tập thở & thư giãn</em> (kỹ thuật thở 4-7-8 giúp nhịp tim chậm lại).
                <br/>• <em>Tìm góc nhìn mới tích cực</em> (tái cấu trúc nhận thức, giảm lo âu).
                <br/>• <em>Lập kế hoạch từng bước nhỏ</em> (hành động từng chút để vượt qua trì hoãn).
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="guide-callout pink">
              <strong>🔒 Cam kết Bảo mật & Riêng tư tuyệt đối:</strong>
              <br/>Khác hoàn toàn với các phần học tập, không gian Chăm sóc tinh thần <strong>KHÔNG LƯU NỘI DUNG VÀO DATABASE MÁY CHỦ</strong>. Mọi chia sẻ của bạn chỉ tồn tại trong phiên làm việc hiện tại và biến mất khi bạn tắt trình duyệt. Bạn hoàn toàn có thể trút bỏ gánh nặng trong lòng mà không sợ ai đọc được.
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.expander("✨ **Bấm xem các chủ đề tâm sự phổ biến của học sinh**"):
            st.markdown(
                """
                - **Áp lực kỳ vọng gia đình:** *"Bố mẹ luôn so sánh mình với con nhà người ta, mình cảm thấy ngột ngạt và tự ti..."*
                - **Peer Pressure (Áp lực đồng trang lứa):** *"Thấy các bạn xung quanh đạt giải cao, học thêm nhiều môn, mình cảm thấy bản thân tụt hậu..."*
                - **Khủng hoảng trước kỳ thi:** *"Chỉ còn 1 tháng nữa là thi tốt nghiệp mà mình cảm thấy đầu óc trống rỗng, rất khó tập trung học bài..."*
                - **Mất ngủ và kiệt sức (Burnout):** *"Dạo này mình thường xuyên thức khuya, sáng dậy uể oải không có chút động lực nào..."*
                """
            )

    # =========================================================================
    # TAB 3: ĐỊNH HƯỚNG TƯƠNG LAI
    # =========================================================================
    with tab_career:
        st.markdown(
            """
            <div class="feature-intro-card">
              <div class="feature-intro-badge">🧭</div>
              <div class="feature-intro-text">
                <h3>Chức năng: Định Hướng Tương Lai (La bàn sự nghiệp)</h3>
                <p>Ứng dụng các phương pháp hướng nghiệp hiện đại giúp học sinh thấu hiểu bản thân, xác định điểm mạnh và thiết lập lộ trình học tập vững chắc.</p>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col_action_c, col_info_c = st.columns([1.2, 2.8], vertical_alignment="center")
        with col_action_c:
            if st.button("👉 Khám phá Hướng đi tương lai ngay", type="primary", use_container_width=True, icon=":material/explore:"):
                _go_to(Feature.CAREER)
        with col_info_c:
            st.caption("Chuyển thẳng sang không gian Định hướng tương lai để thử nghiệm Ikigai, Lộ trình ngược và Giả lập nghề nghiệp.")

        st.markdown("---")

        st.subheader("🖼️ Giao diện thực tế của tính năng")
        col_c_img1, col_c_img2 = st.columns(2)
        with col_c_img1:
            _show_image("career_guide_1.png", "Công cụ Khám phá Ikigai và Lập lộ trình ngược")
        with col_c_img2:
            _show_image("career_guide_2.png", "Tính năng Giả lập nghề nghiệp tương tác")

        st.markdown("---")

        st.subheader("🛠️ 3 Công cụ Hướng nghiệp độc quyền của EduMind AI")

        st.markdown(
            """
            <div class="guide-step-card">
              <span class="guide-step-num">1</span><strong>🧩 Khám phá Ikigai (Giao thoa lý tưởng):</strong>
              <p>Dựa trên triết lý Ikigai nổi tiếng của Nhật Bản, kết hợp 4 vòng tròn cốt lõi:
                <br/>• <em>Điều bạn đam mê:</em> Những môn học, sở thích bạn có thể làm hàng giờ không chán.
                <br/>• <em>Điều bạn làm giỏi:</em> Năng khiếu tự nhiên, điểm số vượt trội ở các môn.
                <br/>• <em>Điều xã hội cần:</em> Các ngành nghề đang khan hiếm nhân lực trong kỷ nguyên số.
                <br/>• <em>Điều giúp bạn có thu nhập:</em> Kỳ vọng mức sống và tiềm năng phát triển tài chính.
                <br/>➡️ <strong>Kết quả từ AI:</strong> Đề xuất 3 hướng nghề nghiệp khả thi nhất, phân tích điểm chạm và gợi ý tổ hợp môn cần tập trung.
              </p>
            </div>

            <div class="guide-step-card">
              <span class="guide-step-num">2</span><strong>🗺️ Lộ trình ngược (Reverse Roadmap):</strong>
              <p>Thay vì loay hoay từ hiện tại nhìn về tương lai mông lung, phương pháp Lộ trình ngược bắt đầu từ <strong>đích đến mong muốn</strong>:
                <br/>• <em>Ví dụ mục tiêu:</em> "Đỗ ngành Khoa học Máy tính Đại học Bách Khoa năm 2027" hoặc "Săn học bổng du học sinh".
                <br/>• <em>Cách AI lập kế hoạch lùi dần:</em>
                <br/>- <strong>Trước 1 năm:</strong> Mốc điểm chứng chỉ ngoại ngữ (IELTS/SAT) và hoàn thành hồ sơ năng lực.
                <br/>- <strong>Trước 6 tháng:</strong> Luyện đề thi đánh giá năng lực và chuyên sâu môn Toán - Lý.
                <br/>- <strong>Trong tháng này:</strong> Hoàn thành từng chương kiến thức nền tảng.
                <br/>- <strong>Hôm nay:</strong> Một hành động nhỏ cụ thể bạn có thể bắt đầu ngay trong 30 phút tới.
              </p>
            </div>

            <div class="guide-step-card">
              <span class="guide-step-num">3</span><strong>💼 Giả lập nghề nghiệp (Job Simulation):</strong>
              <p>Trải nghiệm "một ngày thử làm nghề" trước khi quyết định chọn ngành:
                <br/>• <em>Nhập vai đa dạng:</em> Kỹ sư Trí tuệ nhân tạo (AI Engineer), Bác sĩ điều trị, Chuyên viên Tâm lý học đường, Nhà thiết kế đồ hoạ, Quản trị viên kinh doanh...
                <br/>• <em>Giải quyết bài toán thực tế:</em> AI đưa ra một tình huống thực tế cam go thường gặp trong nghề. Bạn sẽ đưa ra phương án xử lý, sau đó AI phân tích điểm mạnh, điểm yếu và mức độ phù hợp của bạn với nghề đó.
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="guide-callout cyan">
              <strong>🎯 Lời khuyên định hướng:</strong> Hãy thử ít nhất 2 đến 3 ngành nghề khác nhau trong phần Giả lập nghề nghiệp. Bạn sẽ bất ngờ khi nhận ra sự khác biệt giữa "nghĩ là mình thích" và "thực tế trải nghiệm công việc hàng ngày"!
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.expander("🚀 **Bấm xem các mẫu câu hỏi định hướng sự nghiệp hay**"):
            st.markdown(
                """
                - **Ikigai:** *"Mình thích vẽ, giỏi Toán và thích công nghệ, muốn mức lương khởi điểm từ 15-20 triệu. Hãy gợi ý 3 ngành học phù hợp kèm trường đại học uy tín tại Việt Nam."*
                - **Lộ trình ngược:** *"Mục tiêu của mình là đạt 8.0 IELTS và đỗ ngành Kinh tế Đối ngoại trong 2 năm tới. Hãy lập cho mình lộ trình ngược chi tiết theo từng quý."*
                - **Giả lập nghề:** *"Hãy đóng vai người phỏng vấn, đưa ra một thử thách thực tế cho vị trí Data Analyst (Chuyên viên Phân tích Dữ liệu) để mình giải quyết."*
                """
            )

    st.caption("EduMind AI · Cẩm nang hướng dẫn sử dụng 3 tính năng cốt lõi. Bản quyền dự án EduMind.")
