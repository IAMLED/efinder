#!/usr/bin/env python3

import re
import argparse

def splitter(url, path):

    nameList = []

    # Take all content of the file and assign each line in the file as an element of the list 'nameList'
    with open(path, 'r') as file:
        for line in file:
            name = line.strip().lower()
            nameList.append(name)

    splitted_url = re.split(r'[:/.]',url)
    filtered_url = list(filter(None, splitted_url))
    
    #Append elements from splitted_url to emailList
    emailList = [f'{name}@{filtered_url[1]}.{filtered_url[2]}' for name in nameList]
    
    print(emailList)

if __name__ == "__main__":
   
    parser = argparse.ArgumentParser(description="A simple python script that takes a URL and splits it into Protocol, Subdomain, Second-Level Domain, Top-Level Domain, and Subdomains",
                                      usage="./url_splitter [url] [path/to/file] [options]")
    
    # Specify the require arguments or flags
    parser.add_argument("url" , help="A Full URL starting with http(s)")
    parser.add_argument("path", help="Enter the name or path to the file containing list of names")
    
    # Initialise the parser
    args = parser.parse_args()

    splitter(args.url, args.path)


