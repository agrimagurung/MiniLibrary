'''
import csv, os


# StudentDataManager class to handle student data operations
class StudentDataManager:

    def __init__(self, username ):
        self.username = username

        










    # script from examples in https://realpython.com/python-csv/#parsing-csv-files-with-pythons-built-in-csv-library
    # data from kaggle - https://www.kaggle.com/datasets/bimalgajera/library-books
    with open('books_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0 # set line counter to 0 to start @ header row
        for row in csv_reader:
            if line_count == 0:


'''