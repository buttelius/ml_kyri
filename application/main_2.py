from application.bruteforce import Bruteforce
import csv
import os.path

input_path = 'C:\\Users\\butte\\PycharmProjects\\new dipl'
if os.path.isfile(os.path.join(input_path, 'kyri_dataset_3') + '.csv') is False:
    with open(os.path.join(input_path, 'kyri_dataset_3') + '.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(('time_matrix',
                             'configurations',
                             'answer',
                             'answer_time'))
        for i in range(100):
            new_item = Bruteforce()
            new_item.get_time_matrix()
            time, short_ans, full_ans = new_item.old(new_item.configurations1)
            for item in full_ans:
                filewriter.writerow((new_item.time_matrix, new_item.configurations1, item, time))