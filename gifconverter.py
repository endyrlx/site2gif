from PIL import Image

# Create the frames
frames = []
for i in range(0, 59):
    f = f"{i}.png"
    new_frame = Image.open(f)
    frames.append(new_frame)
    print("frame: ", f)


# Save into a GIF file that loops forever
frames[0].save('png_to_gif.gif', format='GIF',
               append_images=frames[0:]+list(reversed(frames[0:])),
               save_all=True,
               duration=20, loop=0)

