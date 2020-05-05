from PIL import ImageGrab

image = ImageGrab.grabclipboard()
print(type(image))
print(image)
image.show()