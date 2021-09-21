import pandas as pd
from tabulate import tabulate
import sys
import argparse

import os

from excel_to_txt_convertor_utility.utils.readcsv import readcsv
from excel_to_txt_convertor_utility.utils.tabulate_df import tabulate_df
from excel_to_txt_convertor_utility.utils.final_txt import final_txt

def main():

    try:
        my_parser = argparse.ArgumentParser(description='Convert csv to.txt file')
        my_parser.add_argument('--Path',
                       metavar='path',
                       type=str,
                       help='The file path')
        args = my_parser.parse_args()

        input_path = args.Path

        if not os.path.isfile(input_path):
            print('Either the file specified does not exist or check the path. If its windows then puth the path inside "" ')
            sys.exit()
        name_of_csv_file = input_path
        df,csv_file = readcsv(input_path) # Calls a function to read csv
        txtcode,txtfile = tabulate_df(df,csv_file) # Calls a function to use tabulate
        final_txt(txtcode,txtfile) # Calls a function to put the contents int .txt file
    except Exception as ex:
        print(ex)
        
if __name__ == "__main__":
    # print("\nName of CSV script:", sys.argv[1])
    main()