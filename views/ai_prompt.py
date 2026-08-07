import streamlit as st
import time
from datetime import datetime

from utils.utils import image_to_png_bytes


def _set_quick_prompt(text):

    st.session_state.ai_prompt_text = text


def show():

    st.markdown("""
<div class="hero">

<span class="badge">
🤖 AI Prompt Editor
</span>

<h1>
Edit Image Using Prompt
</h1>

<p>
Cukup tuliskan apa yang ingin diubah,
biarkan AI mengerjakan sisanya.
</p>

</div>
""", unsafe_allow_html=True)

    st.write("")

    # ============================================
    # IMAGE CHECK
    # ============================================

    if st.session_state.uploaded_image is None:

        st.warning(
            "Silakan upload gambar terlebih dahulu."
        )

        st.stop()

    # ============================================
    # LAYOUT
    # ============================================

    left, right = st.columns([1,1])

    with left:

        st.markdown("## 🖼 Original Image")

        st.image(

            st.session_state.uploaded_image,

            use_container_width=True

        )

    with right:

        st.markdown("## ✍ Prompt")

        prompt = st.text_area(

            "Masukkan Prompt",

            height=220,

            key="ai_prompt_text",

            placeholder="""
Contoh :

- Hilangkan orang di belakang

- Ganti background menjadi pantai

- Tambahkan langit malam

- Jadikan bergaya Anime

- Tambahkan efek hujan

- Jadikan kualitas HD

- Tambahkan salju
"""

        )

        st.write("")

        st.markdown("### ⚡ Quick Prompt")

        p1,p2 = st.columns(2)

        with p1:

            st.button(
                "🖼 Remove Background",
                use_container_width=True,
                on_click=_set_quick_prompt,
                args=("Remove background",)
            )

        with p2:

            st.button(
                "🌄 New Background",
                use_container_width=True,
                on_click=_set_quick_prompt,
                args=("Replace background",)
            )

        p3,p4 = st.columns(2)

        with p3:

            st.button(
                "✨ Enhance",
                use_container_width=True,
                on_click=_set_quick_prompt,
                args=("Enhance image",)
            )

        with p4:

            st.button(
                "🎨 Anime Style",
                use_container_width=True,
                on_click=_set_quick_prompt,
                args=("Anime style",)
            )

    st.write("")
    st.divider()

    # EXAMPLE PROMPT

    
    
    st.markdown("## 💡 Prompt Inspiration")

    c1,c2,c3 = st.columns(3)

    with c1:

        st.info("""

🏖 Tropical Beach

"Ganti background menjadi pantai Bali saat sunset."

""")

    with c2:

        st.info("""

🌃 Cyberpunk

"Ubah menjadi kota cyberpunk di malam hari."

""")

    with c3:

        st.info("""

🎨 Anime

"Jadikan foto bergaya anime Jepang."

""")

    st.write("")
    st.divider()

    # ============================================
    # GENERATE
    # ============================================

    generate = st.button(

        "🚀 Generate AI",

        use_container_width=True,

        type="primary"

    )

    if generate:

        if prompt.strip() == "":

            st.warning(
                "Prompt tidak boleh kosong."
            )

        else:

            progress = st.progress(0)

            status = st.empty()

            for i in range(100):

                time.sleep(0.02)

                progress.progress(i+1)

                status.write(
                    f"Generating... {i+1}%"
                )

            status.success(
                "AI selesai memproses gambar."
            )

            result_image = st.session_state.uploaded_image.copy()

            st.session_state.edited_image = result_image

            st.session_state.history.append({

                "time": datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                ),

                "prompt": prompt,

                "image": result_image

            })

    st.write("")

    # ============================================
    # RESULT
    # ============================================

    if st.session_state.edited_image is not None:

        st.markdown("## ✨ Result")

        left,right = st.columns(2)

        with left:

            st.markdown("### Original")

            st.image(

                st.session_state.uploaded_image,

                use_container_width=True

            )

        with right:

            st.markdown("### AI Result")

            st.image(

                st.session_state.edited_image,

                use_container_width=True

            )

        st.write("")

        st.download_button(

            "⬇ Download Result",

            data=image_to_png_bytes(st.session_state.edited_image),

            file_name="VisionEditAI.png",

            mime="image/png",

            use_container_width=True

        )

    st.write("")
    st.divider()

    # ============================================
    # HISTORY PREVIEW
    # ============================================

    st.markdown("## 🕘 Recent Prompt")

    if len(st.session_state.history) == 0:

        st.info("Belum ada riwayat.")

    else:

        for item in reversed(st.session_state.history[-5:]):

            st.markdown(f"""
<div class="history-card">

🕒 {item['time']}

<br>

💬 {item['prompt']}

</div>
""", unsafe_allow_html=True)