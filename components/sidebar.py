import streamlit as st
import os

NAV_ITEMS = [
    ("🏠", "Home"),
    ("📤", "Upload"),
    ("🤖", "AI Prompt"),
    ("✨", "AI Tools"),
    ("🎨", "Manual Editor"),
    ("🕒", "History"),
    ("⚙", "Settings"),
    ("ℹ️", "About"),
]

def render_sidebar():

    if "page" not in st.session_state:
        st.session_state.page = "Home"

    with st.sidebar:

        st.markdown("<br>", unsafe_allow_html=True)

        if os.path.exists("assets/logo.png"):
            st.image("assets/logo.png", width=170)

        st.markdown("""
<h2 style="text-align:center;">VisionEdit AI</h2>
<p style="text-align:center;color:#CBD5E1;">
AI Image Editing Platform
</p>
""", unsafe_allow_html=True)

        st.divider()

        for icon, label in NAV_ITEMS:

            active = st.session_state.page == label

            if st.button(
                f"{icon} {label}",
                key=f"nav_{label}",
                use_container_width=True,
                type="primary" if active else "secondary",
            ):
                st.session_state.page = label
                st.rerun()

        st.divider()

        st.markdown("""
<div class="premium-card">

<h4>🚀 Premium</h4>

<p>
✔ Unlimited Prompt<br>
✔ Faster AI<br>
✔ 4K Export<br>
✔ No Watermark
</p>

</div>
""", unsafe_allow_html=True)

    return st.session_state.page