import csv
def exist_page2(url):
    # check if a web page exists
    # returns [true , web content] if successes
    # otherwise returns [false, error] if it fails
    import requests
    output = []
    try:
        pointer = requests.get(url, timeout=(60, 60))
        if pointer.status_code == 200:
            return [True, pointer.text]
        else:
            return [False, pointer.status_code]
    except:
        return [False, "wrong domain"]

def exist_page(url):

    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux ppc64le; rv:75.0) Gecko/20100101 Firefox/75.0'}
    try:
        response = requests.get(url, headers=headers)
        print(response.content)
        if response.status_code < 400:
            return [True, response.content]
        else:
            return [False, response.status_code]
    except:
        return [False, 0]

def exist_page3(url):
    import urllib.request
    try:
        webhandler = urllib.request.urlopen(url)
        if webhandler.getcode() == 200:
            return [True, webhandler.read()]
        else:
            return ["other", "code : " + str(webhandler.getcode())]
    except:
        return [False, "wrong domain"]

# source of url of the portals
sourceCsvFile = "../DATA/portal_url_basic.csv"
# status of url of the portals
statusPortalsFile = "../DATA/portals_status.csv"
# variable to report the status
portalsStatus = []

# reading the source portals
with open(sourceCsvFile, "r") as file:
    rawLines = file.readlines()

# preparing a list of portal urls
lines = [line.replace(chr(10), "") for line in rawLines]
print(lines)

for line in lines:
    print("checking portal " + line)
    statusPortal = exist_page(line)
    if statusPortal[0] == True:
        print("the portal " + line + " has been found")
        portalsStatus.append([line, True])
    elif statusPortal[0] == "other":
        print("the portal " + line + "has found something")
        portalsStatus.append([line, "other"])
    elif statusPortal[0] == False:
        portalsStatus.append([line, False])
        print("El portal " + line + " seems to be down")

with open(statusPortalsFile, "w") as file:
    file.write(str(portalsStatus))

print("DEAD PORTALS")
for line in portalsStatus:
    if not line[1]:
        print(line[0])

