import requests
import re
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BS
from news.models import Headline

requests.packages.urllib3.disable_warnings()
def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/home.html", context)

def scrape(request):
    Headline.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.dainikamadershomoy.com/"
    content = session.get(url, verify=False).content
    soup = BS(content, "html.parser")
    News = soup.find_all('div', {"class":re.compile('(w3)')})
    for artcile in News:
        main = artcile.find('a')
        link = main['href'] if main else "N/A"
        if main!=None and link!="N/A":
            PC=main.find('img')
            image_src = str(PC.get('src')) if PC else "N/A"
            title = main.text
        if title!=None and title!="" and link != "N/A":
            new_headline = Headline()
            new_headline.title = title
            new_headline.url = link
            new_headline.image = image_src
            new_headline.save()
    # for row in Headline.objects.all().reverse():
    #     if Headline.objects.filter(url=row.url_id).count() > 1:
    #         row.delete()
    return redirect("../")
