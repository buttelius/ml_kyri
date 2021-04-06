import math
from application.Utils import Utils


class Bruteforce:
    def __init__(self):
        utils = Utils()

        self.change_time_matrix = [[0] * len(self.configurations1) for _ in range(len(self.configurations1))]
        self.set_time_matrix = [0 for _ in range(len(self.configurations1))]
        self.configurations1, self.time_matrix = utils.simple_product_generator()

    def get_time_matrix(self):

        for i in range(len(self.configurations1)):
            for j in range(len(self.configurations1)):
                time_top, time_bot, time_rec = 0, 0, 0

                if self.configurations1[i][0] != self.configurations1[j][0]:
                    time_bot = self.time_matrix[0][self.configurations1[j][0] - 1]
                if self.configurations1[i][1] != self.configurations1[j][1]:
                    time_top = self.time_matrix[1][self.configurations1[j][1] - 1]
                if self.configurations1[i][2] != self.configurations1[j][2]:
                    time_rec = self.time_matrix[2][self.configurations1[j][2] - 1]

        for i in range(len(self.configurations1)):
            for j in range(len(self.configurations1[i])):
                self.set_time_matrix[i] += self.time_matrix[j][self.configurations1[i][j] - 1]

    @staticmethod
    def next_set(config_set):
        j = len(config_set) - 2
        while (config_set[j] > config_set[j + 1]) & (j != -1):
            j -= 1
        if j == -1:
            return True
        l = len(config_set) - 1
        while config_set[j] > config_set[l]:
            l -= 1
        temp = config_set[j]
        config_set[j] = config_set[l]
        config_set[l] = temp
        begin = j + 1
        end = len(config_set) - 1
        while begin < end:
            temp = config_set[begin]
            config_set[begin] = config_set[end]
            config_set[end] = temp
            begin += 1
            end -= 1
        return False

    def old(self, configurations):
        this_way = [i for i in range(len(configurations))]
        min_time = math.inf
        min_result = []
        max_count = math.factorial((len(configurations)))
        count = 1
        while True:
            result = []
            this_time = self.set_time_matrix[self.configurations1.index(configurations[this_way[0]])]
            for current in range(len(this_way) - 1):
                current_config = configurations[this_way[current]]
                next_config = configurations[this_way[current + 1]]
                result.append(configurations.index(current_config))
                this_time += self.change_time_matrix[self.configurations1.index(current_config)][
                    self.configurations1.index(next_config)]
            current_config = configurations[this_way[len(this_way) - 1]]
            result.append(configurations.index(current_config))
            if this_time < min_time:
                min_time = this_time
                min_result = list(result)
                list_results = [result]
            elif this_time == min_time:
                list_results.append(result)
            if self.next_set(this_way):
                break
            count += 1
            if count > max_count / 2:
                break
        answer = []
        for item in list_results:
            sub_answer = []
            for sub_item in item:
                sub_answer.append(self.configurations1[sub_item])
            answer.append(sub_answer)
        return min_time, list_results, answer