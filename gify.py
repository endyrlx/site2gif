from selenium import webdriver
from selenium.webdriver import ChromeOptions
from PIL import Image
import sys, os, time

dontforgettodelete = []

def screenshot():
    options = ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1024, (768 * 2))
    url = str(sys.argv[1])
    driver.get(url)
    driver.save_screenshot('site.png')
    driver.quit()
    dontforgettodelete.append("site.png")

def resize():
    image = Image.open("site.png")
    width, height = image.size
    resized_image = image.resize((int(width / 3), int(height / 3)))
    resized_image.save("resized_site.png")
    dontforgettodelete.append("resized_site.png")

def slicer():
    image = Image.open('resized_site.png')
    width, height = image.size

    for i in range(0, 59):
        if i <= 10:
            frame = image.crop((0, 0 + height / 100, width, height / 2 + height / 100))
            frame.save(f'{i}.png')
            dontforgettodelete.append(f'{i}.png')
        else:
            frame = image.crop((0, 0 + height / 100 * (i - 10), width, height / 2 + height / 100 * (i - 10)))
            frame.save(f'{i}.png')
            dontforgettodelete.append(f'{i}.png')

def gifconverter():
    frames = []
    for i in range(0, 59):
        f = f'{i}.png'
        new_frame = Image.open(f)
        frames.append(new_frame)

    frames[0].save('site.gif', format='GIF',
                   append_images=frames[0:] + list(reversed(frames[0:])),
                   save_all=True,
                   duration=20, loop=0)


def cleaner():
    for file in dontforgettodelete:
        os.remove(file)

    print("Deleted temporary files: ", dontforgettodelete)

if __name__ == '__main__':
    print("Working...")
    print("Taking screenshot...")
    screenshot()
    print("Resizing...")
    resize()
    print("Slicing resized screenshot on frames...")
    slicer()
    print("Converting frames into GIF...")
    gifconverter()
    print("Done!")
    print("Deliting temporary files...")

    cleaner()


