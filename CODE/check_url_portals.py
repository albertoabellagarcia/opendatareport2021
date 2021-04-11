import csv
def exist_page(url):
    # check if a web page exists
    # returns [true , web content] if successes
    # otherwise returns [false, error] if it fails
    import requests
    output = []
    try:
        pointer = requests.get(url)
        if pointer.status_code == 200:
            return [True, pointer.text]
        else:
            return [False, pointer.status_code]
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
    if not exist_page(line)[0]:
        portalsStatus.append([line, False])
    else:
        portalsStatus.append([line, True])
        print("El portal ")
with open(statusPortalsFile, "w") as file:
    file.write(str(portalsStatus))

print("DEAD PORTALS")
for line in portalsStatus:
    if not line[1]:
        print(line[0])

