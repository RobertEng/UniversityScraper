################################################################################
# Scrapes from SB website all pdf documents which are rounds, and extracts the
# text out of the pdf documents.
# 
################################################################################

import urllib2
from urllib2 import Request, urlopen
from StringIO import StringIO
import json
#import cookielib
#import os
from bs4 import BeautifulSoup
#import pyPDF2
#from pyPdf import PdfFileWriter, PdfFileReader

# Website to scrape
#HOME_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.730342%2C-98.977939&radius=2111459&types=university&key=AIzaSyD2f3Qm3ePa6aa05LPXmFRM4UGJipSXuCk&sensor=true'
HOME_URL = 'http://www.findlatitudeandlongitude.com/?loc='

universities = ['princeton university', 'harvard university', 'yale university', 'columbia university', 'stanford university', 'university of chicago', 'massachusetts institute of technology', 'duke university', 'university of pennsylvania', 'caltech']

for uni in universities:
    url = HOME_URL + uni
    home_req = urllib2.Request(url)
    home_content = urllib2.urlopen(home_req)
    soup = BeautifulSoup(home_content)
    print uni
    print soup.find(id='lon_dec').get_text()
    print soup.find(id='lat_dec').get_text()
    print '\n'

    
#
## Request page content
#home_req = urllib2.Request(HOME_URL)
#home_content = urllib2.urlopen(home_req)
## Construct BeautifulSoup object of page content
#soup = BeautifulSoup(home_content)
#
#
## code for google places api call
#decoded = json.loads(soup.get_text())
#for place in decoded['results']:
#    print place['name']




#for link in soup.find_all('a'):
#        candidate = str(link.get('href'))
#        #print "I FOUND A CANDIDATE"
##        print candidate
#        if (candidate[-len(FILE_EXT):] == FILE_EXT):
#                file_url = HOME_URL + candidate
#                file_url = file_url.replace(" ", "%20")
#                # note above: can use urlencode to remove dangerous characters such as spaces
#                #print candidate[0:28]
#                if len(candidate)>29 and candidate[0:28] == '/~/media/wdts/nsb/pdf/hs/pdf':
#                    #print candidate
#                    # k = index of last "/" of the candidate => ...path/filename.pdf
#                    k = candidate.rfind("/")
#                    pathname = candidate[:k]
#                    filename = candidate[k+1:]
#                    #print(pathname) #Everything After root
#                    #print(filename) #Only the last part
#                    print(file_url) #Full URL
#                    ############################################################
#                    # At this point, I have file_url which leads to a pdf I want
#                    writer = PdfFileWriter()
#                    remoteFile = urlopen(Request(file_url)).read()
#                    memoryFile = StringIO(remoteFile)
#                    pdfFile = PdfFileReader(memoryFile)
#                    
#                    ############################################################
#                    #Use this to save scraped file to output.pdf
#                    for pageNum in xrange(pdfFile.getNumPages()):
#                        currentPage = pdfFile.getPage(pageNum)
#                        #currentPage.mergePage(watermark.getPage(0))
#                        writer.addPage(currentPage)
#                    outputStream = open("output.pdf","wb")
#                    writer.write(outputStream)
#                    outputStream.close()
#                    
#                    ############################################################
#                    # Read output.pdf and extract text from each page, spit into
#                    # round.txt
#                    pdf = PdfFileReader(open("output.pdf", "rb"))
#                    for page in pdf.pages:
#                        pgtxt = page.extractText().encode("ascii", "ignore")
#                        #remove new lines
#                        pgtxt = pgtxt.replace('\n', ' ').replace('\r', '')
#                        print pgtxt
#                        f.write(pgtxt)
#f.close()
#                    
#
#                    
#                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    # Open and save content of the file in pdf_read
                    #cj = cookielib.CookieJar()
                    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                    #pdf_req = urllib2.Request(file_url)
                    #pdf_content = opener.open(pdf_req)
                    #pdf_read = pdf_content.read()
                    #pdf_content.close()
                    #opener.close()
                      
                    # Create the path if not defined
                    #if not os.path.exists(pathname):
                    #        os.makedirs(pathname)                
                    
                    # Write content of the file to the path
                    #pdf_write = open("round.txt", 'w')
                    #pdf_write.write(pdf_read)
                    #pdf_write.close()
                    
                    #THIS CODE IS THE ONE I LIKE. DON"T DELETE IT
                    #f= open('round.txt','w')
                    #pdfl = getPDFContent("test.pdf").encode("ascii", "ignore")
                    #f.write(pdfl)
                    #f.close()
                    
                    #for pageNumber, page in enumerate(PDFDocument.get_pages()):
                        #if pageNumber == 42:
                    #    print("sup")
                    #    getPage(i).extractText()

