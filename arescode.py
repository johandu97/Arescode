#!/usr/bin/env python

import sys
sys.path.append('/usr/bin/library/')

from termcolor import colored
from threading import Thread
from http_helpers import *
from string_helpers import *
import pyfiglet
import requests
import argparse
import os
import datetime
import time

t = 1

info = """
            Author: Johan Du
            Date Created: 10/11/2019
            Date Update: 10//11/2019
            Description: Create domain directory structure based on response code
"""

class Request_performer(Thread):

    def __init__(self, url, stt, results):

        Thread.__init__(self)
        self.url = url
        self.stt = stt
        self.results = results

    def run(self):

        response_code_structure(self.url, self.stt, self.results)

def response_code_structure(url, stt, results):

    global t

    try:
        string = ''
        url = url.strip()
        if isHttps(url):
            domain = delete_https(url)
        else:
            domain = delete_http(url)
        string += str(stt) + '\n'
        string +=  colored('Original: ', 'yellow') + url + '\n'
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
            string +=  colored('Redirect: ', 'yellow') + res.request.url + '\n'
        string +=  colored('Response code: ', 'yellow') + colored(res.status_code, 'blue') + '\n'
        string +=  colored('History: ', 'yellow') + str(res.history) + '\n'
    except Exception as error: 
        string +=  colored('Error: ', 'yellow') + colored(error, 'red') + '\n'
        os.system('mkdir ' + results + '/error/' + domain)
        fw = open(results + '/error/' + domain + '/' + domain + '_error', 'w')
        fw.write(str(error))
        fw.close()
    string +=  colored('-'*80, 'white') + '\n'
    print string
    t -= 1

def main():

    global t

    # Construct the argument parser
    ap = argparse.ArgumentParser()
    
    # Add the arguments to the parser
    ap.add_argument("-f", "--file", required=True, help="Enter the filename contain URLs")
    ap.add_argument("-o", "--output", required=True, help="Return the resulting directory name")
    ap.add_argument("-t", "--thread", help="Number of threads")

    args = vars(ap.parse_args())
    files = args['file']
    results = args['output']
    totalthread = args['thread']

    if totalthread == None:
        totalthread = 50
    else:
        totalthread = int(totalthread)

    countthread = 0
    threads = []
    os.system('clear')

    ascii_banner = pyfiglet.figlet_format("Arescode")
    print ascii_banner
    print colored(info, 'yellow')
    print colored('\nWait a few seconds\n', 'blue')
    time.sleep(3)    

    start = time.time()

    f = open(files, 'r')
    urls = f.readlines()

    if os.path.exists(results):
        os.system('rm -r ' + results)
    os.system('mkdir ' + results )
    os.system('mkdir ' + results + '/1xx')
    os.system('mkdir ' + results + '/2xx')
    os.system('mkdir ' + results + '/3xx')
    os.system('mkdir ' + results + '/4xx')
    os.system('mkdir ' + results + '/5xx')
    os.system('mkdir ' + results + '/error')

    count = 0

    for url in urls:
        count += 1
        while t > int(totalthread):
            continue
        t += 1
        thread = Request_performer(url, count, results)
        thread.start()
        threads.append(thread) 
     
    for thread in threads:
        thread.join()

        

    end = time.time()
    print colored('Time hangling proxies is hh:mm:ss: ', 'yellow') + str(datetime.timedelta(seconds=int(end - start)))
         
if __name__ == '__main__':
    main()
