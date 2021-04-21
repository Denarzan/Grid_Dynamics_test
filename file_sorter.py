"""
Sort file which is too large to fit into RAM.
The less RAM memory and the more the file to be sorted takes up, the more files will be created.
In this example RAM is 100000 B.
Create file with your size you can in randomizer.py
If you don't want to launch tests, delete commits on 71 and 72 rows:)
"""
from math import *
import os


def create_new_files(file_to_sort, number_of_files):
    """
    Create new files depending on RAM memory and file memory.
    :param file_to_sort: Name of file to sort.
    :param number_of_files: Number of temporary files.
    :return: Some amount of new files.
    """
    with open(file_to_sort) as first_file:
        count = sum(1 for _ in first_file)  # Count how many lines in the first file.
        first_file.seek(0)  # Moves pointer to the beginning.
        if number_of_files == 0:
            num_of_lines = 0
        else:
            num_of_lines = count / number_of_files  # Amount of lines in one file
        for i in range(number_of_files):
            head = [first_file.readline() for _ in range(ceil(num_of_lines))]  # Takes part of the
            with open("text" + str(i) + ".txt", 'w') as new_file:                   # text for one file.
                print(f"Writing to {new_file.name}...")
                new_file.writelines(head)  # Write part of the text to the file.


def sort_files(number_of_files):
    """
    Sort rows in the created files.
    :param number_of_files: Number of files.
    :return: Sorted files.
    """
    for i in range(number_of_files):
        with open("text" + str(i) + ".txt", 'r') as read_file:  # Read rows in the file and sort them.
            print(f"Reading {read_file.name}...")
            rows = read_file.readlines()
            rows.sort()
        with open("text" + str(i) + ".txt", 'w') as sorted_file:  # Write sorted rows to the file.
            print(f"Sorting in {sorted_file.name}...")
            for row in rows:
                file_string = ''.join(str(stn) for stn in row)  # Change the list to a string.
                sorted_file.write(file_string)


def merge_to_one_file(number_of_files):
    """
    It takes the lines from the specified files one by one, compares them and writes the sorted rows to the file.
    :param number_of_files: Number of files.
    :return: One file with sorted rows.
    """
    file_list = [[(open("text" + str(i) + ".txt", 'r')), i] for i in range(number_of_files)]  # Open all the files.
    buff = [(descriptor.readline(), index) for descriptor, index in file_list]  # Link a string with the file.
    with open('result.txt', 'w') as res_file:
        print(f"Sorting to {res_file.name}...")
        while any(map(lambda x: bool(x[0]), buff)):  # Check if there are any rows left.
            sorted_buff = sorted(filter(lambda x: x[0], buff))  # Sort them.
            res_file.write(str(sorted_buff[0][0]))  # Write rows to file.
            index = sorted_buff[0][1]  # Create new index

            buff[index] = (file_list[index][0].readline(), index)  # Add new row with index to the list.

    for file, _ in file_list:
        file.close()  # Close all files.
        #  For  unittests I put comments, after testing remove them
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file.name)  # Delete them.
        os.remove(path)


if __name__ == "__main__":
    buffer_size = 100000  # Size of RAM
    filename = 'new_test.txt'  # Name of file to sort
    total_size = os.stat(filename).st_size  # Size of file
    num_of_files = ceil(total_size / buffer_size)  # Amount of temporary files
    create_new_files(filename, num_of_files)
    sort_files(num_of_files)
    merge_to_one_file(num_of_files)
