# Name          : main.py
# Project       : UPA 1. část: extrakce dat z webu
# Description   : Main script for the application, handles input arguments and controls which script to run
# Authors       : xbilko03, xpauli08, xsugark00	
import argparse
from webscraping.get import urlObtainer
from webscraping.extract import productExtractor

# sourceURL
URL = "https://www.rolecosplay.com/anime-costume.html"

# load operation argument
argParser = argparse.ArgumentParser(description="Process some integers.")
argParser.add_argument('--operation', type=str, help="operation of the webscraper")
argParser.add_argument('--count', type=int, help="quantity of operations performed")
argParser.add_argument('--source', type=str, help="file containing urls which are to be extracted data from")
arguments = argParser.parse_args()

# check for valid operation
if arguments.operation != 'get' and arguments.operation != 'extract':
    print('Invalid operation. Expected either \'get\' or \'extract\'')
    exit(1)

if arguments.operation == 'get':
    operations = arguments.count

    if operations == None:
        print('Please provide a number of operations you wish to perform')
        exit(1)

    if operations <= 0:
        print('Invalid operation count. Expected a greater than 0')
        exit(1)

if arguments.source == None and arguments.operation == 'extract':
    print('Invalid source file')
    exit(1)

# decide which script to run based on the operation
if arguments.operation == 'get':
    obtainer = urlObtainer(URL)
    obtainer.getUrls(operations)
elif arguments.operation == 'extract':
    extractor = productExtractor(URL)
    extractor.getProducts(arguments.source)
    
exit(0)