import csv
import os

from application.bruteforce import Bruterforce

# input_path = 'C:\\Users\\butte\\PycharmProjects\\new dipl'
path_to_assets = '/Users/alexkoz/projects/ml_kyri/assets'

if os.path.isfile(os.path.join(path_to_assets, 'dataset_test') + '.csv') is False:
    with open(os.path.join(path_to_assets, 'kyri_dataset_3') + '.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        filewriter.writerow(('time_1', 'time_2', 'time_3', 'time_4', 'time_5', 'time_6', 'time_7', 'time_8', 'time_9',

                             'conf_1', 'conf_2', 'conf_3', 'conf_4', 'conf_5', 'conf_6', 'conf_7', 'conf_8', 'conf_9',
                             'conf_10', 'conf_11', 'conf_12', 'conf_13', 'conf_14', 'conf_15', 'conf_16', 'conf_17',
                             'conf_18', 'conf_19', 'conf_20', 'conf_21', 'conf_22', 'conf_23', 'conf_24', 'conf_25',
                             'conf_26', 'conf_27', 'conf_28', 'conf_29', 'conf_30',

                             'answ_1', 'answ_2', 'answ_3', 'answ_4', 'answ_5', 'answ_6', 'answ_7', 'answ_8', 'answ_9',
                             'answ_10', 'answ_11', 'answ_12', 'answ_13', 'answ_14', 'answ_15', 'answ_16', 'answ_17',
                             'answ_18', 'answ_19', 'answ_20', 'answ_21', 'answ_22', 'answ_23', 'answ_24', 'answ_25',
                             'answ_26', 'answ_27', 'answ_28', 'answ_29', 'answ_30',

                             'answ_time'))
        for i in range(2):
            new_item = Bruterforce()
            new_item.get_time_matrix()
            time, short_ans, full_ans = new_item.old(new_item.configurations1)
            for item in full_ans:
                answer_config_list = []
                answer_time_list = []

                times_list = [time_value for sublist in new_item.time_matrix for time_value in sublist]
                configs_list = [change_value for sublist in new_item.configurations1 for change_value in sublist]
                item_list = [item_value for sublist in item for item_value in sublist]

                total_row = times_list + configs_list + item_list
                total_row.append(time)

                filewriter.writerow(total_row)
