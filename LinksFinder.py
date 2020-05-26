from bs4 import BeautifulSoup
import requests
import os

class LinksFinder:
    
    def __init__(self, direc, base_url):
        self.direc = direc
        self.base_url = requests.get(base_url)
        self.soup = BeautifulSoup(self.base_url.text, 'html.parser')
    
    def write_2_file(self):
        direct = os.path.join(self.direc, 'links.txt')
        with open(direct, "w") as f:
            for a in self.soup.find_all('a'):
                link = a.get('href')
                if self.check_link(link):
                    f.write(str(link).split('?')[0] + '\n')
                else:
                    pass
            f.close()
    
    def check_link(self, link):
        if str(link).split('//')[0] == 'https:':
            if str(link).split('?')[0].split('.')[-1] == 'html':
                return True
        return False
    
    def smooth_file(self):
        dir1 = os.path.join(self.direc, 'links.txt')
        list_link = []
        with open(dir1, 'r', encoding="utf-8") as r:
            while True:
                a = r.readline()
                if a == '':
                    break
                list_link.append(str(a))
        r.close()
        dir2 = os.path.join(self.direc, 'Smooth_links.txt')
        with open(dir2, 'w', encoding="utf-8") as w:
            for i in range (0, len(list_link)-1):
                if list_link[i] != list_link[i+1]:
                    w.write(list_link[i])
                else:
                    continue
        w.close()
        
        

# home_page = 'https://vnexpress.net/the-thao'
# peter = LinksFinder(home_page)
# peter.write_2_file()
