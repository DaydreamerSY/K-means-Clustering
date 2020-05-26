import VacuumCleaner_01 as vc
import Tokenization_02 as tk
import Stopword_03 as stw
import Copy_04 as cp
import CreateCSV_05 as csv
import test_v206 as test

if __name__ == '__main__':
    print('Mixing data...')
    cp.do_it()
    print('Cleaning data...')
    vc.do_it()
    print('Tokenization data...')
    tk.do_it()
    print('Cleaning stop word...')
    stw.do_it()
    print('Creating test data as csv type...')
    csv.do_it()
    print('Clustering data...')
    test.do_it()
    print('Done.')
