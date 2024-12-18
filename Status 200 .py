#!/usr/bin/env python
import requests, sys

def requester(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.bing.com/'
    }
    session = requests.Session()
    try:
        resp = session.get(url, headers=headers, verify=False, timeout=4)
        # html = resp.text
        if resp.url != url:
            print(resp.url + "\n")
    except Exception as e:
        # print(e)
        pass

if __name__ == "__main__":
    print "[*] Starting ..."
    f = open(sys.argv[1]).readlines()
    for link in f:
        url = link.strip()
        requester(url)
