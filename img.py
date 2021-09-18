
def responseImg(rates):
    from os import path
    from PIL import Image, ImageDraw, ImageFont
    from parse import parseJSON

# * font declaration

    # roboto = ImageFont.truetype("fonts\RobotoMono.ttf", 30)
    # montserrat = ImageFont.truetype("fonts\Montserrat.ttf", 30)
    # bebas = ImageFont.truetype("fonts\BebasNeue.ttf", 45)
    # slab = ImageFont.truetype("fonts\RobotoSlab.ttf", 20)
    HackNF = ImageFont.FreeTypeFont(
        path.normpath("fonts/HackNF_Regular.ttf"), 45) #for Os compatibly 

    width = 1280
    # 75 for each item in list and 200 for padding
    height = len(rates)*75 + 200


# * Creating a Image

    img = Image.new(mode="RGBA", size=(
        width, height), color=(50, 53, 59, 100))

    draw = ImageDraw.Draw(img)

# * individual List for each Column

    nameList = "Name\n"
    lastPriceList = "Price\n"
    up_DownList = "Change\n"
    perChangeList = "%\n"
    iconsList = "\n"
    colors = (245, 239, 237)
    marginTop = 100

    draw.text((50, marginTop), iconsList, font=HackNF, fill=(250, 159, 66), align='left')  # for the  coin Icon in the First Row


# * imported from parse.py

    for i in rates:
        name, lastPrice, openPrice, uporDown, arrow, colorFill, perChange = rates[i]

        marginTop += 67
        draw.text((50, marginTop), arrow+"\n", font=HackNF,
                  fill=colorFill, align='left')

        nameList = nameList + name + "\n"
        lastPriceList = lastPriceList + lastPrice + "\n"
        up_DownList = up_DownList + uporDown + "\n"

        if float(perChange) > 0:
            perChange = "+" + perChange

        perChangeList = perChangeList + perChange + "\n"

    draw.multiline_text((100,100),nameList,font=HackNF,fill=colors,align='left',spacing=25)
    draw.multiline_text((360,100),lastPriceList,font=HackNF,fill=colors,align='left',spacing=25)
    draw.multiline_text((620,100),up_DownList,font=HackNF,fill=colors,align='left',spacing=25)
    draw.multiline_text((870,100),perChangeList,font=HackNF,fill=colors,align='left',spacing=25)

    img.save("picture.png")


