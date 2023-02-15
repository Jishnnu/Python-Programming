"""
Write a python program to perform basic functions on an image.

"""

from PIL import Image

img = Image.open('C:/Users/jishn/Documents/Programming/Python/Image_Handling/sample.jpg')

print("\nFILENAME :", img.filename)
print("IMAGE FORMAT :", img.format)
print("IMAGE SIZE :", img.size)

width, height = img.size
print(f"Width : {width}\nHeight : {height}")

img = img.resize((int(width * 2), int(height * 2)))
img.save('C:/Users/jishn/Documents/Programming/Python/Image_Handling/resized_image.jpg')

img = img.transpose(Image.FLIP_TOP_BOTTOM)
img.save('C:/Users/jishn/Documents/Programming/Python/Image_Handling/flipped_image.jpg')

img = img.rotate(45)
img.save('C:/Users/jishn/Documents/Programming/Python/Image_Handling/rotated_image.jpg')