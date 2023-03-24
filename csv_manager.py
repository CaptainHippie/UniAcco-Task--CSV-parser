import csv
import pandas as pd

class Manager:
    def __init__(self, dataset):
        self.dataset = dataset
        self.read()
        self.run()

    def read(self):
        # creating a pandas dataframe
        self.df = pd.read_csv(self.dataset)

        # parsing csv using csv module
        self.file = open(self.dataset)
        reader = csv.reader(self.file)
        self.columns = next(reader)
        self.numeric_columns = {}
        for col in self.df.select_dtypes(include='number').columns:
            self.numeric_columns[col] = self.columns.index(col)

        self.integer_columns = {}
        for col in self.df.select_dtypes(include=['int16', 'int32', 'int64']).columns:
            self.integer_columns[col] = self.columns.index(col)

        self.float_columns = {}
        for col in self.df.select_dtypes(include=['float16', 'float32', 'float64']).columns:
            self.float_columns[col] = self.columns.index(col)

        self.rows = []
        
        for row in reader:
            modified_row = []
            index = 0
                
            for item in row:
                if item == "":
                    item == "null"
                elif index in self.integer_columns.values():
                    item = int(item)
                elif index in self.float_columns.values():
                    item = float(item)
                modified_row.append(item)
                index += 1
            self.rows.append(modified_row)

    def print_column_labels(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        for header in self.columns:
            print(header + "  ", end='')
        print("\n")

    def print_csv(self):
        #print(self.df)
        self.print_column_labels()
        for row in self.rows:
            print(row)
        
    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("~~~~~~ CSV File loaded ~~~~~~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    def menu_error(self):
        print("Invalid selection. Please try again.")

    def query_not_found(self):
        print("No matching queries! Try a different value")

    def menu_header(self):
        print("--------------------------------")
        print("------"+ self.dataset.upper()+"-----")
        print("--------------------------------")
        print("(P): Print dataset")
        print("(C): Count the number of rows")
        print("(M): Calculate mean of a column")
        print("(F): Filter dataset by a column value")
        print("(E): Close dataset")

    def close_dataset(self):
        self.file.close()
        print("DATASET closed")

    def count_rows(self):
        print("There are " + str(len(self.rows)) + " rows in this datasaet")

    def print_columns(self):
        for i in range(0, len(self.columns)):
            print(f"({i}): {self.columns[i]}")

    def print_numeric_columns(self):
        for col in self.numeric_columns:
            print(f"({self.numeric_columns[col]}): {col}")

    def mean_colunmn(self):
        print("--------------------------------")
        self.print_numeric_columns()

        while (True):
            try:
                col_index = int(input("Choose a column id: "))
                print("Mean of the column " + self.df.columns[col_index] + " is: " + str(self.df[self.df.columns[col_index]].mean()))
                break
            except:
                self.menu_error()
    
    def filter_column(self, col_index):
        while True:
            value = input("Enter the value which you want to filter: ")
            if col_index in self.integer_columns.values() or col_index in self.float_columns.values():
                try:
                    value = float(value)
                except:
                    self.menu_error()
                    continue
            self.print_column_labels()
            #filtered_rows = []
            found = False
            for row in self.rows:
                if row[col_index] == value:
                    print(row)
                    found = True
                    #filtered_rows.append(row)
            if not found:
                self.query_not_found()
                continue
            #print(filtered_rows)
            break

    def choose_column_filter(self):
        print("--------------------------------")
        self.print_columns()

        while (True):
            col_index = input("Choose a column id you want to filter: ")
            try:
                col_index = int(col_index)
            except:
                self.menu_error()
                continue
            if col_index >= 0 and col_index < len(self.columns):
                self.filter_column(col_index)
                break
            else:
                self.menu_error()
                continue

    def menu(self):
        self.menu_header()

        selection = ""
        while (True):
            selection = input("Select operation? ")

            if len(selection) == 0:
                self.menu_error()
                continue

            selection = selection.capitalize()
            if selection[0] == 'E':
                self.close_dataset()
                break
            elif selection[0] == 'P':
                self.print_csv()
                self.menu_header()
                continue
            elif selection[0] == 'C':
                self.count_rows()
                self.menu_header()
                continue
            elif selection[0] == 'M':
                self.mean_colunmn()
                self.menu_header()
                continue
            elif selection[0] == 'F':
                self.choose_column_filter()
                self.menu_header()
                continue
            else:
                self.menu_error()

    def run(self):
        self.greeting()
        self.menu()

