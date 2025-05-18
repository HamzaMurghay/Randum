from PIL import Image

img = Image.open(r"C:\Users\DELL\Downloads\shinji-encoded.png")
img = img.convert('RGB')
pixels = img.load()

width, height = img.size
bits = ''

for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        bits += str(r & 1)
        bits += str(g & 1)
        bits += str(b & 1)


# Group into 8-bit chunks
chars = [chr(int(bits[i:i + 8], 2)) for i in range(0, len(bits), 8)]

# Stop at the null byte
secret = ''
for c in chars:
    if c == '\x00':
        break
    secret += c

print(type(secret), len(secret), secret)

