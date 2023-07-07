from io import BytesIO
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

with open('./hideandseek.png', 'rb') as f:
    img_b = f.read()
img = Image.open(BytesIO(img_b))
img.save('flag.png')
