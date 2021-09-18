
def responseImg(rates):
    from PIL import Image, ImageDraw, ImageFont
    from parse import parseJSON

    # # * font declaration
    # roboto = ImageFont.truetype("fonts\RobotoMono.ttf", 30)
    # montserrat = ImageFont.truetype("fonts\Montserrat.ttf", 30)
    # bebas = ImageFont.truetype("fonts\BebasNeue.ttf", 45)
    # slab = ImageFont.truetype("fonts\RobotoSlab.ttf", 20)

    # width = 1280
    # height = 720

    # # * imported from parse.py
    # for i in rates:
    #     name, lastPrice, openPrice,uporDown,icon,perChange = rates[i]
    #     lastPrice, openPrice = float(lastPrice), float(openPrice)
    #     change = openPrice - lastPrice
    #     # perChange = str(
    #     #     round(((lastPrice - openPrice) / lastPrice) * 100, 2))

    #     img = Image.new(mode="RGBA", size=(
    #         width, height), color=(54, 57, 63, 100))
    #     draw = ImageDraw.Draw(img)

    # space = " " * 20
    #     moreSpace = " " * 25
    #     spaceFromTop = 60

    #     hdr = "Name" + space + "Price" + space + "Change" + space + "%"
    #     draw.text((10, 5), hdr, font=bebas, fill=(
    #         225, 225, 225), align='right',embedded_color=True)

    #     txt = icon +moreSpace+ name + moreSpace + \
    #         str(lastPrice) + moreSpace + \
    #         str(change) + moreSpace + str(perChange)

    #     draw.text((10, spaceFromTop), txt, font=slab,
    #               fill=(255, 255, 255), align='right')
    # img.save("picture.png")

    # img.show()

    fnt = ImageFont.truetype("fonts\HackNF_Regular.ttf", 45, layout_engine=ImageFont.LAYOUT_RAQM)

    img = Image.new(mode="RGBA", size=(
        1280, 720), color=(54, 57, 63, 100))
    draw = ImageDraw.Draw(img)
    nameList="Name\n" 
    lastPriceList="lastPrice\n"
    up_DownList="uporDown\n"
    perChangeList="perChange\n"
    iconsList="\n"
    colors=[(255,255,255)]
    for i in rates:
        name, lastPrice, openPrice,uporDown,arrow,colorFill,perChange = rates[i]
        colors.append(colorFill) 

        iconsList=iconsList+arrow+"\n"
        nameList= nameList + name +"\n"
        lastPriceList=lastPriceList +lastPrice +"\n"
        up_DownList= up_DownList + uporDown + "\n"
        perChangeList= perChangeList + perChange + "\n"

        



    draw.multiline_text((50,100),iconsList,font=fnt,fill=colors[1],align='left',spacing=25)
    draw.multiline_text((100,100),nameList,font=fnt,fill=colors[0],align='left',spacing=25)
    draw.multiline_text((350,100),lastPriceList,font=fnt,fill=colors[0],align='left',spacing=25)
    draw.multiline_text((620,100),up_DownList,font=fnt,fill=colors[0],align='left',spacing=25)
    draw.multiline_text((870,100),perChangeList,font=fnt,fill=colors[0],align='left',spacing=25)

    img.save("picture.png")
    img.show()
    # return img