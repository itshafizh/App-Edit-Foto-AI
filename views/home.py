import os
import streamlit as st


def show():

    # ======================================================
    # HERO SECTION
    # ======================================================

    left, right = st.columns([1.35, 1])

    with left:

        st.markdown(
            """
<span class="badge">
🤖 AI Powered Image Editor
</span>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<div class="hero-title-small">
Welcome to
</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<div class="hero-title">
Vision<span>Edit AI</span>
</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<div class="hero-subtitle">

Edit your photos using the power of Artificial Intelligence.

<br><br>

Remove background, enhance image quality,
upscale photos, restore old images,
and generate amazing edits using simple prompts.

</div>
""",
            unsafe_allow_html=True
        )

        st.write("")

        b1, b2 = st.columns([1, 1])

        with b1:

            if st.button(
                "🚀 Get Started",
                use_container_width=True
            ):
                st.session_state.page = "Upload"
                st.rerun()

        with b2:

            if st.button(
                "📖 Learn More",
                use_container_width=True
            ):
                st.session_state.page = "About"
                st.rerun()

    with right:

        if os.path.exists("assets/robot.png"):

            st.image(
                "assets/robot.png",
                use_container_width=True
            )

        else:

            st.warning(
                "robot.png belum tersedia"
            )

    st.write("")
    st.divider()

    # ======================================================
    # POPULAR FEATURES
    # ======================================================

    st.markdown("## ✨ Popular Features")

    st.caption(
        "Most frequently used AI tools by VisionEdit users."
    )

    st.write("")

    features = [

        ("🤖", "AI Prompt", "Edit images using natural language prompts."),

        ("🖼️", "Remove BG", "Automatically remove image backgrounds."),

        ("✨", "Enhance", "Improve image quality instantly."),

        ("🎨", "Anime", "Convert photos into anime style."),

        ("🚀", "Upscale", "Increase image resolution without losing quality."),

        ("😊", "Face AI", "Enhance face details automatically."),

        ("📷", "Restore", "Repair and restore old photographs."),

        ("🌄", "Background", "Replace photo backgrounds using AI.")

    ]

    row1 = st.columns(4)

    for col, item in zip(row1, features[:4]):

        icon, title, desc = item

        with col:

            st.markdown(
                f"""
<div class="feature-card">

<div class="icon">
{icon}
</div>

<h3>{title}</h3>

<p>{desc}</p>

</div>
""",
                unsafe_allow_html=True
            )

    st.write("")

    row2 = st.columns(4)

    for col, item in zip(row2, features[4:]):

        icon, title, desc = item

        with col:

            st.markdown(
                f"""
<div class="feature-card">

<div class="icon">
{icon}
</div>

<h3>{title}</h3>

<p>{desc}</p>

</div>
""",
                unsafe_allow_html=True
            )

    st.write("")
    st.divider()
    
    # ======================================================
    # BEFORE & AFTER
    # ======================================================

    st.markdown("## 🖼 Before & After")

    st.caption(
        "See how VisionEdit AI transforms your images."
    )

    st.write("")

    before, after = st.columns(2)

    with before:

        st.markdown(
            """
<div class="image-card">
<h3>Original Image</h3>
</div>
""",
            unsafe_allow_html=True
        )

        if os.path.exists("assets/sample/before.jpg"):

            st.image(
                "assets/sample/before.jpg",
                use_container_width=True
            )

        else:

            st.info(
                "assets/sample/before.jpg belum tersedia"
            )

    with after:

        st.markdown(
            """
<div class="image-card">
<h3>AI Result</h3>
</div>
""",
            unsafe_allow_html=True
        )

        if os.path.exists("assets/sample/after.jpg"):

            st.image(
                "assets/sample/after.jpg",
                use_container_width=True
            )

        else:

            st.info(
                "assets/sample/after.jpg belum tersedia"
            )

    st.write("")
    st.divider()

    # ======================================================
    # STATISTICS
    # ======================================================

    st.markdown("## 📊 VisionEdit Statistics")

    st.caption(
        "Trusted by thousands of creators."
    )

    st.write("")

    stat1, stat2, stat3, stat4 = st.columns(4)

    stats = [

        ("12K+", "Images Edited"),

        ("6K+", "AI Prompts"),

        ("99%", "Accuracy"),

        ("24/7", "Online")

    ]

    for col, item in zip(
        [stat1, stat2, stat3, stat4],
        stats
    ):

        value, title = item

        with col:

            st.markdown(
                f"""
<div class="stats-card">

<h1>{value}</h1>

<p>{title}</p>

</div>
""",
                unsafe_allow_html=True
            )

    st.write("")
    st.divider()

    # ======================================================
    # WHY CHOOSE US
    # ======================================================

    st.markdown("## 💜 Why Choose VisionEdit AI")

    st.write("")

    why1, why2, why3 = st.columns(3)

    why_data = [

        (
            "⚡",
            "Fast Processing",
            "Edit your images within seconds using optimized AI models."
        ),

        (
            "🎯",
            "High Accuracy",
            "Advanced AI understands your prompt naturally."
        ),

        (
            "☁",
            "Cloud Based",
            "No high-end computer required. Everything runs in the cloud."
        )

    ]

    for col, item in zip(
        [why1, why2, why3],
        why_data
    ):

        icon, title, desc = item

        with col:

            st.markdown(
                f"""
<div class="why-card">

<div class="icon">
{icon}
</div>

<h3>{title}</h3>

<p>{desc}</p>

</div>
""",
                unsafe_allow_html=True
            )

    st.write("")
    st.divider()

    # ======================================================
    # HOW IT WORKS
    # ======================================================

    st.markdown("## 🚀 How It Works")

    st.caption(
        "Only four simple steps to create amazing AI images."
    )

    st.write("")

    step1, step2, step3, step4 = st.columns(4)

    steps = [

        (
            "①",
            "Upload",
            "Upload your image."
        ),

        (
            "②",
            "Choose Tool",
            "Select AI Tool or Prompt."
        ),

        (
            "③",
            "AI Process",
            "VisionEdit AI processes your image."
        ),

        (
            "④",
            "Download",
            "Save your final result."
        )

    ]

    for col, item in zip(
        [step1, step2, step3, step4],
        steps
    ):

        number, title, desc = item

        with col:

            st.markdown(
                f"""
<div class="tool-card">

<div class="icon">
{number}
</div>

<h3>{title}</h3>

<p>{desc}</p>

</div>
""",
                unsafe_allow_html=True
            )

    st.write("")
    st.divider()

    # ======================================================
    # FAQ
    # ======================================================

    st.markdown("## ❓ Frequently Asked Questions")

    with st.expander("Is VisionEdit AI free?"):

        st.write(
            """
            Yes. VisionEdit AI provides a free version
            with several AI editing tools.
            """
        )

    with st.expander("Do I need a powerful computer?"):

        st.write(
            """
            No. Everything runs on cloud-based AI.
            """
        )

    with st.expander("Can I download the result?"):

        st.write(
            """
            Absolutely. Every edited image can be downloaded.
            """
        )

    with st.expander("Which image formats are supported?"):

        st.write(
            """
            JPG, JPEG, PNG and WEBP.
            """
        )

    st.write("")
    st.divider()

    # ======================================================
    # CALL TO ACTION
    # ======================================================

    st.markdown(
        """
<div class="glass-card">

<h2 style="text-align:center;color:white;">
Ready to Create Amazing Images?
</h2>

<p style="text-align:center;">

Start editing your photos today
with VisionEdit AI.

</p>

</div>
""",
        unsafe_allow_html=True
    )

    center1, center2, center3 = st.columns([1,2,1])

    with center2:

        st.button(
            "🚀 Start Editing Now",
            use_container_width=True
        )
        st.session_state.page = "Upload"
        

    st.write("")
    st.divider()

    # ======================================================
    # FOOTER
    # ======================================================

    st.markdown(
        """
<div class="footer">

<h2>

✨ VisionEdit AI

</h2>

<p>

AI Image Editing Platform

</p>

<br>

<p>

Create • Edit • Enhance • Inspire

</p>

<br>

<p>

Built with ❤️ using
Streamlit & Artificial Intelligence

</p>

<br>

<p>

Version 2.0

</p>

<br>

<p style="font-size:13px;opacity:.7;">

© 2026 VisionEdit AI.
All Rights Reserved.

</p>

</div>
""", unsafe_allow_html=True
    )