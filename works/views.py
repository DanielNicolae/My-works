from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen

myModels1 = "https://grabcad.com/daniel.nicolae-1/models?page=1"
myGames = "https://play.google.com/store/apps/developer?id=Don%C8%9Bu+Daniel+Nicolae"

def index(request):
    # 3D models
    modelsClient = urlopen(myModels1)
    modelsPage = modelsClient.read()
    modelsClient.close()
    modelsPageSoup = BeautifulSoup(modelsPage, 'html.parser')
    allModels = []
    modelContainers = modelsPageSoup.findAll("div", {"class":"profile-tile__wrapper"})
    for model in modelContainers:
        modelUrl = model.find("div", {"class":"profile-tile profile-tile--sizer"}).a['href']
        modelImageContainer= model.find("div", {"class":"profile-tile profile-tile--sizer"})['style'].split('(')
        modelImage = modelImageContainer[1].split(')')
        modelTitle = model.find("div", {"class":"profile-tile profile-tile--sizer"}).a.div.text
        allModels.append((modelUrl, modelImage[0], modelTitle))
    return render(request, 'works/index.html', {
        "allModels": allModels,
    })
