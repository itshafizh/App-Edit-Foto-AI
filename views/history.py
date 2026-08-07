import streamlit as st
from PIL import Image
import io


def show():

    st.markdown("""
<div class="hero">

<span class="badge">
🕘 History
</span>

<h1>
Editing History
</h1>

<p>
Semua aktivitas editing akan tersimpan di halaman ini.
</p>

</div>
""", unsafe_allow_html=True)

    st.write("")

    if "history" not in st.session_state:

        st.session_state.history = []

    # ==========================================
    # EMPTY HISTORY
    # ==========================================

    if len(st.session_state.history) == 0:

        st.info(
            "Belum ada riwayat editing."
        )

        st.image(
            "assets/history.png",
            width=250
        ) if False else None

        return

    # ==========================================
    # HEADER
    # ==========================================

    total = len(st.session_state.history)

    col1, col2 = st.columns([3,1])

    with col1:

        st.subheader(
            f"📂 Total History : {total}"
        )

    with col2:

        if st.button(
            "🗑 Hapus Semua",
            use_container_width=True
        ):

            st.session_state.history.clear()

            st.rerun()

    st.write("")

    # ==========================================
    # LIST HISTORY
    # ==========================================

    for index, item in enumerate(
        reversed(st.session_state.history)
    ):

        with st.container(border=True):

            left, right = st.columns([1,2])

            with left:

                if "image" in item:

                    st.image(
                        item["image"],
                        use_container_width=True
                    )

                else:

                    if st.session_state.uploaded_image:

                        st.image(
                            st.session_state.uploaded_image,
                            use_container_width=True
                        )

            with right:

                st.markdown(
                    f"### 📝 Prompt"
                )

                st.write(
                    item.get(
                        "prompt",
                        "-"
                    )
                )

                st.markdown(
                    f"### 🕒 Waktu"
                )

                st.write(
                    item.get(
                        "time",
                        "-"
                    )
                )

                st.markdown(
                    f"### 🏷 Status"
                )

                st.success("Completed")

        st.divider()

    # ==========================================
    # DOWNLOAD HISTORY
    # ==========================================

    st.subheader("📥 Export History")

    if st.button(
        "Generate Report",
        use_container_width=True
    ):

        report = ""

        report += "VISIONEDIT AI\n"

        report += "History Report\n\n"

        for i, item in enumerate(
            st.session_state.history
        ):

            report += f"{i+1}\n"

            report += f"Prompt : {item.get('prompt')}\n"

            report += f"Waktu : {item.get('time')}\n"

            report += "\n"

        st.download_button(

            "⬇ Download TXT",

            report,

            file_name="history.txt",

            use_container_width=True

        )

    st.write("")
    st.divider()

    # ==========================================
    # SUMMARY
    # ==========================================

    st.subheader("📊 Summary")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Total Edit",
            len(st.session_state.history)
        )

    with c2:

        st.metric(
            "AI Prompt",
            len(st.session_state.history)
        )

    with c3:

        st.metric(
            "Success",
            "100%"
        )

    st.write("")
    st.divider()

    st.info("""
💡 Semua hasil editing akan otomatis muncul di halaman ini.

Riwayat meliputi:

- Prompt AI

- Waktu Editing

- Preview Gambar

- Status Editing

- Export History
""")