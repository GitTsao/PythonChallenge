from PIL import Image

im = Image.open('oxygen.png')
box = im.crop((0,45,629,52 ))
print("fuck you")
box.show()
