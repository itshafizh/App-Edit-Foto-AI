import os
import shutil


def save_upload(uploaded_file):

    os.makedirs("uploads", exist_ok=True)

    filepath = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(filepath, "wb") as f:
        shutil.copyfileobj(uploaded_file, f)

    return filepath