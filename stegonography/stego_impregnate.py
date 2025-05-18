from PIL import Image
import numpy as np

secret = "secgs"

image = Image.open(r"C:\Users\DELL\Downloads\shinji.jpg")
image = image.convert('RGB')
image_pixels = image.load()


secret_bits_e = ''.join(f'{ord(c):08b}' for c in secret)
secret_bits_e += '00000000'  # delimiter to indicate end of the string (null byte)

print(len(secret_bits_e))


width, height = image.size
bit_index = 0

for y in range(height):
    for x in range(width):
        if bit_index >= len(secret_bits_e):
            image.save(r"C:\Users\DELL\Downloads\hi\shinji-encoded.png")
            exit()

        r, g, b = image_pixels[x,y]

        if bit_index < len(secret_bits_e):
            r = (r & ~1) | int(secret_bits_e[bit_index])
            bit_index += 1
        if bit_index < len(secret_bits_e):
            g = (g & ~1) | int(secret_bits_e[bit_index])
            bit_index += 1
        if bit_index < len(secret_bits_e):
            b = (b & ~1) | int(secret_bits_e[bit_index])
            bit_index += 1

        image_pixels[x, y] = (r, g, b)

