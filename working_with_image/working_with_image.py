from PIL import Image
#pillow

mac=Image.open('working_with_image/example.jpg')
type(mac)
print(mac.filename)
print(mac.format_description)
print(mac.crop((0,0,100,100)))

pencils=Image.open('working_with_image/pencils.jpg')
print(pencils.size)
x=0
y=0
w=1950/3
h=1300/10
print(pencils.crop((x,y,w,h)).show())

computer=max.crop(x,y,w,h)
mac.paste(im=computer,box=(0,0))