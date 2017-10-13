from bs4 import BeautifulSoup as bs
html_doc="<html><head><title>111</title></head><body><h1>易车</h1></bady></html>"
soup=bs(html_doc,"html.parser")
print(soup.title.string)
print(soup.h1.string)
print(soup.a)
print(soup.find(id='link2').get_text())
for link in soup.findAll("a"):
    print(link.string)


