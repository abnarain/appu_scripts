#Author : Abhinav Narain
#Purpose : Classifies websites from macaffee online webpage
#March 18, 2014

import re
import mechanize
from mechanize import Browser
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    doc=[]
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            self.doc.append(list(attr))
    def handle_endtag(self, tag):
        self.doc.append(list(tag))
    def handle_data(self, data):
        self.doc.append(list(data))
    def handle_comment(self, data):
        self.doc.append(list(data))
    def string_s(self):
        return self.doc
    def __del__(self):
        return self.doc


if __name__=='__main__':
    shit =[]
    ll= ["www.porn.com","www.facebook.com","www.gatech.edu"]
    for i in range(0, len(ll)) :
        browser = Browser()
        browser.open("https://www.trustedsource.org/en/feedback/url?action=checksingle")   
    # fill the select check form
        try:
            browser.select_form(name="single_check_form")
        except:
            print "catching error "
        browser.form["product"] =["12-ts-3"]
        browser.form["url"]=ll[i]
        response = browser.submit()
        parser = MyHTMLParser()
        parser.feed(response.read())
        page = parser.doc
        shit.append(page[921+(i*2029)+i])
        response.close()
        del parser 
        del browser
        del response
        del page
    for i in range(0,len(shit)):
        print shit[i]
