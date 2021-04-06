import random


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def time_matrix_generator(time_matrix: list):
        sizes = {}
        for position_times_index in range(len(time_matrix)):
            sizes[position_times_index] = len(set(time_matrix[position_times_index]))

        final_matrix = []
        for index in range(len(sizes.keys())):
            time_matrix_row = [random.randint(5, 20) for _ in range(sizes[index])]
            final_matrix.append(time_matrix_row)

        return final_matrix

    def products_generator(self, num_of_positions: int, num_of_products: int):
        products = []
        i = 0
        while i < num_of_products:
            product = [0] * num_of_positions
            for position in range(len(product)):
                product[position] = random.randint(1, 3)
            if product not in products:
                products.append(product)
                i += 1

        time_matrix = []
        for position_index in range(len(products[0])):
            position_times = [item[position_index] for item in products]
            time_matrix.append(position_times)

        final_time_matrix = self.time_matrix_generator(time_matrix)

        return products, final_time_matrix

    def simple_product_generator(self):
        products = []
        num_of_products = 10
        num_of_positions = 3
        num_of_dif_positions = 3
        i = 0
        while i < num_of_products:
            product = [0] * num_of_positions
            for position in range(len(product)):
                product[position] = random.randint(1, num_of_dif_positions)
            if product not in products:
                products.append(product)
                i += 1

        self.time_matrix = [[random.randint(5, 20) for _ in range(num_of_dif_positions)] for __ in range(num_of_positions)]

        return products, self.time_matrix
