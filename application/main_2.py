from application.bruteforce import Bruterforce
import csv
import os.path
from itertools import *

input_path = 'C:\\Users\\butte\\PycharmProjects\\new dipl'
if os.path.isfile(os.path.join(input_path, 'kyri_dataset_same_ans') + '.csv') is False:
    with open(os.path.join(input_path, 'kyri_dataset_same_ans') + '.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(('time_matrix',
                             'configurations',
                             'answer',
                             'answer_time'))

        new_config = Bruterforce()
        j = 0
        #str_time = ''.join(str(_) for _ in new_config.time_matrix[0])
        #str_time = str_time.join(str(_) for _ in new_config.time_matrix[1])
        #str_time = str_time.join(str(_) for _ in new_config.time_matrix[2])
        long_time = 542683371
        #for item in product(str_time, repeat=9):
        #while long_time < 999999999:
        while long_time < 542683380:
            long_time += 3
            item = str(long_time)
            new_time_matrix = [[int(item[0]), int(item[1]), int(item[2])],
                               [int(item[3]), int(item[4]), int(item[5])],
                               [int(item[6]), int(item[7]), int(item[8])]]
            new_config.time_matrix = new_time_matrix
            new_config.get_time_matrix()
            time, short_ans, full_ans = new_config.old(new_config.configurations1)
            for ans_item in full_ans:
                filewriter.writerow((new_time_matrix, new_config.configurations1, ans_item, time))

        #for i in range(100):
        #    new_item = Bruterforce()
        #    new_item.get_time_matrix()
        #    time, short_ans, full_ans = new_item.old(new_item.configurations1)
        #    for item in full_ans:
        #        filewriter.writerow((new_item.time_matrix, new_item.configurations1, item, time))
