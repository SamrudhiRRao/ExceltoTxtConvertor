import pandas as pd
from tabulate import tabulate
import openpyxl
import sys

def readcsv(csv_file):
    
    if csv_file.endswith('.xlsx'):
        df = pd.read_excel (csv_file,engine='openpyxl') # reading xlsx file
    if csv_file.endswith('.xls'):
        df = pd.read_excel(csv_file) # reading xls file
    if csv_file.endswith('csv'):
        df = pd.read_csv (csv_file) # reading csv file
    else:
        print("File not supported")
        sys.exit()
    return df,csv_file