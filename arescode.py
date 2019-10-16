#!/usr/bin/env python

import sys
sys.path.append('./library/')

import pyfiglet
import requests
import argparse
from termcolor import colored
import os
from http_helpers import *
from string_helpers import *
import time


info = """
            Author: Johan Du
            Date Created: 10/11/2019
            Date Update: 10//11/2019
            Description: Create domain directory structure based on response code
"""

def main():

    # Construct the argument parser
    ap = argparse.ArgumentParser()
    
    # Add the arguments to the parser
    ap.add_argument("-f", "--file", required=True, help="Enter the filename contain URLs")
    ap.add_argument("-o", "--output", required=True, help="Enter the resulting directory name")
    args = vars(ap.parse_args())
    files = args['file']
    results = args['output']

    os.system('clear')

    ascii_banner = pyfiglet.figlet_format("Arescode")
    print ascii_banner
    print colored(info, 'yellow')
    print colored('\nWait a few seconds\n\n\n', 'blue')
    time.sleep(3)    

    f = open(files, 'r')
    domains = f.readlines()

    if os.path.exists(results):
        os.system('rm -r ' + results)
    os.system('mkdir ' + results )
    os.system('mkdir ' + results + '/1xx')
    os.system('mkdir ' + results + '/2xx')
    os.system('mkdir ' + results + '/3xx')
    os.system('mkdir ' + results + '/4xx')
    os.system('mkdir ' + results + '/5xx')
    os.system('mkdir ' + results + '/error')

    count = 1

    for domain in domains:
        try:
            domain = domain.strip()
            url = domain
            if isHttps(url):
                domain = delete_https(url)
            else:
                domain = delete_http(url)
             
            print str(count)
            print colored('Original: ', 'yellow') + url
        
            count += 1

            res = requests.get(url, headers=gen_headers)

            code = int(res.status_code)
            if not len(res.history):
                if code >= 100 and code < 200:
                    os.system('mkdir -p ' + results + '/1xx/' + str(code) + "/" + domain)
                if code >= 200 and code < 300:
                    os.system('mkdir -p ' + results + '/2xx/' + str(code) + "/" + domain)
                if code >= 400 and code < 500:
                    os.system('mkdir -p ' + results + '/4xx/' + str(code) + "/" + domain)
                if code >= 500:
                    os.system('mkdir -p ' + results + '/5xx/' + str(code) + "/" + domain)
            else:
                os.system('mkdir ' + results + '/3xx/' + domain)
                fw = open(results + '/3xx/' + domain  + '/' + domain + '_redirect', 'w')
                for history in res.history:
                    fw.write(history.request.url + "\t\t\t" + str(history.status_code) + "\n")
                    fw.write('-'*200 + "\n")
                fw.write(res.request.url + "\t\t\t" + str(res.status_code) + "\n")
                fw.close()
           
            print colored('Redirect: ', 'yellow') + res.request.url
            print colored(res.status_code, 'blue')
            print res.history
        except Exception as error:
            print colored(error, 'red')
            os.system('mkdir ' + results + '/error/' + domain)
            fw = open(results + '/error/' + domain + '/' + domain + '_error', 'w')
            fw.write(str(error))
            fw.close()
        print colored('-'*80, 'white')
         
if __name__ == '__main__':
    main()
