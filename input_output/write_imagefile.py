import sys

from PIL import Image

image = []
for arg in sys.argv[1:]:
    img = Image.open(arg)
    image.append(img)
    
if len(image) > 1:
    image[1].save(
        "costume.gif", save_all=True, append_image=[image[1]], duration=200, loop=0
    )
else:
    print("Please provide at least two image files as arguments.")