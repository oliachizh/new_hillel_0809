image_name= 'sign.png'
with open(image_name, 'rb') as f:
    image_bytes = f.read()

with open('new_image.png', 'wb') as f:
    f.write(image_bytes)