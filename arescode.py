#!/usr/bin/env python

import sys
sys.path.append('/usr/bin/library_arescode/')

from termcolor import colored
from threading import Thread
from http_helpers import *
from file_dir_helpers import *
import pyfiglet
import requests
import argparse
import os
import datetime
import time

t = 1

info = """
            Author: Johan Du
            Description: Create domain directory structure based on response code
"""

class Request_performer(Thread):

    def __init__(self, subdomain, stt, schema, verbose):

        Thread.__init__(self)
        self.subdomain = subdomain
        self.stt = stt
        self.schema = schema
        self.verbose = verbose

    def run(self):

        response_code_structure(self.subdomain, self.stt, self.schema, self.verbose)

def response_code_structure(subdomain, stt, schema, verbose):

    global t

    try:
        string = ''
        string_file = ''
        subdomain = subdomain.strip()
        string += str(stt) + '\n'
        string_file += str(stt) + '\n'
        url = schema + '://' + subdomain
        string +=  colored('Original: ', 'yellow') + url + '\n'
        string_file +=  'Original: ' + url + '\n'
        res = requests.get(url, headers=gen_headers, timeout=10)
        code = int(res.status_code)
        if not len(res.history):
            if code >= 100 and code < 200:
                os.system('mkdir -p ' + 'response_code/' + schema + '/1xx/' + str(code) + "/" + subdomain)
            if code >= 200 and code < 300:
                os.system('mkdir -p ' + 'response_code/' + schema + '/2xx/' + str(code) + "/" + subdomain)
            if code >= 400 and code < 500:
                os.system('mkdir -p ' + 'response_code/' + schema + '/4xx/' + str(code) + "/" + subdomain)
            if code >= 500:
                os.system('mkdir -p ' + 'response_code/' + schema + '/5xx/' + str(code) + "/" + subdomain)
        else:
            os.system('mkdir ' + 'response_code/' + schema + '/3xx/' + subdomain)
            fw = open('response_code/' + schema + '/3xx/' + subdomain  + '/' + subdomain + '-redirect.txt', 'w')
            for history in res.history:
                fw.write(history.request.url + "\t\t\t" + str(history.status_code) + "\n")
                fw.write('-'*200 + "\n")
            fw.write(res.request.url + "\t\t\t" + str(res.status_code) + "\n")
            fw.close()
            string +=  colored('Redirect: ', 'yellow') + colored(res.request.url, 'green') + '\n'
            string_file +=  'Redirect: ' + res.request.url + '\n'
        string +=  colored('Response code: ', 'yellow') + colored(res.status_code, 'blue') + '\n'
        string_file +=  'Response code: ' + str(res.status_code) + '\n'
        string +=  colored('History: ', 'yellow') + str(res.history) + '\n'
        string_file +=  'History: ' + str(res.history) + '\n'
    except Exception as error: 
        string +=  colored('Error: ', 'yellow') + colored(error, 'red') + '\n'
        string_file += 'Error: ' + str(error) + '\n'
        os.system('mkdir ' + 'response_code/' + schema  + '/error/' + subdomain)
        fw = open('response_code/' + schema + '/error/' + subdomain + '/' + subdomain + '-error.txt', 'w')
        fw.write(str(error))
        fw.close()
    string +=  colored('-'*80, 'white') + '\n'
    string_file += '-'*80 + '\n'
    if verbose:
        print string
    append_to_file('response_code/' + schema + '/arescode-'+schema+'.log', string_file)
    t -= 1

def main():

    global t

    # Construct the argument parser
    ap = argparse.ArgumentParser()
    
    # Add the arguments to the parser
    ap.add_argument("-f", "--file", required=True, help="Enter the filename contain living subdomains")
    ap.add_argument("-t", "--thread", help="Number of threads")
    ap.add_argument("-v", "--verbose", action='store_true', help="Increase verbosity level")

    args = vars(ap.parse_args())
    files = args['file']
    totalthread = args['thread']
    verbose = args['verbose']

    if totalthread == None:
        totalthread = 1
    else:
        totalthread = int(totalthread)

    os.system('clear')

    ascii_banner = pyfiglet.figlet_format("Arescode")
    print colored(ascii_banner, 'green')
    print colored(info, 'yellow')
    print colored('\nWaiting a few seconds ...\n', 'blue')
    time.sleep(3)    

    start = time.time()

    f = open(files, 'r')
    subdomains = f.readlines()

    inital_dir()

    for schema in ['http', 'https']:
        print colored('Waiting for testing ' + schema + ' schema ...\n', 'blue')
        time.sleep(3)

        count = 0
        threads = []

        for subdomain in subdomains:
            count += 1
            while t > int(totalthread):
                continue
            t += 1
            thread = Request_performer(subdomain, count, schema, verbose)
            thread.start()
            threads.append(thread) 
     
        for thread in threads:
            thread.join()

    end = time.time()
    print colored('Time handling proxies is hh:mm:ss: ', 'yellow') + str(datetime.timedelta(seconds=int(end - start)))
         
if __name__ == '__main__':
    main()
