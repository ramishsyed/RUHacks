def runApp(imgurl,lang):
    from translate import translator
    from visionAPI import image_description
    import urllib.request

    urllib.request.urlretrieve(imgurl, "image.jpg")

    imagePath = "image.jpg"
    language = lang

    description = image_description(imagePath)
    desclist = []
    translist = []
    for i in range (len(description)):
        desclist.append(description[i])
        translist.append(translator((desclist[i]),language))
    return (desclist,translist)

def runAppUpl(fileName,lang):
    from translate import translator
    from visionAPI import image_description

    imagePath = fileName
    language = lang

    description = image_description(imagePath)
    desclist = []
    translist = []
    for i in range(len(description)):
        desclist.append(description[i])
        translist.append(translator((desclist[i]),language))
    return (desclist, translist)


