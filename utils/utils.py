from io import BytesIO


def image_to_png_bytes(image):
    """
    Encode a PIL Image into PNG bytes, suitable for st.download_button.
    Ensures the downloaded file always matches the image currently on screen.
    """

    buffer = BytesIO()

    image.save(buffer, format="PNG")

    return buffer.getvalue()