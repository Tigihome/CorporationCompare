import requests as req


#                   Funktion Block
# ----------------------------------------------------------
# Get the Pilots ID via ESI "search"
def getID(Pilot):
    url = "https://esi.evetech.net/latest/search/?categories=character&datasource=tranquility&language=en-us&search=" + str(Pilot) + "&strict=false"
    resp= req.get(url)
    PilotJson = resp.json()
    # morph Json to ID
    PilotID = PilotJson['character']
    return(PilotID[0])
# Get the Pilots Corp History and return ID list of corps
def CorpHistory(ID):
    url = "https://esi.evetech.net/latest/characters/" + str(ID) +"/corporationhistory/?datasource=tranquility"
    resp= req.get(url)
    PilotHistory = resp.json()
    corphistory = []
    # morph the Json to a dict of IDs
    for ph in PilotHistory:
        CID = ph['corporation_id']
        corphistory.append(CID)
    return(corphistory)
# Compare two dicts of list and return IDs
def compare(Pilot,ComparePilot):
    same = []
    # compare the dicts
    for p in Pilot:
        for cp in ComparePilot:
            if p == cp:
                same.append(p)
    samesingle = []
    # filter doubles
    for s in same:
        if s in samesingle:
            skip = 1
        else:
            samesingle.append(s)
    return(samesingle)
# Get Corp names via ESI, return list of names
def corpname(idlist):
    names = []
    for idl in idlist:
        url = "https://esi.evetech.net/latest/corporations/" + str(idl) + "/?datasource=tranquility"
        resp2 = req.get(url)
        corp = resp2.json()
        names.append(corp["name"])
    return(names)
# Print a dict
def printdict(dict):
    for d in dict:
        print(d)
#
# ----------------------------------------------------------
#

#                   Program Block
# ----------------------------------------------------------
# Enter Pilot name
Pilot = input("Enter your Pilots Name:  ")
# get the ID
PilotID = getID(Pilot)
# Enter Pilot to compare with
ComparePilot = input("Enter the Pilot you want to compare with:  ")
# get the pilots name
CompareID = getID(ComparePilot)
# get the Pilots ids of history corps
PilotHistroy = CorpHistory(PilotID)
# get the ids of history corps you want to compare
CompareHistory = CorpHistory(CompareID)
# compare the lists
ProcessedList = compare(PilotHistroy, CompareHistory)
# get the corp names
SameCorp = corpname(ProcessedList)
# print the names
printdict(SameCorp)
# -----------------------------------------------------------

# exit
exit = input("Press a key to exit")