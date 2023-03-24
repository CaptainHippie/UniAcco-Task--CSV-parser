# UniAcco Task- CSV-parser
 
 ## Prerequisites:
 1. Python 3.6 or higher installed
 2. Linux or Mac operating system because python virtual environment works differently in windows
 ## How to run:
1. Open a terminal inside the directory
2. activate virtual environment by the command '$ source venv/bin/activate'
if you see a (venv) symbol in the command prompt, it means it's activated
3. Run the program using the command '$ python3 main.py'
The rest is guided by command prompts

If you have a windows operating system, you can still run the application. Skip the virtual environment activation and install pandas module by 'pip install pandas' manually.

Support is added for multiple CSV files, just drop them inside the 'datasets' folder
Modules used:
csv, pandas, argparse(deprecated)

I couldn't find any use for argparse at the moment, but will try to add if the need arises
More complex operations using pandas will be added soon