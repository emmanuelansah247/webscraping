from copyreg import constructor
from csv import writer
from email.mime import base
import imp
from django.shortcuts import render
from django.http import HttpResponse
import os,time
import threading
from os import listdir
from os.path import isfile,join
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from . import custommainfunction as main

# Create your views here.

async def home(request):

    scraping_url = 'https://tympanus.net/codrops/author/crnacura/'   

    scrapfilesdatalist = getScrapDataFiles()
    
    return render(request,'home.html',{
        'scrapfilesdatalist' : scrapfilesdatalist
    })


def posthome(request):
    
    if request.method ==  "POST":
        t = threading.Thread(target=somefun ,args=[])
        t.start()
    
    scrapfilesdatalist = getScrapDataFiles()

    return render(request,'home.html',{
        'scrapfilesdatalist' : scrapfilesdatalist
    })

def somefun():
        main.mainRun()

def getScrapDataFiles():
    mypath = "./static/media"
    scrapfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f))]
    scrapfilesdatalist = []
    for scrapfile in scrapfiles:
        fullpath = join(mypath,scrapfile)
        temp_scrapfiledatalist = {
            'name': scrapfile,
            'path': join("media",scrapfile),
            'datecreated': time.ctime(os.path.getmtime(fullpath))
        }
        scrapfilesdatalist.append(temp_scrapfiledatalist)
    scrapfilesdatalist =  sorted(scrapfilesdatalist, key= lambda x: x['datecreated'], reverse=True)
    if len(scrapfilesdatalist) > 2:
        scrapfilesdatalist = [scrapfilesdatalist[0] , scrapfilesdatalist[1]]
    return scrapfilesdatalist


