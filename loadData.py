import requests
import json
import sys

def loadData():
    botsDocID = '1saYD5dpWh-XH8HSTa7XOqmYvJZAsNoEE_FAGwEgboE4'
    botsDocName = 'СписокБотов'
    botsReqResult = requests.get('https://opensheet.elk.sh/'+ botsDocID + '/' +botsDocName)

    if botsReqResult:
        botsTable = json.loads(botsReqResult.text)
        
        with open("bots.json", "w") as file:
            json.dump(botsTable, file)
    else:
        with open("bots.json", "r") as file:
            botsTable = json.load(file)
        
    botsRealData = {}
    for bot in botsTable:
        if ("Token" in bot) and ("Name" in bot):
            botsRealData[bot["Name"]] = bot["Token"]
    
    dataDocID = '1cF8-TYSpb2w_DySG-cHtEfuvS1fZ0ZUmcJKohkdByus'
    dataDocName = 'Данные'
    dataReqResult = requests.get('https://opensheet.elk.sh/'+ dataDocID + '/' +dataDocName)
    
    if dataReqResult:
        dataTable = json.loads(dataReqResult.text)
        
        with open("data.json", "w") as file:
            json.dump(dataTable, file)
    else:
        with open("data.json", "r") as file:
            dataTable = json.load(file)

    dataDict= {}
    for row in dataTable:
        if ("ID" in row):
            dataDict[row["ID"]] = row
    
    return botsRealData, dataDict