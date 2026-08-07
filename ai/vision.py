from PIL import Image
from ai.gemini_client import client


def describe_image(image_path):

    image = Image.open(image_path)

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[
            "Describe this image in detail.",
            image
        ]
    )

    return response.text