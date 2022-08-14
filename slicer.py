from PIL import Image


image = Image.open('resized_ss.png')
width, height = image.size

for i in range(0, 59):
    if i <= 10:
        frame = image.crop((0, 0+height/100, width, height/2+height/100))
        frame.save(f'{i}.png')
    else:
        frame = image.crop((0, 0+height/100*(i-10), width, height/2+height/100*(i-10)))
        frame.save(f'{i}.png')