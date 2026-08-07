import streamlit as st
import os

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="VisionEdit AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# LOAD CSS
# =====================================

if os.path.exists("style.css"):
    with open("style.css", "r", encoding="utf-8") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================
# CREATE FOLDER
# =====================================

os.makedirs("assets", exist_ok=True)
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# =====================================
# SESSION STATE
# =====================================

default_state = {
    "uploaded_image": None,
    "edited_image": None,
    "history": [],
    "theme": "Purple Gradient",
    "language": "Indonesia"
}

for key, value in default_state.items():
    if key not in st.session_state:
        st.session_state[key] = value

# =====================================
# RUNTIME THEME
# =====================================

from utils.theme import ThemeManager

ThemeManager.inject(st.session_state.theme)

# =====================================
# IMPORT VIEWS
# =====================================

from views import (
    home,
    upload,
    ai_prompt,
    ai_tools,
    manual_editor,
    history,
    settings,
    about
)

from components.sidebar import render_sidebar

# =====================================
# SIDEBAR
# =====================================

page = render_sidebar()

# =====================================
# ROUTING
# =====================================

PAGE_HANDLERS = {
    "Home": home.show,
    "Upload": upload.show,
    "AI Prompt": ai_prompt.show,
    "AI Tools": ai_tools.show,
    "Manual Editor": manual_editor.show,
    "History": history.show,
    "Settings": settings.show,
    "About": about.show,
}

# Falls back to Home instead of silently rendering nothing
# if st.session_state.page ever holds an unrecognized value.
handler = PAGE_HANDLERS.get(page, home.show)

handler()