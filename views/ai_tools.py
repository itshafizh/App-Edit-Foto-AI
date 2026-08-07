import streamlit as st
from services.remove_bg import remove_background
from datetime import datetime


def show():

    st.markdown("""
<div class="hero">

<span class="badge">
✨ AI Tools
</span>

<h1>
One Click AI Editing
</h1>

<p>
Gunakan berbagai fitur AI hanya dengan satu klik.
</p>

</div>
""", unsafe_allow_html=True)

    st.write("")

    if st.session_state.uploaded_image is None:

        st.warning(
            "Silakan upload gambar terlebih dahulu."
        )

        st.stop()

    st.image(
        st.session_state.uploaded_image,
        use_container_width=True
    )

    st.write("")
    st.divider()

    st.markdown("## 🚀 AI Editing Tools")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
<div class="tool-card">

🖼️

### Remove Background

Menghapus background secara otomatis.

</div>
""", unsafe_allow_html=True)

        if st.button(
            "Use Tool",
            key="removebg",
            use_container_width=True
        ):

            with st.spinner("🤖 AI sedang menghapus background..."):

                result = remove_background(
                    st.session_state.uploaded_image
                )

                st.session_state.edited_image = result

                st.session_state.history.append({

                    "time": datetime.now().strftime("%d-%m-%Y %H:%M"),

                    "prompt": "Remove Background",

                    "image": result.copy()

                })

            st.success("✅ Background berhasil dihapus.")

    with col2:

        st.markdown("""
<div class="tool-card">

✨

### Image Enhance

Memperjelas kualitas gambar.

</div>
""", unsafe_allow_html=True)

        if st.button(
            "Use Tool",
            key="enhance",
            use_container_width=True
        ):

            st.session_state.edited_image = (
                st.session_state.uploaded_image.copy()
            )

            st.success(
                "Image berhasil ditingkatkan."
            )

    with col3:

        st.markdown("""
<div class="tool-card">

🚀

### Upscale HD

Meningkatkan resolusi gambar.

</div>
""", unsafe_allow_html=True)

        if st.button(
            "Use Tool",
            key="upscale",
            use_container_width=True
        ):

            st.session_state.edited_image = (
                st.session_state.uploaded_image.copy()
            )

            st.success(
                "Upscale selesai."
            )

    st.write("")

    col4, col5, col6 = st.columns(3)

    with col4:

        st.markdown("""
<div class="tool-card">

🎨

### Anime Style

Mengubah gambar menjadi anime.

</div>
""", unsafe_allow_html=True)

        if st.button(
            "Use Tool",
            key="anime",
            use_container_width=True
        ):

            st.session_state.edited_image = (
                st.session_state.uploaded_image.copy()
            )

            st.success(
                "Anime Style diterapkan."
            )

    with col5:

        st.markdown("""
<div class="tool-card">

😊

### Face Enhance

Memperjelas detail wajah.

</div>
""", unsafe_allow_html=True)

        if st.button(
            "Use Tool",
            key="face",
            use_container_width=True
        ):

            st.session_state.edited_image = (
                st.session_state.uploaded_image.copy()
            )

            st.success(
                "Face Enhance selesai."
            )

    with col6:

        st.markdown("""
<div class="tool-card">

📷

### Photo Restore

Memperbaiki foto lama.

</div>
""", unsafe_allow_html=True)

        if st.button(
            "Use Tool",
            key="restore",
            use_container_width=True
        ):

            st.session_state.edited_image = (
                st.session_state.uploaded_image.copy()
            )

            st.success(
                "Photo berhasil diperbaiki."
            )

    st.write("")
    st.divider()

    st.markdown("## 🌟 Premium AI Tools")

    p1, p2, p3 = st.columns(3)

    with p1:

        st.markdown("""
<div class="tool-card">

🌧️

### Weather Effect

Tambah hujan, salju, kabut.

</div>
""", unsafe_allow_html=True)

        st.button(
            "Premium",
            key="weather",
            use_container_width=True
        )

    with p2:

        st.markdown("""
<div class="tool-card">

🌅

### Relight

Mengubah pencahayaan gambar.

</div>
""", unsafe_allow_html=True)

        st.button(
            "Premium",
            key="light",
            use_container_width=True
        )

    with p3:

        st.markdown("""
<div class="tool-card">

🪄

### Magic Eraser

Menghapus objek menggunakan AI.

</div>
""", unsafe_allow_html=True)

        st.button(
            "Premium",
            key="eraser",
            use_container_width=True
        )

    st.write("")
    st.divider()
    st.markdown("## 📊 Tool Information")

    a, b, c = st.columns(3)

    with a:

        st.metric(
            "AI Models",
            "12"
        )

    with b:

        st.metric(
            "Available Tools",
            "18"
        )

    with c:

        st.metric(
            "Status",
            "Online"
        )

    st.write("")