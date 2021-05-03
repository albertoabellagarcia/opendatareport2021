def exist_page(url):
    import urllib.request
    try:
        webhandler = urllib.request.urlopen(url)
        code = webhandler.getcode()
        print("the code is" + str(code))
        if code == 200:
            return [True, webhandler.read()]
        else:
            return ["other", "code : " + str(webhandler.getcode())]
    except:
        return [False, "wrong domain"]

url = "https://www.dipucuenca.es/open-data"
print(exist_page(url))



print(exist_page2(url))