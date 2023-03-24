import os, argparse
from csv_manager import Manager

class CSVReader:
    DATASET_FOLDER = "datasets"

    def __init__(self):
        self.datafolder = CSVReader.DATASET_FOLDER
        self.csvs = list()

    def startup(self):        
        self.greeting()

    def initialize_csv_reader(self):
        Manager(self.DATASET_FOLDER + "/" + self.csvs[self.csv_id])
    
    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("~~~~~~ Basic CSV Parser ~~~~~~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    def menu_header(self):
        print("--------------------------------")
        print("Please make a selection:")
        print("(L): Load CSV file")
        print("(E): Exit program")

    def menu_error(self):
        print("Invalid selection. Please try again.")

    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("~-~-~-~-~-~~-~-~-~Goodbye!~-~-~-~-~-~-~-~~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    def select_csv(self):
        id_choice = input("Select CSV number:")
        try:
            csv_id_input = int(id_choice) - 1
            if csv_id_input >= 0 and csv_id_input < len(self.csvs):
                self.csv_id = csv_id_input
            else:
                self.menu_error()
                self.select_csv()
        except:
            self.menu_error()
            self.select_csv()
        self.initialize_csv_reader()

    def list_csvs(self):
        self.csvs = os.listdir(self.datafolder)
        for i, item in enumerate(self.csvs):
            #print(str(self.csvs.index(item)+1)+ ". " + item)
            print(str(i+1)+ ". " + item)
        self.select_csv()
        
    def menu(self):
        self.menu_header()

        selection = ""
        while (True):
            selection = input("Selection? ")

            if len(selection) == 0:
                self.menu_error()
                continue

            selection = selection.capitalize()
            if selection[0] == 'E':
                self.goodbye()
                break
            elif selection[0] == 'M':
                self.menu_header()
                continue
            elif selection[0] == 'L':
                print("----------------------------------")
                print("\nChoose CSV file:")
                # list the available quizzes
                self.list_csvs()
                self.menu_header()
                continue
            else:
                # if we get here, the user didn't make a valid selection
                self.menu_error()

    def run(self):
        self.startup()
        self.menu()

if __name__ == "__main__":
    app = CSVReader()
    app.run()
