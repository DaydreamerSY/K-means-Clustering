from Paragrapher import *
import os


def introduce():
    print('Project\'s homepage in file name \'home_pages_prepare.txt\'\n'
          '-Firt line is your homepage\n'
          '-Second line is numbers of page of homepage.\n'
          '--Ex: 1 is homepage/p1, 2 is homepage/p1 homepage/p2\n\n'
          'Make sure you get right ones')
    input()

def create_project_dir(path):
    """Create project's directory if not exits one"""
    if not os.path.exists(path):
        print('Creating directory: ' + path)
        os.makedirs(path)
        
def prepare_it(direc, home_page):
    sherlock = LinksFinder(direc, home_page)
    sherlock.write_2_file()
    sherlock.smooth_file()

def do_it(project_name):
    linksfile = os.path.join(project_name, 'Smooth_links.txt')
    print('Crawling...'
          'Please wait...')
    with open(linksfile, "r", encoding='utf-8') as f:
        count = 1
        while True:
            link = f.readline()
            if link == '':
                break
            countstr = f"{count:04}"
            para = Paragrapher(project_name, link)
            new_name = countstr + 'crawled.txt'
            para.write_paragraph(new_name)
            if delete_file(project_name, new_name) == False:
                count += 1
            else:
                print('deleting file...')
        f.close()
    
    
def delete_file(project_name, new_name):
    # print('DELETING EMPTY FILE')
    new_dir = os.path.join(project_name, new_name)
    with open(new_dir, "r", encoding="utf-8") as f:
        f.readline()
        f.readline()
        if f.readline() == '':
            f.close()
            os.remove(new_dir)
            return True
        return False

def generator_homepage():
    fg = open('home_pages_prepare.txt', 'r', encoding='utf-8')
    fghp = str(fg.readline()).split('\n')[0]
    numbers_of_page = fg.readline()
    signal = fg.readline().split('\n')[0]
    if numbers_of_page == '1':
        hp = open('HOME_PAGES.txt', 'w', encoding='utf-8')
        hp.write(str(fghp)+'\n')
        hp.close()
    else:
        hp = open('HOME_PAGES.txt', 'w', encoding='utf-8')
        hp.write(str(fghp)+'\n')
        for i in range(2, int(numbers_of_page) + 1):
            hp.write(str(fghp)+signal+'p'+str(i)+'\n')
        hp.close()
    fg.close()

if __name__ == '__main__':
    project_name = input('Project\'s name: ')
    des = os.path.join('Source', project_name)
    create_project_dir(des)
    introduce()
    generator_homepage()
    f = open('HOME_PAGES.txt', "r", encoding='utf-8')
    
    count = 1
    while True:
        home_page = f.readline()
        if home_page == '':
            break
        print(home_page)
        
        sub_project_name = project_name + f"{count:02}"
        direc = os.path.join(des, sub_project_name)
        create_project_dir(direc)
        
        prepare_it(direc, home_page)
        
        do_it(direc)
        count += 1
    f.close()
    
    
    
    
    