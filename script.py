from PIL import Image
import potrace
import numpy as np

# Load the image
file_path = './image.png'
bitmap = Image.open(file_path)

# Convert the image to a binary bitmap using a threshold
bitmap = bitmap.convert('L')  # Convert to grayscale
bw = np.array(bitmap)
bw = bw < 128  # Apply threshold

# Create a bitmap from the array
bmp = potrace.Bitmap(bw)
path = bmp.trace()

# Convert the path to SVG
svg = path.to_svg()
svg_path = '/mnt/data/ui_designer_icon.svg'
with open(svg_path, "w") as f:
    f.write(svg)

svg_path

