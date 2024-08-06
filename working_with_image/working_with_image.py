from PIL import Image
#pillow

mac=Image.open('working_with_image/example.jpg')
type(mac)
print(mac.filename)
print(mac.format_description)
mac.crop()