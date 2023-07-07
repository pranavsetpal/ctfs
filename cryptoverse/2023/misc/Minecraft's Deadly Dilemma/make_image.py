import PIL
from PIL import Image
import base64
import numpy as np

def load_image(img: str):
    with open(img, 'rb') as f:
        img = Image.open(f)
        img = img.convert('L')
        return np.asarray(img)

def distance(x, y):
    return np.linalg.norm(x - y)

def is_close(inp, x):
    if inp.shape != x.shape:
        return False
    return np.sqrt(np.sum(np.abs(inp - x))) < 474

def closeness(inp, x):
    if inp.shape != x.shape:
        return False
    return np.sqrt(np.sum(np.abs(inp - x)))


sword = load_image("./sword.png")
pickaxe = load_image("./pickaxe.png")

# test = (sword + 0.1*(pickaxe-sword)).clip(min=0, max=255).round()
test = (pickaxe + 0.999*(sword-pickaxe)).clip(min=0, max=255).round()

# print(np.array_equal(test, test.astype(int)))

print(closeness(test, pickaxe)) #464
print(distance(test, pickaxe), distance(test, sword)) # 6403, 1041

test_image = Image.fromarray(test)
test_image = test_image.convert('L')
test_image.save('test.png')

