import csv
import math
from typing import Dict, List, TextIO

CATEGORY = 0
TYPE = 1
NAME = 2
QUALITY = 3
PRICE = 4
MATERIAL = 5
FEATURE = 6

def read_data(csv_file: TextIO) -> List[List[str]]:
    lines = csv.reader(csv_file)
    data = list(lines)[1:]
    return data

def recommend_product(data: list) -> list:
    product = input("Please enter the product type are you looking for:");
    feature = input("Please enter the features are you looking for (enter 'None' if none):");
    print("Please enter your priority:")
    print("1 - maximize quality")
    priority = input("2 - minimize price, while maintaining some quality?")  
    priority = int(priority)
    count = 0
    
    if (priority == 1):
        maxProduct = None
        count = 0
        for item in data:
            if (product.lower() ==  item[TYPE].lower()):
                print("here")
                if (count == 0):
                    maxProduct = data[0]
                    maxQual = data[0][QUALITY] 
                count = count + 1
                if (feature.lower() in item[FEATURE].lower()):
                    if (item[QUALITY] > maxQual):
                        maxQual = item[QUALITY]
                        maxProduct = item
                    elif ((item[QUALITY] == maxQual) and (item[PRICE] < maxQual)):
                        maxQual = item[QUALITY]
                        maxProduct = item
        return maxProduct
    else:       
        bestProduct = None
        count = 0
        for item in data:
            if (product.lower() == item[TYPE].lower()):
                if (count == 0):
                    bestProduct = data[0]
                    bestQual = data[0][QUALITY]
                count = count + 1
                if (feature.lower() in item[FEATURE].lower()):
                    if (item[QUALITY] > 5):
                        bestQual = item[QUALITY]
                        bestProduct = item
                    elif ((item[QUALITY] > bestQual) and (item[PRICE] < maxQual)):
                        bestQual = item[QUALITY]
                        bestProduct = item
        return bestProduct        

def redundant(data: list) -> list:
    red = []
    cat = input("Please enter the category of object: ");
    i = 0
    for item in data:
        if (item[0] == cat):
            for feature in item[i]:
                for other in data:
                    if (i != j):
                        if ((other[0] == cat) and (feature in other[6])):
                            if item[1] not in red:
                                red.append(item[1])
    return red    
    

#def format_data(data: List) -> Dict[str, Dict[str, str]]:
    #dictItem = {}
    #sub_dictItem = dict()
    #for item in data:
        #print(item)
        #if item[0] not in dictItem:
            #dictItem[item[0]] = []        
        #for item[1] in data:
            #dictItem[item[0]].append(item[1])
    #return dictItem
        
if __name__ == '__main__':
    products = read_data(open('product_data.csv'))
    print(products)
    print("Which feature would you like?")
    print("1 - product recommendation")
    choice = input("2 - check redundancies of features\n")
    choice = int(choice)
    
    if (choice == 1):
        maxProduct = recommend_product(products)
        if (maxProduct == None):
            maxProduct = "Sorry, no products met the specifications"
        print(maxProduct)
    elif(choice == 2):
        redundantProduct = redundant(products)
        print("Redundant Products:")
        print(redundantProduct)
    