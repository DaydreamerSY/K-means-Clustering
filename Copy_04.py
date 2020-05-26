import os

count = 0
def find_Source(source):
    path = os.path.join(source)
    lf = [x[0] for x in os.walk(path)]
    return lf


def make_source(subpath):
    if not os.path.exists(subpath):
        os.makedirs(subpath)


def make_copy(subdir, des):
    for fname in os.listdir(subdir):
        if fname.endswith('.txt'):
            global count
            count += 1
            oder = f"{count:05}"
            name = oder + '.txt'
            old_name = os.path.join(subdir, fname)
            new_name = os.path.join(des, name)
            with open(old_name, 'r', encoding='utf-8') as r:
                w = open(new_name, 'w', encoding='utf-8')
                while True:
                    line = r.readline()
                    if line == '':
                        break
                    if not line == '\n':
                        w.write(line)
                w.close()
                r.close()


def do_it():
    source = 'Source'
    des = 'Mixing'
    
    list_folders = find_Source(source)
    make_source(des)
    
    for i in range(len(list_folders)):
        subdirsource = os.path.join(list_folders[i])
        make_copy(subdirsource, des)
