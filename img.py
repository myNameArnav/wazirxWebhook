from PIL import Image, ImageDraw, ImageFont
from parse import parseJSON

# * font declaration
roboto = ImageFont.truetype("fonts\RobotoMono.ttf", 30)
montserrat = ImageFont.truetype("fonts\Montserrat.ttf", 30)
bebas = ImageFont.truetype("fonts\BebasNeue.ttf", 45)
slab = ImageFont.truetype("fonts\RobotoSlab.ttf", 20)

width = 1280
height = 720

# * imported from parse.py
name, lastPrice, openPrice = parseJSON("btcusdt")
lastPrice, openPrice = float(lastPrice), float(openPrice)
change = openPrice - lastPrice
perChange = str(round(((lastPrice - openPrice) / lastPrice)* 100, 2))

img = Image.new(mode = "RGBA", size = (width, height), color = (54, 57, 63, 100))
draw = ImageDraw.Draw(img)

space = " " * 20
moreSpace = " " * 25
spaceFromTop = 60

hdr = "Name" + space + "Price" + space + "Change" + space + "%"
draw.text((10,5), hdr, font = bebas, fill = (225,225,225), align= 'right')

txt = name + moreSpace + str(lastPrice) + moreSpace + str(change) + moreSpace + str(perChange)

draw.text((10,spaceFromTop), txt, font = slab, fill=(255,255,255), align = 'right')

img.save("picture.png")

img.show()