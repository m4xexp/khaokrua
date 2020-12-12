import datetime
import calendar
import csv
import sys
import json


def contoJson(result):
    outputData = json.dumps(result)
    return outputData


def row_as_dict(data, columns):
    result = []
    for row in data:
        i=0
        items = {}
        for col in row:
            #skip first column for key of dictionary
            if (i > -1):
                column_name = columns[i]
                items[column_name] = col
            i=i+1
        result.append(items)
    return result



def increaseID(id,text):
    newID = id.split(text)
    newID = str(int(newID[1]) + 1)
    newID = text+(10-(len(newID)+len(text)))*"0" + newID
    return newID
