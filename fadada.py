import os
import sys
import urllib2
import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import urllib2
import random
import StringIO
import gzip
import re

def save_page_info(save_path, filename,pageinfo):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path+"/"+filename+".html"
    with open(path, "w+") as fp:
            fp.write(str(pageinfo))

def get_page_title(myPage):
    soup = BeautifulSoup(myPage,"lxml")
    print str(soup.title)
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', soup.title.text)
    print dd
    return dd
    #return soup.select('.fdd-ht-detail-zw')

def getContent(url):
    my_headers = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"] 
    random_header = random.choice(my_headers)
    req =urllib2.Request(url)  
    req.add_header("User-Agent", random_header)  
    req.add_header("GET",url)  
    req.add_header("Host","www.fadada.com") 
    req.add_header("Connection","keep-alive") 
    #req.add_header("Accept-Encoding","gzip, deflate, br") 
    req.add_header('Accept-encoding', 'gzip')
    req.add_header("Upgrade-Insecure-Requests","1")
    req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
    req.add_header("Cookie","__jsluid=058b9d7a7139d1217b8d0e9581dd9a23; gr_user_id=8196a831-234d-401b-aaf6-a7299401f132; myAccounts=17621496302; Hm_lvt_e1e828ede8f023b510da95de235d8b96=1522641691,1523264780; JSESSIONID=BFF1072EE4994664E43F72CF4CBFD917; gr_session_id_584825818a7443419d9551c1eb62014d=4748efbb-86c0-4e3a-9dad-8327bed83782; Hm_lpvt_e1e828ede8f023b510da95de235d8b96=1523277324")
    data=urllib2.urlopen(req).read()
    data = StringIO.StringIO(data)
    gzipper = gzip.GzipFile(fileobj=data)
    html = gzipper.read()
    return html

def Spider(url):
    save_path = u"/Users/data"
    for num in range(40,42): 
        myPage = getContent(url+str(num))
    	print "downloading ", url+str(num)
    	filename = get_page_title(myPage)
        save_page_info(save_path, filename, myPage)
        num += 1

if __name__ == '__main__':
    print "start"
    start_url = "https://www.fadada.com/hetongmuban/detail-"
    Spider(start_url)
    print "end"