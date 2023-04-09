import requests
from termcolor import colored as cl
import socket
import dns.resolver

def CHRM(test_url, test_cookie, header):
    print(" ")
    url = test_url
    cookie={"Cookie":test_cookie}
    print(cl("Trying GET Method...", color='yellow'))
    req_get = requests.get(url=url, cookies=cookie, headers=header).status_code
    #methods = ['POST','PATCH','TRACE','HEAD','OPTIONS']
    if req_get == 403:
        print(cl("GET >> 403", color='red'))
        print(" ")
        print(cl("Trying POST Method...", color='yellow'))
        req_post = requests.post(url=url, cookies=cookie, headers=header).status_code
        if req_post == 200:
            print(cl("POST >> 200", color='green'))
            print(cl("Change Method To POST", color='green'))
            print(cl("curl -X POST {} --cookie {}".format(url,test_cookie), color='green'))
            print(" ")
            exit()
        elif req_post == 403:
            print(cl("POST >> 403", color='red'))
            print(" ")
            print(cl("Trying PATCH Method...", color='yellow'))
            req_patch = requests.patch(url=url, cookies=cookie, headers=header).status_code
            if req_patch == 200:
                print(cl("POST >> 200", color='green'))
                print(cl("Change Method To PATCH", color='green'))
                print(cl("curl -X PATCH {} --cookie {}".format(url, test_cookie), color='green'))
                print(" ")
            elif req_patch == 403:
                print(cl("PATCH >> 403", color='red'))
                print(" ")
                print(cl("Trying OPTIONS Method...", color='yellow'))
                req_options = requests.options(url=url, cookies=cookie, headers=header).status_code
                if req_options == 200:
                    print(cl("OPTIONS >> 200", color='green'))
                    print(cl("Change Method To OPTIONS", color='green'))
                    print(cl("curl -X OPTIONS {} --cookie {}".format(url, test_cookie), color='green'))
                    print(" ")
                    exit()
                elif req_options == 403:
                    print(cl("OPTIONS >> 403", color='red'))
                    print(" ")
                    print(cl("Trying HEAD Method...", color='yellow'))
                    req_head = requests.head(url=url, cookies=cookie, headers=header).status_code
                    if req_head == 200:
                        print(cl("HEAD >> 200", color='green'))
                        print(cl("Change Method To HEAD", color='green'))
                        print(cl("curl -X HEAD {} --cookie {}".format(url, test_cookie), color='green'))
                        print(" ")
                        exit()
                    elif req_head == 403:
                        print(cl("HEAD >> 403", color='red'))
    elif req_get == 200:
        print("GET >> 200")
        print(" ")
        exit()

def CHLFLTU(test_url, test_cookie, header):
    url_upper = str(test_url).upper()
    url_lower = str(test_url).lower()
    print(" ")
    print("____________________________________________________")
    print(" ")
    print(cl("Testing Upper Case...", color='yellow'))
    print(cl(url_upper, color='blue'))
    CHRM(url_upper,test_cookie, header)
    print("____________________________________________________")
    print(" ")
    print(cl("Testing Lower Case...", color='yellow'))
    print(cl(url_lower, color='blue'))
    CHRM(url_lower,test_cookie, header)

def ADEX(test_url, test_cookie, header):
    if str(test_url).endswith('/'):
        print(" ")
        print(cl("Enter URL without '/' at end", color='red'))
    else:
        print(" ")
        url_json = str(test_url) + ".json"
        url_css = str(test_url) + ".css"
        url_xml = str(test_url) + ".xml"
        url_js = str(test_url) + ".js"
        url_html = str(test_url) + ".html"
        print(cl("Testing With JSON Extension...", color='yellow'))
        CHLFLTU(url_json, test_cookie, header)
        print(" ")
        print(cl("Testing With CSS Extension...", color='yellow'))
        CHLFLTU(url_css, test_cookie, header)
        print(" ")
        print(cl("Testing With XML Extension...", color='yellow'))
        CHLFLTU(url_xml, test_cookie, header)
        print(" ")
        print(cl("Testing With JS Extension...", color='yellow'))
        CHLFLTU(url_js, test_cookie, header)
        print(" ")
        print(cl("Testing With HTML Extension...", color='yellow'))
        CHLFLTU(url_html, test_cookie, header)

#def CNAME(test_url, test_cookie):
#    domain = test_url
#    ip_address = socket.gethostbyname(domain)
#    answers = dns.resolver.resolve(domain, 'CNAME')
#    cname = None
#    for rdata in answers:
#        if rdata.rdtype == dns.rdatatype.CNAME:
#            cname = rdata.target.to_text()
#    print(cname)

def Headers(test_url,test_cookie):
    url = test_url
    head = ["X-Originating-IP", "X-Forwarded-For", "X-Forwarded", "Forwarded-For", "X-Remote-IP", "X-Remote-Addr", "X-ProxyUser-Ip", "X-Original-URL", "Client-IP", "True-Client-IP", "Cluster-Client-IP", "X-ProxyUser-Ip"]
    cookie = {"Cookie": test_cookie}
    for h in head:
        header = {h:"127.0.0.1", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"}
        req = requests.get(url, cookies=cookie, headers=header).status_code
        if req == 403:
            print("  ")
            print(cl("{} >> 403".format(h), color='red'))
        elif req == 200:
            print("  ")
            print(cl("{} >> 200".format(h), color='green'))
    print("____________________________________________________")

def ALL(test_url, test_cookie):
    head = ["X-Originating-IP", "X-Forwarded-For", "X-Forwarded", "Forwarded-For", "X-Remote-IP", "X-Remote-Addr", "X-ProxyUser-Ip", "X-Original-URL", "Client-IP", "True-Client-IP", "Cluster-Client-IP", "X-ProxyUser-Ip"]
    for h in head:
        header = {h:"127.0.0.1", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"}
        print(" ")
        print(cl("Testing ALL With Header >>> {}".format(h), color='yellow'))
        print(" ")
        ADEX(test_url,test_cookie, header)



banner = """
  ______     _______  _  _   _____ _____ ______ _____  
 |  _ \ \   / /  __ \| || | / ____/ ____|  ____|  __ \ 
 | |_) \ \_/ /| |__) | || || (___| (___ | |__  | |__) |
 |  _ < \   / |  ___/|__   _\___ \\___ \|  __| |  _  / 
 | |_) | | |  | |       | | ____) |___) | |____| | \ \ 
 |____/  |_|  |_|       |_||_____/_____/|______|_|  \_\

"""
print(cl(banner, color='red'))
print(cl("[+] CoDed By Mostafa Elguerdawi", color='green'))
try:
    print(" ")
    test_url = input(cl("Enter URL with endpoint >> ", color='blue'))
    print(" ")
    test_cookie = input(cl("Enter Cookie if Existing >> ", color='blue'))
except Exception as e:
    print(e)

option = """
1) Change Request Method
2) Convert From Lower to Upper
3) Add Extensions
4) Add Custom Headers
5) ALL
"""
print(cl(option, color='green'))
op = int(input(cl("Enter Number of Testing >> ", color='blue')))

head = ["X-Originating-IP", "X-Forwarded-For", "X-Forwarded", "Forwarded-For", "X-Remote-IP", "X-Remote-Addr", "X-ProxyUser-Ip", "X-Original-URL", "Client-IP", "True-Client-IP", "Cluster-Client-IP", "X-ProxyUser-Ip"]
for h in head:
    header = {h:"127.0.0.1", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"}
    if op == 1:
        print(" ")
        print(cl("\t\tTesting With Header {}".format(h), color='blue'))
        CHRM(test_url, test_cookie, header)
    elif op == 2:
        print(" ")
        print(cl("\t\tTesting With Header {}".format(h), color='blue'))
        CHLFLTU(test_url, test_cookie, header)
    elif op == 3:
        print(" ")
        print(cl("\t\tTesting With Header {}".format(h), color='blue'))
        ADEX(test_url, test_cookie, header)
if op == 4:
    Headers(test_url, test_cookie)
elif op == 5:
    ALL(test_url, test_cookie)
else:
    print("Enter Valid option...")