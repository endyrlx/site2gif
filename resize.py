from PIL import Image


image = Image.open("ss.png")
width, height = image.size
resized_image = image.resize((int(width/3), int(height/3)))
resized_image.show()
resized_image.save("resized_ss.png")