from PIL import Image


def get_size(path):

    img = Image.open(path)

    return img.size