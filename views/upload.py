import streamlit as st
from PIL import Image
import os


def show():

    st.markdown("""
<div class="hero">

<span class="badge">
📤 Upload Image
</span>

<h1>
Upload Your Image
</h1>

<p>
Upload gambar yang ingin diedit menggunakan Artificial Intelligence.
</p>

</div>
""", unsafe_allow_html=True)

    st.write("")

    left, right = st.columns([1, 1])

    # ===========================================
    # UPLOAD
    # ===========================================

    with left:

        st.markdown("## 📂 Select Image")

        uploaded_file = st.file_uploader(

            "Drag & Drop atau Klik untuk Upload",

            type=["png", "jpg", "jpeg", "webp"]

        )

        if uploaded_file is not None:

            MAX_SIZE_BYTES = 10 * 1024 * 1024

            if uploaded_file.size > MAX_SIZE_BYTES:

                st.error(
                    "Ukuran file melebihi 10 MB. Silakan upload gambar yang lebih kecil."
                )

            else:

                image = Image.open(uploaded_file)

                st.session_state.uploaded_image = image

                save_path = os.path.join(
                    "uploads",
                    uploaded_file.name
                )

                image.save(save_path)

                st.success("✅ Upload berhasil.")

    # ===========================================
    # PREVIEW
    # ===========================================

    with right:

        st.markdown("## Preview")

        if st.session_state.uploaded_image is not None:

            st.image(
                st.session_state.uploaded_image,
                use_container_width=True
            )

        else:

            st.info(
                "Belum ada gambar."
            )

    st.write("")
    st.divider()

    # ===========================================
    # IMAGE INFORMATION
    # ===========================================

    if st.session_state.uploaded_image is not None:

        img = st.session_state.uploaded_image

        width, height = img.size

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Width",
                f"{width}px"
            )

        with c2:

            st.metric(
                "Height",
                f"{height}px"
            )

        with c3:

            st.metric(
                "Mode",
                img.mode
            )

    st.write("")
    st.divider()

    # ===========================================
    # QUICK ACTION
    # ===========================================

    st.markdown("## ⚡ Quick Action")

    q1, q2, q3 = st.columns(3)

    with q1:

        if st.button(
            "🤖 AI Prompt",
            use_container_width=True
        ):
            if st.session_state.uploaded_image is None:
                st.warning("Silakan upload gambar terlebih dahulu.")
            else:
                st.session_state.page = "AI Prompt"
                st.rerun()

    with q2:

        if st.button(
            "✨ AI Tools",
            use_container_width=True
        ):
            if st.session_state.uploaded_image is None:
                st.warning("Silakan upload gambar terlebih dahulu.")
            else:
                st.session_state.page = "AI Tools"
                st.rerun()

    with q3:

        if st.button(
            "🎨 Manual Editor",
            use_container_width=True
        ):
            if st.session_state.uploaded_image is None:
                st.warning("Silakan upload gambar terlebih dahulu.")
            else:
                st.session_state.page = "Manual Editor"
                st.rerun()

    st.write("")
    st.divider()

    # ===========================================
    # SUPPORTED FORMAT
    # ===========================================

    st.markdown("## 📄 Supported Format")

    f1, f2, f3, f4 = st.columns(4)

    with f1:
        st.success("PNG")

    with f2:
        st.success("JPG")

    with f3:
        st.success("JPEG")

    with f4:
        st.success("WEBP")

    st.write("")
    st.divider()

    # ===========================================
    # TIPS
    # ===========================================

    st.markdown("## 💡 Tips")

    st.info("""
📌 Gunakan gambar dengan resolusi tinggi.

📌 Hindari gambar yang blur.

📌 Format terbaik adalah PNG.

📌 Maksimal ukuran file 10 MB.
    """)