import requests
import os
import threading
def scrape():
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
                    with open("proxy.txt", "a+") as proxy:
                            proxy.write(i)
                except:
                    pass
            with open("proxy.txt") as file:
                for z in file.readlines():
                    if len(z) > 7 and len(z) < 18:
                        if z.__contains__(":"):
                            with open("proxy1.txt", "a+") as f:
                                f.write(z)
            print("Filter finished, now Checking for duplicate. Remember to check the original code of the duplicate text: https://github.com/Hazza3100/Text-Duplicate-Checker")
            with open('proxy1.txt') as f:
                content = f.read().split('\n')
                content = set([line for line in content if line != ''])
                content = '\n'.join(content)
                with open('proxies.txt', 'a+') as f:
                    f.writelines(content)
threading.Thread(target=scrape).start()
os.remove("check.txt")
os.remove("proxy.txt")
os.remove("proxy1.txt")