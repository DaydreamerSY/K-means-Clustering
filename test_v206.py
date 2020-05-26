import os

from sklearn.cluster import KMeans
import numpy as np


def prepare_labels(test_data, nc):
    X = []
    with open(os.path.join(test_data, 'shit.csv'), 'r', encoding='utf-8') as r:
        r.readline()
        while True:
            line = r.readline()
            if line == '':
                break
            X.append([float(i)*10000 for i in line.split('\n')[0].split(',')])
        r.close()
    X = np.array(X)
    
    km = KMeans(n_clusters=nc)
    result = km.fit(X)
    label = result.labels_
    
    with open('label.txt', 'w', encoding='utf-8') as w:
        for x in label:
            w.write(str(x))
            w.write(',')
        w.write('\n')
        sum_of_all = {}
    
        for x in label:
            if x not in sum_of_all:
                sum_of_all[x] = 1
            else:
                sum_of_all[x] = sum_of_all[x] + 1
    
        for x in sum_of_all:
            w.write('{}: {}\n'.format(x, sum_of_all[x]))
        w.close()

def make_source(des):
    if not os.path.exists(des):
        os.makedirs(des)

def get_info():
    r = open('label.txt', 'r', encoding='utf-8')
    line = r.readline()
    oder = [x for x in line.split('\n')[0].split(',')]
    return oder
            
    
def make_clustered(source, des, oder):
    data_need_to_cluster = os.path.join(source)
    names = os.listdir(data_need_to_cluster)
    for i in range(len(oder)):
        try:
            old_name = os.path.join(source, names[i])
            level = os.path.join(des, 'cluster{:02}'.format(int(oder[i])))
            make_source(level)
            new_name = os.path.join(level, names[i])
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
        except:
            continue
    

def do_it():
    source = 'FINAL'
    test_data = 'TestData'
    nc = int(input('How many cluster do you want? '))
    prepare_labels(test_data, nc)
    des = 'Result'
    make_source(des)
    oder = get_info()
    make_clustered(source, des, oder)
    # xây dựng giao diện nữa là .... done, ez
    