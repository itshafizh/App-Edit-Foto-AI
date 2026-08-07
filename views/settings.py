import streamlit as st

from utils.theme import ThemeManager


def show():

    st.markdown("""
<div class="hero">

<span class="badge">
⚙ Settings
</span>

<h1>
Application Settings
</h1>

<p>
Atur preferensi aplikasi VisionEdit AI sesuai kebutuhan Anda.
</p>

</div>
""", unsafe_allow_html=True)

    st.write("")

    # ==========================================
    # APPEARANCE
    # ==========================================

    st.subheader("🎨 Appearance")

    def _apply_theme_selection():

        st.session_state.theme = st.session_state.theme_selector

    theme_names = ThemeManager.get_theme_names()

    current_theme = st.session_state.get(
        "theme",
        ThemeManager.DEFAULT_THEME
    )

    theme = st.selectbox(

        "Theme",

        theme_names,

        index=theme_names.index(current_theme),

        key="theme_selector",

        on_change=_apply_theme_selection

    )

    accent = st.color_picker(

        "Accent Color",

        "#8B5CF6"

    )

    animation = st.toggle(

        "Enable Animation",

        True

    )

    st.divider()

    # ==========================================
    # AI SETTINGS
    # ==========================================

    st.subheader("🤖 AI Settings")

    ai_model = st.selectbox(

        "AI Model",

        [

            "VisionEdit AI",

            "FLUX.1 Kontext",

            "Stable Diffusion XL",

            "Gemini Image"

        ]

    )

    quality = st.select_slider(

        "Image Quality",

        options=[

            "Low",

            "Medium",

            "High",

            "Ultra HD"

        ],

        value="High"

    )

    creativity = st.slider(

        "Creativity",

        0,

        100,

        75

    )

    st.divider()

    # ==========================================
    # EXPORT SETTINGS
    # ==========================================

    st.subheader("💾 Export")

    export_format = st.selectbox(

        "Format",

        [

            "PNG",

            "JPG",

            "WEBP"

        ]

    )

    export_quality = st.slider(

        "Export Quality",

        10,

        100,

        95

    )

    keep_metadata = st.checkbox(

        "Keep Metadata",

        False

    )

    st.divider()

    # ==========================================
    # NOTIFICATION
    # ==========================================

    st.subheader("🔔 Notification")

    notification = st.toggle(

        "Enable Notification",

        True

    )

    auto_save = st.toggle(

        "Auto Save History",

        True

    )

    sound = st.toggle(

        "Sound Effect",

        False

    )

    st.divider()

    # ==========================================
    # BUTTON
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        if st.button(

            "💾 Save Settings",

            use_container_width=True

        ):

            st.success(
                "Pengaturan berhasil disimpan."
            )

    with col2:

        if st.button(

            "🔄 Reset",

            use_container_width=True

        ):

            st.rerun()

    st.write("")

    st.info(f"""
Theme : {theme}

AI Model : {ai_model}

Quality : {quality}

Export : {export_format}

Export Quality : {export_quality}%

Animation : {"Aktif" if animation else "Nonaktif"}
""")