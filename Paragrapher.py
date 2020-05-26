from LinksFinder import *
import datetime
import os

class Paragrapher:
    def __init__(self,project_name, base_url):
        self.project_name = project_name
        self.name_url = str(base_url)
        self.base_url = requests.get(base_url)
        self.soup = BeautifulSoup(self.base_url.text, 'html.parser')
    
    def write_paragraph(self, file_name):
        dir = os.path.join(self.project_name, file_name)
        with open(dir, 'w', encoding='utf-8') as f:
            # f.write(datetime.datetime.now().strftime("[%H:%M:%S] [%d-%m-%y]") + '\n')
            f.write(self.name_url)
            for p in self.soup.find_all('p'):
                p1 = str(p).split('<p class="Normal">')
                if p1[0] == '':
                    p2 = p1[1].split('\n')
                    shit = p2[1].split('</p>')
                    f.write(str(shit[0]) + '\n\n')
            f.close()


# home_page = 'https://vnexpress.net/bong-da/union-berlin-doi-bong-vuon-len-nho-mau-cua-cdv-3968980.html'
# peter = Paragrapher(home_page)
# peter.write_paragraph('Crawled.txt')
