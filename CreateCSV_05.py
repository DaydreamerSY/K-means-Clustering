import os

def make_source(destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


def create_csv(source, des):
    key = []
    count = 0
    for fname in os.listdir(source):
        if fname.endswith('.txt'):
            old_name = os.path.join(source, fname)
            with open(old_name, 'r', encoding='utf-8') as r:
                while True:
                    line = r.readline().split('\n')[0]
                    if line == '':
                        break
                    for k in line.split(' '):
                        if k not in key and not (k.split('//')[0] == 'https:'):
                            if ',' in k:
                                k = k.replace(',', '.')
                            if not is_number(k):
                                count += 1
                                key.append(k)
                                
    test_data = os.path.join(des, 'shit.csv')
    with open(test_data, 'w', encoding='utf-8') as w:
        for i in range(len(key)):
            w.write(key[i])
            if i < (len(key) - 1):
                w.write(',')
        w.write('\n')
        w.close()
    
    key_data = os.path.join(des, 'key.txt')
    with open(key_data, 'w', encoding='utf-8') as w:
        for i in range(len(key)):
            w.write(key[i])
            if i < (len(key) - 1):
                w.write(',')
        w.write('\n')
        w.close()
    
    for fname in os.listdir(source):
        values = [0]*len(key)
        if fname.endswith('.txt'):
            old_name = os.path.join(source, fname)
            with open(old_name, 'r', encoding='utf-8') as r:
                while True:
                    line = r.readline().split('\n')[0]
                    if line == '':
                        break
                    for k in line.split(' '):
                        if ',' in k:
                            k = k.replace(',', '.')
                        if not (k.split('//')[0] == 'https:'):
                            if not is_number(k):
                                values[key.index(k)] += 1
        with open(test_data, 'a', encoding='utf-8') as w:
            for i in range(len(values)):
                w.write(str(values[i]))
                if i < (len(values) - 1):
                    w.write(',')
            w.write('\n')
            w.close()

def do_it():
    source = 'FINAL'
    des = 'TestData'
    make_source(des)
    create_csv(source, des)
    


