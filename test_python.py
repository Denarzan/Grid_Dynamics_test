import unittest
import random
import string

from file_sorter import *


def generate_random_string(length):
    """
    Generate random string with given length.
    :param length: Length of the string
    :return: String.
    """
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for _ in range(length))
    return rand_string


def create_random_file(rand_file_name, min_str, max_str, number_of_rows):
    """
    Fill the chosen file with raws of random numbers.
    You can choose how many numbers will be in the row, how many rows and range of numbers.
    :param rand_file_name: Name of the file.
    :param min_str: The smallest row.
    :param max_str: The largest row.
    :param number_of_rows: Number of rows.
    :return: New file with random strings.
    """
    with open(rand_file_name, 'w') as f:
        for _ in range(number_of_rows):
            f.write(generate_random_string(random.randint(min_str, max_str)))
            f.write('\n')


class TestPython(unittest.TestCase):

    def test_small_file_sort(self):
        """
        Testing small file with 10 rows.
        :return: True
        """
        num_rows = 10
        min_amount = 1
        max_amount = 100
        test_file = 'new_test.txt'
        test_buffer_size = 200000
        create_random_file(test_file, min_amount, max_amount, num_rows)
        test_total_size = os.stat(test_file).st_size
        test_num_of_files = ceil(test_total_size / test_buffer_size)
        create_new_files(test_file, test_num_of_files)
        sort_files(test_num_of_files)
        merge_to_one_file(test_num_of_files)
        with open('new_test.txt', 'r') as test_file:
            lines = test_file.readlines()
            lines.sort()
        with open('new_test_sorted.txt', 'w') as test_sorted_file:
            for row in lines:
                file_string = ''.join(str(stn) for stn in row)
                test_sorted_file.write(file_string)
        with open('result.txt', 'r') as res:
            first = res.readlines()
        with open('new_test_sorted.txt', 'r') as test:
            second = test.readlines()
        self.assertEqual(first, second)

    def test_medium_file_sort(self):
        """
        Testing medium file with 1000 rows.
        :return: True
        """
        num_rows = 1000
        min_amount = 1
        max_amount = 100
        test_file = 'new_test.txt'
        test_buffer_size = 200000
        create_random_file(test_file, min_amount, max_amount, num_rows)
        test_total_size = os.stat(test_file).st_size
        test_num_of_files = ceil(test_total_size / test_buffer_size)
        create_new_files(test_file, test_num_of_files)
        sort_files(test_num_of_files)
        merge_to_one_file(test_num_of_files)
        with open('new_test.txt', 'r') as test_file:
            lines = test_file.readlines()
            lines.sort()
        with open('new_test_sorted.txt', 'w') as test_sorted_file:
            for row in lines:
                file_string = ''.join(str(stn) for stn in row)
                test_sorted_file.write(file_string)
        with open('result.txt', 'r') as res:
            first = res.readlines()
        with open('new_test_sorted.txt', 'r') as test:
            second = test.readlines()
        self.assertEqual(first, second)

    def test_huge_file_sort(self):
        """
        Testing huge file with
        :return:
        """
        num_rows = 100000
        min_amount = 1
        max_amount = 100
        test_file = 'new_test.txt'
        test_buffer_size = 200000
        create_random_file(test_file, min_amount, max_amount, num_rows)
        test_total_size = os.stat(test_file).st_size
        test_num_of_files = ceil(test_total_size / test_buffer_size)
        create_new_files(test_file, test_num_of_files)
        sort_files(test_num_of_files)
        merge_to_one_file(test_num_of_files)
        with open('new_test.txt', 'r') as test_file:
            lines = test_file.readlines()
            lines.sort()
        with open('new_test_sorted.txt', 'w') as test_sorted_file:
            for row in lines:
                file_string = ''.join(str(stn) for stn in row)
                test_sorted_file.write(file_string)
        with open('result.txt', 'r') as res:
            first = res.readlines()
        with open('new_test_sorted.txt', 'r') as test:
            second = test.readlines()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'new_test_sorted.txt')  # Delete them.
        os.remove(path)
        self.assertEqual(first, second)

    def test_temp_files_size(self):
        num_rows = 100000
        min_amount = 1
        max_amount = 100
        test_file = 'new_test.txt'
        test_buffer_size = 200000
        test_total_size = os.stat(test_file).st_size
        create_random_file(test_file, min_amount, max_amount, num_rows)
        test_num_of_files = ceil(test_total_size / test_buffer_size)
        create_new_files(test_file, test_num_of_files)
        sort_files(test_num_of_files)
        merge_to_one_file(test_num_of_files)
        for i in range(test_num_of_files):
            file_name = "text" + str(i) + ".txt"
            try:
                test_file_size = os.stat(file_name).st_size
                self.assertLess(test_file_size, test_buffer_size)
            except FileNotFoundError:
                self.assertTrue(True, True)

    def test_empty_file(self):
        num_rows = 0
        min_amount = 1
        max_amount = 100
        test_file = 'new_test.txt'
        test_buffer_size = 200000
        create_random_file(test_file, min_amount, max_amount, num_rows)
        test_total_size = os.stat(test_file).st_size
        test_num_of_files = ceil(test_total_size / test_buffer_size)
        create_new_files(test_file, test_num_of_files)
        sort_files(test_num_of_files)
        merge_to_one_file(test_num_of_files)
        with open('result.txt', 'r') as res:
            lines = res.readlines()
        self.assertEqual(first=lines, second=[])
