def runApp(imgurl):
    from translate import translator
    from visionAPI import image_description
    import urllib.request

    urllib.request.urlretrieve(imgurl, "image.jpg")

    imagePath = "image.jpg"

    description = image_description(imagePath)
    desclist = []
    translist = []
    for i in range (len(description)):
        desclist.append(description[i])
        translist.append(translator(desclist[i]))
    return (desclist,translist)

def runAppUpl(fileName):
    from translate import translator
    from visionAPI import image_description

    imagePath = fileName

    description = image_description(imagePath)
    desclist = []
    translist = []
    for i in range(len(description)):
        desclist.append(description[i])
        translist.append(translator(desclist[i]))
    return (desclist, translist)


