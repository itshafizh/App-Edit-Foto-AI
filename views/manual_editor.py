import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
from datetime import datetime

from utils.utils import image_to_png_bytes

EDITOR_DEFAULTS = {
    "me_brightness": 1.0,
    "me_contrast": 1.0,
    "me_saturation": 1.0,
    "me_sharpness": 1.0,
    "me_rotate": 0,
    "me_flip_h": False,
    "me_flip_v": False,
}


def _reset_editor():
    """
    Resets every editor control to its default value.
    Also clears st.session_state.edited_image, which is the same shared
    slot used by the AI Prompt and History pages — intentional, since the
    task requires Reset to clear all editor state, not just this page's.
    """

    for key, value in EDITOR_DEFAULTS.items():

        st.session_state[key] = value

    st.session_state.edited_image = None


def show():

    st.markdown("""
<div class="hero">

<span class="badge">
🎨 Manual Editor
</span>

<h1>
Manual Image Editor
</h1>

<p>
Edit gambar secara manual menggunakan berbagai pengaturan.
</p>

</div>
""", unsafe_allow_html=True)

    st.write("")

    if st.session_state.uploaded_image is None:

        st.warning(
            "Silakan upload gambar terlebih dahulu."
        )

        st.stop()

    image = st.session_state.uploaded_image.copy()

    left, right = st.columns([1,2])

    # ==========================================
    # CONTROL PANEL
    # ==========================================

    with left:

        st.markdown("## 🎛 Editor")

        brightness = st.slider(
            "Brightness",
            0.0,
            2.0,
            EDITOR_DEFAULTS["me_brightness"],
            0.1,
            key="me_brightness"
        )

        contrast = st.slider(
            "Contrast",
            0.0,
            2.0,
            EDITOR_DEFAULTS["me_contrast"],
            0.1,
            key="me_contrast"
        )

        saturation = st.slider(
            "Saturation",
            0.0,
            2.0,
            EDITOR_DEFAULTS["me_saturation"],
            0.1,
            key="me_saturation"
        )

        sharpness = st.slider(
            "Sharpness",
            0.0,
            5.0,
            EDITOR_DEFAULTS["me_sharpness"],
            0.1,
            key="me_sharpness"
        )

        rotate = st.slider(
            "Rotate",
            -180,
            180,
            EDITOR_DEFAULTS["me_rotate"],
            key="me_rotate"
        )

        flip_h = st.checkbox(
            "Flip Horizontal",
            EDITOR_DEFAULTS["me_flip_h"],
            key="me_flip_h"
        )

        flip_v = st.checkbox(
            "Flip Vertical",
            EDITOR_DEFAULTS["me_flip_v"],
            key="me_flip_v"
        )

    # ==========================================
    # IMAGE PROCESSING
    # ==========================================

    image = ImageEnhance.Brightness(
        image
    ).enhance(brightness)

    image = ImageEnhance.Contrast(
        image
    ).enhance(contrast)

    image = ImageEnhance.Color(
        image
    ).enhance(saturation)

    image = ImageEnhance.Sharpness(
        image
    ).enhance(sharpness)

    image = image.rotate(
        rotate,
        expand=True
    )

    if flip_h:

        image = ImageOps.mirror(
            image
        )

    if flip_v:

        image = ImageOps.flip(
            image
        )

    # ==========================================
    # PREVIEW
    # ==========================================

    with right:

        st.markdown("## 🖼 Preview")

        before, after = st.columns(2)

        with before:

            st.markdown("### Original")

            st.image(
                st.session_state.uploaded_image,
                use_container_width=True
            )

        with after:

            st.markdown("### Edited")

            st.image(
                image,
                use_container_width=True
            )

    st.write("")
    st.divider()

    st.markdown("## 📦 Quick Edit")

    q1, q2, q3 = st.columns(3)

    with q1:

        st.button(
            "Reset",
            use_container_width=True,
            on_click=_reset_editor
        )

    with q2:

        if st.button(
            "Apply",
            use_container_width=True
        ):

            st.session_state.edited_image = image.copy()

            st.session_state.history.append({

                "time": datetime.now().strftime("%d-%m-%Y %H:%M"),

                "prompt": "Manual Editor",

                "image": image.copy()

            })

            st.success(
                "Perubahan berhasil diterapkan."
            )

    with q3:

        if st.session_state.edited_image is not None:

            st.download_button(

                "Download",

                data=image_to_png_bytes(image),

                file_name="VisionEditAI.png",

                mime="image/png",

                use_container_width=True

            )

        else:

            st.button(
                "Download",
                use_container_width=True,
                disabled=True
            )

    st.write("")
    st.divider()
    # ==========================================
    # IMAGE INFORMATION
    # ==========================================

    width, height = image.size

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
            "Color Mode",
            image.mode
        )

    st.write("")
    st.divider()

    st.markdown("## 💡 Editing Tips")

    st.info("""
- Brightness untuk mengatur tingkat terang.

- Contrast untuk memperjelas perbedaan warna.

- Saturation untuk mengatur intensitas warna.

- Sharpness untuk mempertajam gambar.

- Rotate untuk memutar gambar.

- Flip digunakan untuk membalik gambar.
""")