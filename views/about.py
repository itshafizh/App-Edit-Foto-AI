import streamlit as st
import os


def show():

    st.markdown("""
<div class="hero">

<span class="badge">
ℹ About
</span>

<h1>
VisionEdit AI
</h1>

<p>
AI Image Editing Platform
</p>

</div>
""", unsafe_allow_html=True)

    st.write("")

    left, right = st.columns([1,2])

    with left:

        if os.path.exists("assets/logo.png"):

            st.image(

                "assets/logo.png",

                use_container_width=True

            )

    with right:

        st.markdown("""

### 🚀 VisionEdit AI

VisionEdit AI adalah aplikasi editing gambar berbasis Artificial Intelligence
yang memungkinkan pengguna melakukan editing foto hanya menggunakan prompt.

Fitur utama:

- 🤖 AI Prompt Editing
- 🖼 Remove Background
- 🚀 Upscale HD
- ✨ Image Enhance
- 🎨 Anime Style
- 📷 Photo Restore
- 🎛 Manual Editor

""")

    st.divider()

    st.subheader("👨‍💻 Developer")

    st.markdown("""
<div class="glass-card">

**Framework :** Streamlit

**Language :** Python

**Version :** 1.0

</div>
""", unsafe_allow_html=True)

    st.divider()

    st.subheader("🛠 Technology")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success("Python")

    with c2:
        st.success("Streamlit")

    with c3:
        st.success("Pillow")

    with c4:
        st.success("AI API")

    st.divider()

    st.subheader("📈 Application Information")

    a, b, c = st.columns(3)

    with a:
        st.metric("Version", "1.0")

    with b:
        st.metric("Pages", "8")

    with c:
        st.metric("AI Tools", "18")

    st.divider()

    st.markdown("""
<div class="footer">

Made with ❤️ using Python & Streamlit

© 2026 VisionEdit AI

</div>
""", unsafe_allow_html=True)