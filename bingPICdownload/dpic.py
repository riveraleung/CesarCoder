import os
import datetime
import urllib.request
import json


def url():
    response = urllib.request.urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&idx=1&n=1&mkt")
    obj = json.load(response)
    url = (obj['images'][0]['url'])
    url='http://www.bing.com'+url
    return url

def gettime():
    time=datetime.datetime.now()
    date=time.strftime("%Y-%m-%d")
    return date

def download_pic(url,filename):
    req=urllib.request.Request(url)
    f=open(filename,"wb")
    try:
        resp=urllib.request.urlopen(req)
        if resp.getcode()==200:
          f.write(resp.read())
    except:
        return "failed"+resp.getcode()
    return filename

name = gettime()+".jpg"
url = url()

download_pic(url,name)

