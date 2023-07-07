from PIL import Image
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
test = load_image("./test.png")

print(is_close(test, pickaxe))
print(closeness(test, pickaxe))
print(distance(test, pickaxe), distance(test, sword))

