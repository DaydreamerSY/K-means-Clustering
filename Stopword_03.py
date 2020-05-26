import os

def make_dict():
    stop = []
    with open('stop_word_dash.txt', 'r', encoding= 'utf-8') as r:
        while True:
            l = r.readline()
            if l == '':
                l = r.readline()
                if l == '':
                    break
            stop.append(l.split('\n')[0])
        r.close()
    return stop
    
def split(line, stop_dic):
    shit = line.split(' ')
    result = []
    for s in shit:
        if s not in stop_dic and not s == 'Unnamed':
            result.append(s)
    return ' '.join(result)

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
    
def stop_split(subdir, des, dic):
    for fname in os.listdir(subdir):
        if fname.endswith('.txt'):
            # number = fname.split('tokened.txt')[0]
            new_name = os.path.join(des, fname.replace('tokened.txt', 'splited.txt'))
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
                    shit = split(l, dic)
                    w.write(shit + '\n')
                    
                w.close()
                r.close()
                

def do_it():
    source = 'Tokened'
    des = 'FINAL'
    stop_dictionary = make_dict()
    
    list_folders = find_Source(source)
    list_destination = make_source(list_folders, source, des)
    
    for i in range(len(list_folders)):
        subdirsource = os.path.join(list_folders[i])
        subdirdes = os.path.join(list_destination[i])
        stop_split(subdirsource, subdirdes, stop_dictionary)
