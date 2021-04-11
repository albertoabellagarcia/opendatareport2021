statusPortalsFile = "../DATA/portals_status.csv"
with open(statusPortalsFile, "r") as file:
    lines = file.readlines()
print(lines)
print(len(lines))
for rawline in lines:
    print(rawline)
    line = list(rawline)
    print(type(line))
    print(line)
    if not line[1]:
        print(line[0])
