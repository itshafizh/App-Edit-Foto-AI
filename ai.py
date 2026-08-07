import requests
from PIL import Image
from io import BytesIO
from config import HF_TOKEN, MODEL


class VisionAI:

    def __init__(self):

        self.API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL}"

        self.headers = {
            "Authorization": f"Bearer {HF_TOKEN}"
        }

    def generate(self, image, prompt):

        buffer = BytesIO()

        image.save(
            buffer,
            format="PNG"
        )

        buffer.seek(0)

        files = {

            "image": buffer.getvalue()

        }

        data = {

            "inputs": prompt

        }

        response = requests.post(

            self.API_URL,

            headers=self.headers,

            files=files,

            data=data

        )

        if response.status_code == 200:

            img = Image.open(
                BytesIO(response.content)
            )

            return img

        raise Exception(

            response.text

        )