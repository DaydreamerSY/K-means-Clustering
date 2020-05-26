import os

def find_Source(source):
    path = os.path.join(source)
    lf = [x[0] for x in os.walk(path)]
    return lf

def make_source(listFol, source, destination):
    lf = [x for x in listFol]
    for i in range(len(lf)):
        lf[i] = lf[i].replace(source, destination)
        
    for p in lf:
        subpath = os.path.join(p)
        if not os.path.exists(subpath):
            os.makedirs(subpath)
            
    ld = [x[0] for x in os.walk(destination)]
    return ld
        

def smooth(subdir, des):
    for fname in os.listdir(subdir):
        if fname.endswith('.txt'):
            # number = fname.split('crawled.txt')[0]
            new_name = os.path.join(des, fname.replace('crawled.txt', 'smoothed.txt'))
            content = []
            old_name = os.path.join(subdir, fname)
            with open(old_name, 'r', encoding='utf-8') as r:
                w = open(new_name, 'w', encoding='utf-8')
                while True:
                    line = r.readline()
                    if line == '':
                        break
                    content.append(line.split('\n')[0])
                    
                for l in content:
                    shit = list(l)
                    temp = []
                    wait = False
                    for i in range(len(shit)):
                        if shit[i] == '<':
                            wait = True
                        if not wait:
                            temp.append(shit[i])
                        if shit[i] == '>':
                            wait = False
                    shit = ''.join(temp)
                    w.write(shit + '\n')
                    
                w.close()
                r.close()
                

def do_it():
    source = 'Mixing'
    des = 'Smoothed'
    list_folders = find_Source(source)
    list_destination = make_source(list_folders, source, des)
    for i in range(len(list_folders)):
        subdirsource = os.path.join(list_folders[i])
        subdirdes = os.path.join(list_destination[i])
        smooth(subdirsource, subdirdes)

