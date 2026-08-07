import streamlit as st
import os
from PIL import Image


def show():

    st.markdown("""
    <div class="hero">

        <span class="badge">
            🖼 Gallery
        </span>

        <h1>
            My AI Gallery
        </h1>

        <p>
            Semua hasil editing AI tersimpan di sini.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    folder = "outputs"

    if not os.path.exists(folder):

        os.makedirs(folder)

    images = [

        file

        for file in os.listdir(folder)

        if file.lower().endswith(
            (".png",".jpg",".jpeg",".webp")
        )

    ]

    if len(images) == 0:

        st.info(
            "Belum ada gambar."
        )

        return

    columns = st.columns(3)

    for index, file in enumerate(images):

        path = os.path.join(

            folder,

            file

        )

        image = Image.open(path)

        with columns[index % 3]:

            st.image(

                image,

                use_container_width=True

            )

            st.caption(file)

            with open(path,"rb") as img:

                st.download_button(

                    "⬇ Download",

                    img,

                    file_name=file,

                    key=file,

                    use_container_width=True

                )

            if st.button(

                "🗑 Delete",

                key=f"delete_{file}",

                use_container_width=True

            ):

                os.remove(path)

                st.rerun()