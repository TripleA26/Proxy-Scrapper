import requests
import os
import threading
import queue
def scrape():
    os.system("cls")
    with open("links.txt") as f:
        for _ in f.readlines():
            link = _.removesuffix("\n")
            r = requests.get(link)
            with open("check.txt", "a+") as temp:
                try:
                    temp.write(r.text)
                    print(r.text)
                except:
                    pass
        print("Scrapped finished, now wait for filter, this will take some minutes. ")
        with open("check.txt") as f:
            for i in f.readlines():
                try:
                    i = i[i.find("/")+1:]
                    i = i[i.find("/")+1:]
                    if len(i) > 7 and len(i) < 22:
                        if i.__contains__(":"):
                            with open("proxy.txt", "a+") as proxy:
                                    proxy.write(i)
                except:
                    pass
            os.system("cls")
            print("Filter finished, now Checking for duplicate. Remember to check the original code of the duplicate text: https://github.com/Hazza3100/Text-Duplicate-Checker")
            with open('proxy.txt') as f:
                content = f.read().split('\n')
                content = set([line for line in content if line != ''])
                content = '\n'.join(content)
                with open('proxies.txt', 'a+') as f:
                    f.writelines(content)
threading.Thread(target=scrape).start()
c = queue.Queue()
valid = []

with open('proxies.txt', 'r') as f:
    proxies = f.read().split('\n')
    for x in proxies:
        c.put(x)
print("finished the filter, starting checking the proxies")
def check():
    with requests.Session() as session:
        try:
            global c
            while not c.empty():
                proxy = c.get()
                r = session.get('https://ipinfo.io/ip', proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'})
                if r.status_code == 200:
                    print("valid proxy")
                    open('valid.txt', 'a').write(f'{proxy}\n')
                else:
                    pass

        except:
            pass


b = len(open('proxies.txt', 'r').readlines())
for _ in range(b):
    threading.Thread(target=check).start()
os.remove("check.txt")
os.remove("proxy.txt")
