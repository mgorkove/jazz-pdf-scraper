#this program downloads all pdfs on the source page below, and saves them to the directory below
from bs4 import BeautifulSoup
import requests
import sys
import urllib


source = "http://duhoviki.ru/index.php?option=com_content&view=category&id=16&Itemid=165"
directory = "/trumpet study pdfs/aebersolds/"
prefix = "http://duhoviki.ru"



def getParent(element):
    parent = element.parent
    try:
        pdfLink = prefix + "/" + parent["href"]
        downloadFilename = pdfLink.split("/")[-1]
        urllib.request.urlretrieve(pdfLink, directory + downloadFilename)
    except:
        print("exception")

def getPDFLinks(fullLink):
    with requests.Session() as s:
        r = s.get(fullLink, allow_redirects=False)
        soup = BeautifulSoup(r.content, "lxml")
        spanList = soup.find_all("span", style="color:#ff0000;")
        for element in spanList:
            getParent(element)

def downloadPDF(element):
    linksList = element.find_all('a')
    for a in linksList:
        fullLink = prefix + a["href"]
        getPDFLinks(fullLink)

def downloadAllPdfs():
    with requests.Session() as s:
        r = s.get(source, allow_redirects=False)
        soup = BeautifulSoup(r.content, "lxml")
        tdList = soup.find_all("td", class_="list-title")
        for element in tdList:
            downloadPDF(element)

downloadAllPdfs()





    
