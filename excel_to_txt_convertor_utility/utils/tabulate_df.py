import pandas as pd
from tabulate import tabulate

def tabulate_df(df,csv_file):
    
    txtcode = tabulate(df, headers='keys', tablefmt='psql')
    txtfile = csv_file.split(".csv")[0] + ".txt"
    return txtcode,txtfile