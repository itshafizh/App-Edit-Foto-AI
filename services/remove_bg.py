from rembg import remove
from PIL import Image
import io


def remove_background(image: Image.Image):

    if image.mode != "RGBA":
        image = image.convert("RGBA")

    input_buffer = io.BytesIO()
    image.save(input_buffer, format="PNG")

    output = remove(input_buffer.getvalue())

    result = Image.open(io.BytesIO(output))

    return result